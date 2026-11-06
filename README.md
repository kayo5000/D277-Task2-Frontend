# Explore Illinois

An original five-page HTML, CSS, and JavaScript practice website based on the two Task 1 wireframes. Open index.html directly; there is no build step or runtime dependency. This is an educational guide, not an official government website.

## Files and choices

- index.html introduces Illinois, links to each city, and contains the required list and comparison table.
- springfield.html, chicago.html, and peoria.html share the interior layout and provide all five city facts.
- contact.html contains the required names, email, confirmation email, question, and Submit controls.
- styles.css is the only stylesheet. Grid places the main section beside the aside. Flex handles navigation and city rows. A media query stacks the layout on phones. Arial is the body family; Georgia distinguishes headings.
- script.js is the only browser script. It enables the form, prevents server submission, compares the email fields, alerts on a mismatch, and gives local success feedback when they match. Disabled controls prevent accidental submission if JavaScript fails or is unavailable.
- assets/ contains four original SVG illustrations. These load offline and have descriptive HTML alt text. They depict places symbolically and are not photographs or accurate maps.
- layouts/ contains two updated low-level drawings. LAYOUT-CHANGES.md explains the additions.
- screenshots/ contains all five pages at 375px and 1280px.
- QA.md maps the assignment checks to implementation evidence. SUBMISSION.md records the project addresses and external grading status.
- verification/ contains development-only page-authoring and browser-check scripts. The delivered HTML is complete; users do not run these scripts to open the site.

## Required CSS examples

The body element selector sets the font. The city-card class is reused three times on the home page. The contact-form id selector styles the form. Navigation links change background on hover. The Illinois image floats left so introductory text wraps around it. The image caption is absolutely positioned within a relative figure. The site mark is relatively moved down by 2px for alignment.

## Data and attribution

Population is the April 1, 2020 Census count for each city. Income is per-capita income from the 2020–2024 ACS, expressed in 2024 dollars. It is a mean per resident, not median household income or salary. Illinois is $46,406; Springfield $42,670; Chicago $50,086; Peoria $38,466. Differences are simple subtraction. City densities support an editorial urban classification, not a legal or zoning designation.

Primary sources, checked November 6, 2026:

- [Springfield Census QuickFacts](https://www.census.gov/quickfacts/springfieldcityillinois)
- [Chicago Census QuickFacts](https://www.census.gov/quickfacts/chicagocityillinois)
- [Peoria Census QuickFacts](https://www.census.gov/quickfacts/peoriacityillinois)
- [Illinois Census QuickFacts](https://www.census.gov/quickfacts/illinois)
- [Springfield incorporation — Lincoln Library](https://www.lincolnlibrary.info/learn/sangamon-valley-collection/indexes-pathfinders/city-officials)
- [Chicago incorporation — Office of the City Clerk](https://www.chicityclerk.com/about-city-council)
- [Peoria incorporation — city government](https://www.peoriagov.org/733/Transparency)

Links also appear beside the facts on the website. Geographic regions are descriptive. Original illustrations and code were authored with Codex for this practice exercise; review and understand them before using them in assessed coursework.

## Verification

Run `npx html-validate index.html springfield.html chicago.html peoria.html contact.html` for markup checks. The validator configuration accepts explicitly quoted boolean attributes.

The original browser run uses Google Chrome through Playwright. To repeat independently, install Playwright in verification (`npm install --prefix verification playwright`), then run `node verification/check.cjs` from this folder. It captures ten screenshots and checks structure, images, local link targets, navigation, required CSS, and the form. The site itself does not require Playwright.
