"""Author the static deliverable files; the website itself has no build step."""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
(root / 'assets').mkdir(exist_ok=True)
cities = [
    dict(slug='springfield', name='Springfield', role='The state capital', region='Central Illinois', population='114,394', year='1840', income=42670, density='1,871.1', intro='Meet Illinois at its political and historic heart. Springfield brings state government and the story of Abraham Lincoln into the same walkable city.', history='https://www.lincolnlibrary.info/learn/sangamon-valley-collection/indexes-pathfinders/city-officials', official='https://www.springfield.il.us/', stops=['Explore the Illinois State Capitol area.', 'Visit the Lincoln Home National Historic Site.', 'Learn about the city at Lincoln Library.']),
    dict(slug='chicago', name='Chicago', role='The lakefront metropolis', region='Northeastern Illinois, on Lake Michigan', population='2,746,388', year='1837', income=50086, density='12,059.8', intro='A city of neighborhoods, a vast lakefront, and a skyline that rewards looking up. Chicago offers a different view of Illinois around every corner.', history='https://www.chicityclerk.com/about-city-council', official='https://www.chicago.gov/', stops=['Walk along the Lake Michigan waterfront.', 'Explore the public spaces of Millennium Park.', 'Discover the architecture along the Chicago River.']),
    dict(slug='peoria', name='Peoria', role='Life along the Illinois River', region='Central Illinois, on the Illinois River', population='113,150', year='1845', income=38466, density='2,359.0', intro='Follow the Illinois River to Peoria. Its riverfront and surrounding neighborhoods offer a city experience shaped by the water.', history='https://www.peoriagov.org/733/Transparency', official='https://www.peoriagov.org/', stops=['Start at the downtown riverfront.', 'Explore the Peoria Riverfront Museum.', 'Take in the views along Grandview Drive.'])
]

def illustration(slug):
    # Original vector drawings represent each place; they are not photographs.
    base = '<svg xmlns="http://www.w3.org/2000/svg" width="960" height="480" viewBox="0 0 960 480"><rect width="960" height="480" fill="#dce9ef"/><circle cx="780" cy="95" r="44" fill="#e8b66d"/>'
    if slug == 'springfield':
        scene = '<path d="M0 360Q240 320 480 360T960 350V480H0" fill="#a2b5a2"/><rect x="215" y="245" width="530" height="150" fill="#ded5bf"/><path d="M170 260L480 155L790 260Z" fill="#acaa9d"/><rect x="415" y="130" width="130" height="110" fill="#b4b6ab"/><path d="M415 135Q480 5 545 135Z" fill="#6a827b"/><path d="M480 25V0" stroke="#435e59" stroke-width="8"/>'
        scene += ''.join(f'<rect x="{x}" y="280" width="25" height="110" fill="#f6f0df"/>' for x in range(250,730,60))
    elif slug == 'chicago':
        scene = '<path d="M0 365H960V480H0Z" fill="#7da5b8"/>'
        scene += ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{365-y}" fill="{c}"/>' for x,y,w,c in [(50,210,95,'#849baa'),(165,150,90,'#547082'),(280,70,100,'#2e4a60'),(390,190,100,'#9aacb3'),(515,125,100,'#587c90'),(645,180,100,'#718e9b'),(765,225,120,'#adc0c7')])
        scene += '<path d="M305 70V30M350 70V15" stroke="#2e4a60" stroke-width="6"/><path d="M0 405H960M0 435H960" stroke="#bed5df" stroke-width="3"/>'
    else:
        scene = '<path d="M0 230Q200 150 400 230T960 210V480H0" fill="#96ad96"/><path d="M0 290Q250 240 450 330T960 300V480H0" fill="#7ea9bc"/><path d="M0 280Q220 220 460 270T960 260" fill="none" stroke="#465f6e" stroke-width="18"/><path d="M180 265V380M400 265V430M650 280V440M850 270V390" stroke="#465f6e" stroke-width="12"/><path d="M60 410H220L195 440H85Z" fill="#f4ede0"/><rect x="110" y="375" width="65" height="35" fill="#a84624"/>'
    return base + scene + '</svg>'

for city in cities:
    (root / 'assets' / (city['slug'] + '.svg')).write_text(illustration(city['slug']), encoding='utf-8')
(root / 'assets/illinois.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="180" height="220" viewBox="0 0 180 220"><path d="M55 10L136 10L145 45L137 95L148 139L130 169L120 205L91 194L83 170L55 152L63 128L43 110L49 87L30 65L49 50Z" fill="#a84624"/><circle cx="116" cy="42" r="6" fill="white"/><circle cx="83" cy="105" r="6" fill="white"/><circle cx="91" cy="140" r="6" fill="white"/></svg>', encoding='utf-8')

