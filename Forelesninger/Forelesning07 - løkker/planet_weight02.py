
# Oppretter to lister. Den første med noen planetnavn, den andre med disse planetenes tyngdekraft
# Merk at listene har like mange elementer, og at f.eks indeksnummer 0 tilsvarer Merkur i den ene og Merkurs tyngdekraft i den andre.

planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

# Skriver ut en liste over planetene som blir presentert til brukeren
print("---- Planeter -----")
print("1 - Merkur")
print("2 - Venus")
print("3 - Jorden")
print("4 - Mars")
print("5 - Jupiter")
print("6 - Saturn")
print("7 - Uranus")
print("8 - Neptun")

# Ber brukeren om å velge en planet fra lista og gjør samtidig om til heltall (int)
planetnummer = int(input(" Velg et planetnummer: "))

# Dersom brukeren skriver inn et tall som ikke fins i lista skal det komme en feilmelding og programmet avsluttes:
if (planetnummer <= 0 or planetnummer > len(planeter)):
    print("Nummeret er ikke gyldig")
    exit()

# Trekker fra 1 fra nummeret brukeren skrev inn (fordi indeksene i en liste alltid begynner på 0)
# Denne verdien skal vi bruke senere for å finne tyngdekraften på valgt planet.
planetnummer = planetnummer - 1

print(f"Du valgte {planeter[planetnummer]}")

# Ber brukeren skrive inn sin vekt. Her gjøres vekten om til heltall i en separat operasjon på linjen under.
din_vekt = input("Hva er din vekt på Jorden (i kg)")
din_vekt = int(din_vekt)

# Beregninger for å regne ut vekten på valgt planet. Merk at tyngdekraft[2] er inneholder jordens tyngdekraft.
din_masse = din_vekt / tyngdekraft[2]
vekt_paa_planet = din_masse * tyngdekraft[planetnummer]

# Skriver ut brukerens vekt på den valgte planeten.
print(f"Din vekt på {planeter[planetnummer]} er {round(vekt_paa_planet, 2)} kg")
