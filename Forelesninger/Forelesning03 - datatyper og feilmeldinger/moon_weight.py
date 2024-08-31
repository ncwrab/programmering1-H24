# Et lite program som skal regne ut hva en brukers vekt vil være på månen.
# Brukeren skal kunne skrive inn sin vekt, og få tilbake hva vekten er på månen.

# Når programmet kjøres spørres brukeren om å skrive inn sin vekt
# Legg merke til at input() alltid vil tolke det brukeren skriver som en string (tekst)
my_earth_weight = input("Hva er din vekt på jorden?")

# For at verdien hentet med input() skal tolkes som et tall, må vi konvertere fra tekst til enten int eller float.
# Dette forutsetter imidlertid at tekst-verdien vi forsøker å konverte er samsvarig med disse datatypene
# (altså, det kan ikke være bokstaver i en tekst som skal konverteres til tall).
# Å konvertere til float er stort sett det sikreste, ettersom alle tall i tekstformat kan konverteres til float og
# det er alltid en mulighet for at brukeren ønsker å benytte float, noe int-konvertering ikke støtter.
my_earth_weight = float(my_earth_weight)


# Variabler for tyngdekraft på jorden og månen
earth_gravity = 9.807       # Hvilken datatype har disse to variablenes data?
moon_gravity = 1.622

# Formel for å beregne vekten på månen ut fra vekten på jorden.
# Her brukes verdiene som er lagret i variablene våre til å beregne vekten på månen
moon_weight = my_earth_weight / earth_gravity * moon_gravity

# Skriver ut resultatet (brukers vekt på månen)

print(f"Din vekt på månen er {moon_weight} kg.")