nav = [('index', 'Home'), ('springfield', 'Springfield'), ('chicago', 'Chicago'), ('peoria', 'Peoria'), ('contact', 'Ask a question')]

def frame(slug, title, body, aside):
    links = '\n'.join(f'<li><a href="{key}.html"' + (' aria-current="page"' if key == slug else '') + f'>{label}</a></li>' for key, label in nav)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Explore Illinois and three of its cities through this educational website.">
  <title>{title} | Explore Illinois</title>
  <link rel="stylesheet" href="styles.css">
  <script src="script.js" defer="defer"></script>
</head>
<body>
  <!-- The same frame and navigation appear on all five pages. -->
  <header class="container site-header">
    <a class="brand" href="index.html"><span class="site-mark" aria-hidden="true">◈</span> Explore Illinois</a>
    <p class="project-note">An educational city guide</p>
  </header>
  <nav class="nav-bar" aria-label="Main navigation"><ul class="container nav-list">{links}</ul></nav>
  <main class="container page-layout">
    <section class="stack" aria-labelledby="page-title">{body}</section>
    <aside class="stack" aria-labelledby="aside-title">{aside}</aside>
  </main>
  <footer class="container site-footer"><p>Explore Illinois · Student practice project · Not a government website.</p><a href="contact.html">Ask a question</a></footer>
