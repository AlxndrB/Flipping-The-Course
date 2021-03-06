from main.models import Questions, Modules

# ========================================================= questions

# studie vragen
q = Questions(
    question='Weet je welke opleidingen er zijn?',
    gebied='studie'
)
q.save()
q = Questions(
    question='Vind je de studie leuk',
    gebied='studie'
)
q.save()
q = Questions(
    question='Heb je zicht op welke kennis en vaardigheden er nodig zijn voor deze opleiding?',
    gebied='studie'
)
q.save()
q = Questions(
    question='Heb je een idee van wat je leert bij deze opleiding?',
    gebied='studie'
)
q.save()

# toekomst vragen
q = Questions(
    question='Weet je welk werk je later kan doen met deze opleiding?',
    gebied='toekomst'
)
q.save()
q = Questions(
    question='Sluiten de toekomsige werkmogelijkheden aan op jouw interesses?',
    gebied='toekomst'
)
q.save()
q = Questions(
    question='Weet je (ongeveer) waar je kan gaan werken met deze opleiding?',
    gebied='toekomst'
)
q.save()
q = Questions(
    question='Weet je hoe snel je een baan vindt met deze opleding?',
    gebied='toekomst'
)
q.save()

# sociaal vragen
q = Questions(
    question='Ken jij de studenten van de opleiding?',
    gebied='sociaal'
)
q.save()
q = Questions(
    question='Heb je het gevoel dat je bij de studenten van deze opleiding past?',
    gebied='sociaal'
)
q.save()
q = Questions(
    question='Heb je zicht op wat je naast je opleiding kan doen?',
    gebied='sociaal'
)
q.save()
q = Questions(
    question='Weet je wat het \'studentenleven\' voor jou inhoudt?',
    gebied='sociaal'
)
q.save()


# ==================================================================================== modules

p = Modules(
    gebied='studie',
    naam='Webklassen',
    omschrijving='Online cursus over bepaalde bachelor opleidingen',
    tijd=16,
    kosten=240,
    baten_vast=240,
    # baten_flex=,
    experience_vast=192,
    # experience_flex=,
    # factor=,
    niveau=2
)
p.save()

p = Modules(
    gebied='toekomst',
    naam='Case',
    omschrijving='Een probleem oplossen voor een bedrijf',
    tijd=3,
    kosten=45,
    baten_vast=45,
    # baten_flex=,
    # experience_vast=,
    # experience_flex=,
    # factor=,
    niveau=1
)
p.save()


p = Modules(
    gebied='sociaal',
    naam='Borrel studievereniging',
    omschrijving='Vrijdag middag borrel met lezing/praatje',
    tijd=2,
    kosten=60,
    # baten_vast=,
    # baten_flex=,
    experience_vast=48,
    # experience_flex=,
    # factor=,
    niveau=1
)
p.save()

p = Modules(
    gebied='studietoekomst',
    naam='Een dag student',
    omschrijving='Een dagje student zijn',
    tijd=8,
    kosten=120,
    baten_vast=240,
    # baten_flex=,
    experience_vast=92,
    # experience_flex=,
    # factor=,
    niveau=1
)
p.save()

p = Modules(
    gebied='studiesociaal',
    naam='Opendag op locatie',
    omschrijving='Een specifieke opleiding beter leren kennen',
    tijd=8,
    kosten=240,
    # baten_vast=,
    # baten_flex=,
    experience_vast=192,
    # experience_flex=,
    # factor=,
    niveau=1
)
p.save()

p = Modules(
    gebied='sociaaltoekomst',
    naam='Excursie met studievereniging',
    omschrijving='Bij een bedrijf op bezoek',
    tijd=4,
    kosten=120,
    # baten_vast=,
    # baten_flex=,
    experience_vast=94,
    # experience_flex=,
    # factor=,
    niveau=2
)
p.save()
