
import random

# definerer en funksjon som skal skrive ut en "fin" overskrift til brukeren
# Funksjonen trenger ikke returnere noen verdi
def skriv_header():
    print("\n ========================================")
    print(" ==  Hva er din vekt på en annen planet? ==")
    print(" =========================================")

# definerer en funksjon som skal skrive ut planetene fra en liste
# Funksjonen har 1 parameter, og denne er tenkt å være en liste
# Funksjonen trenger ikke returnere noen verdi
def skriv_ut_planetliste(planeter_som_skal_skrives_ut):
    for index, planet in enumerate(planeter_som_skal_skrives_ut):
        print(f"{index} - {planet['navn']}")

# definerer en funksjon som skal velge en tilfeldig planet fra lista.
# funksjonen har 1 parameter, og denne er tenkt å være en liste (listen med planeter)
# Bruker randrange() for å velge et tilfeldig tall mellom 1 og antall elementer i lista
# Funksjonen skal returnere navnet på den tilfeldig valgte planeten (string)
def velg_tilfeldig(valgt_samling):
    random_index = random.randrange(1, len(valgt_samling))
    valgt_element = valgt_samling[random_index]
    return valgt_element

# definerer en funksjon som skal beregne brukerens vekt på den valgte planeten
# funksjonen har 3 parametere: brukerens vekt, tyngdekraften på valgt planet og jordens tyngdekraft
# Den tredje parameteren, jordens tyngdekraft, setter vi en standardverdi for (=9,807). Det innebærer at dersom vi kun sender med 2 argumenter når vi kaller funksjonen, så vil den bruke standardvedien vi satt for jordens tyngdekraft som den tredje parameteren)
# Legg merke til at vi bruker de interne variabelnavnene våre (fra parameterne) når vi gjør beregningen
# Funksjonen skal returnere den beregnede vekten, avrundet til 2 desimaler (float)
def beregn_vekt(din_vekt, planettyngdekraft, jordtyngdekraft=9.807):
    beregnet_vekt = (din_vekt/jordtyngdekraft)*planettyngdekraft
    return round(beregnet_vekt, 2)
  
# definerer en funksjon for å styre hvorvidt løkka (og dermed programmet vårt) skal kjøre en gang til
# Vi ber brukeren om å skrive inn Y eller N.
# Ved å omgjøre brukerens input til store bokstaver med upper() vil både stor og liten y godkjennes for å kjøre en gang til
# Funksjonen skal returnere enten True eller False (bool) basert om om brukerens input var Y eller ikke.
def en_gang_til():
    svar = input("Vil du prøve en gang til? (Y/N)")
    return svar.upper() == 'Y'

# En liste der hvert element i lista er en dictionary. Hver dictionary (bortsett fra den på indeks 0) inneholder 2 key:value-par
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


#-------------------------
# All kode ovenfor er kun definisjoner av funksjoner og variabler og gjør ikke noe 'synlig' i seg selv
# Under kommer koden som kjøres:

# Variabelen run skal styre while-løkka. Så lenge run er True vil løkka gå om igjen og om igjen

run = True
while run:      # betyr det samme som while run == True
    # " PSEUDOKODE"
    #Skrive ut overskrift
        # Vi kaller funksjonen skriv_header(). Da utføres koden til den funksjonen, slik vi definerte den tidligere
    skriv_header()
    #Skrive ut liste over planeter
        # Vi kaller funksjonen skriv_ut_planetliste(planeter) og sender med lista vår 'planeter' som argument. Da utføres koden til den funksjonen, slik vi definerte den tidligere
    skriv_ut_planetliste(planeter)
    #Ta input med valg, og en tilbakemelding
    planetnummer = int(input("\n Velg en planet ved å skrive inn et tall: "))
    # Evt velge tilfeldig, og tilbakemelding
        # Dersom brukeren har valgt 0 for tilfeldig planet kaller vi funksjonen velg_tilfeldig() for å trekke et tall.        
    if planetnummer == 0:
        valgt_planet = velg_tilfeldig(planeter)      # Denne variabelen vil få datatypen dict, siden funksjonen vi definerte returnerer en dict fra den gitte indeksen i lista
        print(f"Du fikk planeten {valgt_planet['navn']}")
    # Ellers bruker vi tallet brukeren valgte som indeks for å finne planeten i lista vår  
    else:
        valgt_planet = planeter[planetnummer]        # Denne variabelen vil få datatypen dict, siden funksjonen vi definerte returnerer en dict fra den gitte indeksen i lista
        print(f"Du har valgt planeten {valgt_planet['navn']}")

    # Ta input med vekt, gjør den direkte om til float
    brukervekt = float(input("Hva er din vekt på jorden?: "))

    #Beregninger
    # beregner den nye veklten med funksjonen vi definerte og lagrer det i en variabel. Argumentene vi sender med er vekten som ble skrevet inn og tyngdekraften på den valgte planeten
    vekt_pa_annen_planet = beregn_vekt(brukervekt, valgt_planet['tyngdekraft'])
    
    #Tilbakemelding
    print(f"Din vekt på planeten {valgt_planet['navn']} med tyngdekraft {valgt_planet['tyngdekraft']} er {vekt_pa_annen_planet} kg")

    #Ta input om avslutning
    # run skal som nevnt styre løkka, her vil verdien til run (True/False) bli bestemt av hva som returneres fra funksjonen vår en_gang_til.
    run = en_gang_til()