</body>
</html>'''.replace('><', '>\n<')

def figure(slug, alt, label):
    return f'<figure class="scene"><img src="assets/{slug}.svg" width="960" height="480" alt="{alt}"><figcaption class="image-label">{label} · original illustration</figcaption></figure>'

def external(url, label):
    return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{label} (opens in a new tab)</a>'

cards = ''.join(f'<article class="city-card"><img src="assets/{c["slug"]}.svg" width="130" height="90" alt="Illustrated view of {c["name"]}."><div><h3>{c["name"]}</h3><p>{c["role"]}</p><a href="{c["slug"]}.html">Explore {c["name"]}</a></div></article>' for c in cities)
rows = ''.join(f'<tr><th scope="row"><a href="{c["slug"]}.html">{c["name"]}</a></th><td class="numeric">{c["population"]}</td><td>{c["year"]}</td><td class="numeric">${c["income"]:,}</td></tr>' for c in cities)
home = f'''<p class="eyebrow">One state. Three perspectives.</p><h1 id="page-title">Discover Illinois.</h1>
<p class="lead">From the state capital to the lakefront and the river, get to know three distinct Illinois cities.</p>
{figure('chicago','Illustration of the Chicago skyline beside blue Lake Michigan.','Illinois / Chicago lakefront')}
<div class="intro"><img class="state-image" src="assets/illinois.svg" width="180" height="220" alt="Stylized Illinois outline with three markers representing Chicago, Peoria, and Springfield."><h2>A place to begin</h2><p>Illinois is a Midwestern state with Springfield as its capital. This guide connects the history of Springfield, the scale of Chicago, and the river setting of Peoria. Choose a city to explore its people, location, and story.</p></div>
<h2>Explore the cities</h2><div class="city-cards">{cards}</div>
<h2>Plan a three-stop introduction</h2><ol><li>Start in Springfield for the state capital and Lincoln history.</li><li>Head to Peoria for an Illinois River perspective.</li><li>Finish in Chicago for the Lake Michigan waterfront.</li></ol>
<div class="table-scroll"><table><caption>Three cities at a glance</caption><thead><tr><th scope="col">City</th><th scope="col">2020 population</th><th scope="col">City incorporation</th><th scope="col">Income per person</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="small">Population: April 1, 2020 Census. Income: 2020–2024 American Community Survey, in 2024 dollars. Per-capita income is total income divided by population, not a wage or median household income.</p>
<section class="sources stack" aria-labelledby="sources-title"><h2 id="sources-title">Sources</h2><p>Population and income: {', '.join(external('https://www.census.gov/quickfacts/'+c['slug']+'cityillinois',c['name']+' QuickFacts') for c in cities)}. Incorporation sources appear on each city page.</p><p>State context: {external('https://www.illinois.gov/','State of Illinois')}. All illustrations are original vector artwork for this project.</p></section>'''
aside = '<h2 id="aside-title">Illinois at a glance</h2><ul><li>Capital: Springfield</li><li>Region: Midwest</li><li>Three cities to explore</li></ul><h3>Keep exploring</h3><p>'+external('https://www.illinois.gov/','Official Illinois website')+'</p><p><a href="contact.html">Have a question?</a></p>'
(root / 'index.html').write_text(frame('index', 'Discover Illinois', home, aside), encoding='utf-8')

for c in cities:
    diff = c['income'] - 46406
    compare = f'${abs(diff):,} {"above" if diff > 0 else "below"} the Illinois figure of $46,406.'
    body = f'''<p class="eyebrow">{c['role']}</p><h1 id="page-title">{c['name']}</h1><p class="lead">{c['intro']}</p>
{figure(c['slug'], {'springfield':'Illustration of the domed Illinois State Capitol in Springfield.','chicago':'Illustration of the Chicago skyline along Lake Michigan.','peoria':'Illustration of a bridge and boat on the Illinois River at Peoria.'}[c['slug']],c['name'])}
<h2>Five things to know</h2><dl class="facts"><dt>Population</dt><dd>{c['population']} residents (April 1, 2020 Census).</dd><dt>Incorporated as a city</dt><dd>{c['year']}</dd><dt>Region</dt><dd>{c['region']}</dd><dt>Classification</dt><dd>Urban city. This guide uses an urban description based on its city setting and density of {c['density']} people per square mile (2020).</dd><dt>Average income comparison</dt><dd>${c['income']:,} per person; {compare} Both values use 2020–2024 ACS estimates, in 2024 dollars.</dd></dl>
<h2>A few places to start</h2><ol>{''.join('<li>'+s+'</li>' for s in c['stops'])}</ol>
<section class="sources stack" aria-labelledby="sources-title"><h2 id="sources-title">Sources and notes</h2><ul><li>{external('https://www.census.gov/quickfacts/'+c['slug']+'cityillinois',c['name']+' Census QuickFacts')}: population, density, and per-capita income.</li><li>{external('https://www.census.gov/quickfacts/illinois','Illinois Census QuickFacts')}: comparable state income.</li><li>{external(c['history'],'City incorporation history')}: incorporation year.</li><li>{external(c['official'],'Official city website')}: local context and resources.</li></ul><p class="small">Region labels are geographic descriptions. Urban classification is editorial, not an official zoning designation. Income differences are arithmetic comparisons, not claims of statistical significance. Illustration: original project artwork.</p></section>'''
    aside = f'<h2 id="aside-title">{c["name"]} at a glance</h2><p>{c["role"]}</p><h3>Other cities</h3><ul>'+''.join(f'<li><a href="{other["slug"]}.html">{other["name"]}</a></li>' for other in cities if other != c)+'</ul><p><a href="index.html">Back to Illinois</a></p><p><a href="contact.html">Ask a question</a></p>'
    (root / (c['slug'] + '.html')).write_text(frame(c['slug'], c['name'], body, aside), encoding='utf-8')

fields = ''.join(f'<div class="field"><label for="{id}">{label}</label><input id="{id}" name="{id}" type="{type}" autocomplete="{auto}" required="required" disabled="disabled"></div>' for id,label,type,auto in [('first-name','First name','text','given-name'),('last-name','Last name','text','family-name'),('email','Email address','email','email'),('confirm-email','Confirm email address','email','email')])
contact = f'''<p class="eyebrow">Let curiosity lead</p><h1 id="page-title">Ask a question.</h1><p class="lead">What would you like to know about Illinois or its cities?</p>
<p>This is a practice form. All fields are required. Your question is checked in this browser and is never sent or saved.</p>
<noscript><p>Enable JavaScript to use the local email confirmation check. The form is disabled until JavaScript loads.</p></noscript>
<form id="contact-form" action="contact.html" method="get">{fields}<div class="field full"><label for="question">Your question</label><textarea id="question" name="question" rows="6" required="required" disabled="disabled"></textarea></div><button type="submit" disabled="disabled">Submit</button><p id="form-status" class="full" role="status" aria-live="polite"></p></form>'''
aside = '<h2 id="aside-title">Explore while you think</h2><img src="assets/illinois.svg" width="180" height="220" alt="Stylized outline of Illinois with markers for the three featured cities."><ul><li><a href="springfield.html">Springfield</a></li><li><a href="chicago.html">Chicago</a></li><li><a href="peoria.html">Peoria</a></li></ul><p class="small">Original illustration. Educational practice site, not an official contact service.</p>'
(root / 'contact.html').write_text(frame('contact','Ask a question',contact,aside),encoding='utf-8')
print('Created five complete HTML pages and four local SVG illustrations.')
