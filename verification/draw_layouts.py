"""Draw the two updated grayscale layout images for the assignment."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

out = Path(__file__).resolve().parent.parent / 'layouts'
out.mkdir(exist_ok=True)
def font(size, bold=False):
    return ImageFont.truetype('C:/Windows/Fonts/' + ('arialbd.ttf' if bold else 'arial.ttf'), size)
for city in [False, True]:
    im = Image.new('RGB', (1440, 1740), 'white')
    d = ImageDraw.Draw(im)
    def text(x,y,s,size=22,bold=False):
        d.text((x,y),s,fill='#222222',font=font(size,bold))
    def box(rect,label,lines):
        d.rectangle(rect,fill='#f3f3f3',outline='#555555',width=2)
        x,y,_,_ = rect
        text(x+18,y+16,label,24,True)
        for i,line in enumerate(lines): text(x+18,y+58+i*34,line,21)
    text(60,30,'UPDATED INTERIOR / CITY PAGE' if city else 'UPDATED HOME / ILLINOIS',34,True)
    text(60,84,'Task 2 layout | Grayscale structure | Desktop view',22)
    box((60,140,1380,255),'HEADER',['Explore Illinois site identity / educational project note'])
    box((60,280,1380,395),'NAV',['Home | Springfield | Chicago | Peoria | Ask a question'])
    box((60,425,990,1510),'SECTION / CITY PROFILE' if city else 'SECTION / STATE INTRODUCTION',[
        'City title, role, and introduction' if city else 'State title and introduction',
        'Relevant local illustration with alt text and caption'])
    d.rectangle((84,565,966,825),fill='white',outline='#999999',width=2)
    d.line((84,565,966,825),fill='#cccccc',width=2)
    d.line((966,565,84,825),fill='#cccccc',width=2)
    text(330,680,'IMAGE PLACEHOLDER',22,True)
    if city:
        box((84,855,966,1165),'FIVE CITY FACTS',[
            'Population: 2020 Census count', 'Incorporated as a city: year',
            'Region: location within Illinois', 'Classification: urban, with density/context',
            'Income per person: city vs. Illinois, same ACS period'])
        box((84,1190,966,1320),'PLACES TO START',['Ordered list: three local places'])
        box((84,1345,966,1485),'SOURCES AND NOTES',['Census, incorporation history, official city links', 'Method notes and original artwork credit'])
    else:
        box((84,855,966,1000),'STATE CONTEXT',['Small floated Illinois illustration and wrapped introduction'])
        box((84,1020,966,1185),'THREE CITY ROWS',['Springfield: image, capital label, and link','Chicago: image and link','Peoria: image and link'])
        box((84,1205,966,1305),'ORDERED ITINERARY',['Three stops: Springfield, Peoria, Chicago'])
        box((84,1325,966,1485),'COMPARISON TABLE AND SOURCES',['City | Population | Incorporated | Income per person','Three data rows; dated measures and source links'])
    box((1015,425,1380,1510),'ASIDE / RELATED INFO',[
        'City at a glance' if city else 'Illinois at a glance',
        'Capital / city role', '', 'Other city links' if city else 'State facts: three items',
        'Official resources', '', 'Ask a question link'])
    box((60,1535,1380,1650),'FOOTER',['Educational project note / contact link'])
    text(60,1680,'Phone layout: section first, then aside; navigation wraps. See LAYOUT-CHANGES.md.',21)
    im.save(out / ('interior-layout-updated.png' if city else 'home-layout-updated.png'))
print('Two updated layout images saved.')
