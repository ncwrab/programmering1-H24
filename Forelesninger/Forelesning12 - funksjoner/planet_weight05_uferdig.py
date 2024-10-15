# Full versjon med utfyllende kommentarer kommer neste gang :)

# definerer en funksjon som skal skrive ut en "fin" overskrift til brukeren
# Funksjonen trenger ikke returnere noen verdi
def skriv_header():
    print("\n ========================================")
    print(" ==  Hva er din vekt på en annen planet? ==")
    print(" =========================================")

# definerer en funksjon som skal skrive ut planetene fra en samling med planeter
# Funksjonen har 1 parameter, og denne er tenkt å være en liste med dictionaries
# Funksjonen trener ikke returnere noen verdi
def skriv_ut_planetliste(planeter_som_skal_skrives_ut):
    for index, planet in enumerate(planeter_som_skal_skrives_ut):      # enumerate returnerer et tall/index og listeinnholdet på på den indeksen, disse vil bli mellomlagret for hver iterasjon som hhv. index og planet
        print(f"{index} - {planet['navn']}")

# Liste med planeter. På hver indeks i lista er en dictionary for hver planet. Hver dictionary har to key-value-par, bortsett fra den første.
planeter = [{'navn' : 'Tilfeldig planet'},
            {'navn':'Merkur', 'tyngdekraft':3.7},
            {'navn': 'Venus', 'tyngdekraft' : 8.87},
            {'navn': 'Jorden', 'tyngdekraft' : 9.807},
            {'navn': 'Mars', 'tyngdekraft': 3.721},
            {'navn': 'Jupiter', 'tyngdekraft': 24.79},
            {'navn': 'Saturn', 'tyngdekraft': 10.44},
            {'navn': 'Uranus', 'tyngdekraft': 8.87},
            {'navn': 'Neptun', 'tyngdekraft':11.15}
            ]


#-------------------------# Bare en skillelinje. Over er funksjonsdefinisjoner, variabler og importer, under er løkke med selve 'programmet'

run = True
while run ==True:
    # " PSEUDOKODE"
    #Skrive ut overskrift
    skriv_header()
    #Skrive ut liste over planeter
    skriv_ut_planetliste(planeter)
    #Ta input med valg, og en tilbakemelding
    planetnummer = int(input("\n Velg en planet ved å skrive inn et tall: "))
    #Ta input med vekt
    #Beregninger
    #Tilbakemelding

    #Ta input om avslutning


    #Midlertidig avslutningskode
    run = False
