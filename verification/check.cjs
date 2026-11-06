// Run from task-2: node verification/check.cjs
let chromium;
try {
  ({ chromium } = require('playwright'));
} catch {
  // Reuse the existing local practice tools when available.
  ({ chromium } = require('../../../recipe-practice/verification/node_modules/playwright'));
}
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const assert = require('node:assert/strict');

(async () => {
  const browser = await chromium.launch({ headless: true, channel: 'chrome' });
  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  const files = ['index', 'springfield', 'chicago', 'peoria', 'contact'];
  fs.mkdirSync('screenshots', { recursive: true });
  const local = name => pathToFileURL(path.resolve(name + '.html')).href;
  for (const file of files) {
    for (const width of [375, 1280]) {
      await page.setViewportSize({ width, height: 900 });
      await page.goto(local(file));
      await page.evaluate(() => document.fonts.ready);
      const state = await page.evaluate(() => ({
        overflow: document.documentElement.scrollWidth > innerWidth,
        h1: document.querySelectorAll('h1').length,
        landmarks: ['header', 'nav', 'main', 'section', 'aside', 'footer'].every(tag => document.querySelector(tag)),
        images: [...document.images].every(img => img.complete && img.naturalWidth && img.alt),
        headings: [...document.querySelectorAll('h1,h2,h3,h4')].map(h => Number(h.tagName[1])),
        nav: [...document.querySelectorAll('nav a')].map(a => a.getAttribute('href')),
        active: document.querySelectorAll('nav [aria-current="page"]').length,
        links: [...document.querySelectorAll('a')].map(a => a.getAttribute('href'))
      }));
      assert.equal(state.overflow, false, `${file} ${width} overflow`);
      assert.equal(state.h1, 1);
      assert.ok(state.landmarks && state.images);
      assert.equal(state.active, 1);
      assert.deepEqual(state.nav, files.map(name => name + '.html'));
      state.headings.forEach((level, index) => assert.ok(!index || level <= state.headings[index - 1] + 1));
      for (const link of state.links.filter(link => !link.startsWith('http'))) {
        assert.ok(fs.existsSync(link.split('#')[0]));
      }
      await page.screenshot({ path: `screenshots/${file}-${width}.png`, fullPage: true });
      console.log(`PASS ${file} ${width}: structure, headings, images, links, overflow`);
    }
  }
  await page.goto(local('index'));
  assert.equal(await page.locator('.city-card').count(), 3);
  assert.equal(await page.locator('tbody tr').count(), 3);
  assert.equal(await page.locator('thead th').count(), 4);
  assert.ok(await page.locator('ol li').count() >= 3);
  const css = await page.evaluate(() => ({
    floated: getComputedStyle(document.querySelector('.state-image')).float,
    absolute: getComputedStyle(document.querySelector('.image-label')).position,
    relative: getComputedStyle(document.querySelector('.site-mark')).position
  }));
  assert.deepEqual(css, { floated: 'left', absolute: 'absolute', relative: 'relative' });
  const nav = page.locator('nav a').nth(1);
  const before = await nav.evaluate(e => getComputedStyle(e).backgroundColor);
  await nav.hover();
  assert.notEqual(await nav.evaluate(e => getComputedStyle(e).backgroundColor), before);
  await page.goto(local('contact'));
  await page.getByRole('button', { name: 'Submit', exact: true }).click();
  assert.equal(await page.locator('form').evaluate(f => f.checkValidity()), false);
  await page.locator('#first-name').fill('Practice');
  await page.locator('#last-name').fill('Visitor');
  await page.locator('#email').fill('visitor@example.test');
  await page.locator('#confirm-email').fill('other@example.test');
  await page.locator('#question').fill('Where can I learn about Springfield?');
  const dialogPromise = page.waitForEvent('dialog');
  const clickPromise = page.getByRole('button', { name: 'Submit', exact: true }).click();
  const dialog = await dialogPromise;
  assert.equal(dialog.type(), 'alert');
  assert.match(dialog.message(), /do not match/);
  await dialog.accept();
  await clickPromise;
  assert.equal(await page.locator('#confirm-email').getAttribute('aria-invalid'), 'true');
  await page.locator('#confirm-email').fill('visitor@example.test');
  assert.equal(await page.locator('#confirm-email').getAttribute('aria-invalid'), null);
  const requests = [];
  page.on('request', request => requests.push(request.url()));
  await page.getByRole('button', { name: 'Submit', exact: true }).click();
  assert.match(await page.locator('#form-status').innerText(), /passed the local checks/);
  assert.equal(requests.length, 0);
  await page.locator('#email').fill('invalid');
  assert.equal(await page.locator('form').evaluate(f => f.checkValidity()), false);
  const noScript = await browser.newContext({ javaScriptEnabled: false });
  const disabledPage = await noScript.newPage();
  await disabledPage.goto(local('contact'));
  assert.equal(await disabledPage.locator('button').isDisabled(), true);
  assert.equal(errors.length, 0);
  console.log('PASS form: required, invalid email, mismatch alert, correction, local success, no requests, JavaScript disabled');
  console.log('PASS required CSS: float, absolute/relative positions, hover, reused class; table/list counts; zero page errors');
  await browser.close();
})().catch(error => { console.error(error); process.exitCode = 1; });
