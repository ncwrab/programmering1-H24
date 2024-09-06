# Oppgaven sier at vi skal lage et lite program som gjør det mulig å regne ut vår vekt på andre planeter.
# Vi skal ta følgende som input fra brukeren:
# - Vår vekt (i kg)
# - Navnet på den andre planeten
# - Den andre planetens tyngdekraft
#
# I tillegg skal vi gjøre en del tester på hva brukeren får lov til å gi som input:
# - Vekt må være et positivt tall
# - Vekt kan ikke være over et gitt tall (Her brukes 600)
# - "Pluto" er ingen planet (Vi skal gi en advarsel, men godta det allikevel)
# - Programmet skal avsluttes med exit() dersom noen av inputene er feil/ugyldige i forhold til kravene over

# Starter med en liten velkomstmelding:
print(" Hva er din vekt på andre planeter? ")

# Brukeren skal skrive inn sin vekt:
din_vekt = input(" Hva er din vekt på jorden (i hele kg)")

# Sjekker om vekten er skrevet med tall (isnumeric() godtar bare 0-9 som input)
# Dersom det er skrevet inn med kun tall godkjennes dette, og vi omformer datatypen til int:
if din_vekt.isnumeric() == True:
    din_vekt = int(din_vekt)
    print("OK")
# Har man derimot brukt andre tegn, slik som bokstaver eller andre tegn, gor programmet en feilmelding og avsluttes
else:
    print(f" {din_vekt} er ikke en gyldig vekt")
    exit()
# If-test for å sjekke om tallet er negativt, i så fall gis en feilmelding og programmet avsluttes:
if (din_vekt <= 0) :
    print(f"Din vekt, {din_vekt} kg er ikke positiv. Prøv igjen.")
    exit()
# Sjekker med en ny betingelse (elif) om tallet er for høyt.
# Er det for høyt (her over 600) gis en feilmelding og pragrammet avsluttes:
elif din_vekt >= 600:
    print(f"{din_vekt} er enten verdensrekord, eller så lyver du.")
    exit()

# Vi er nå ferdige med tester for riktig input av vekt.
# Vi ber nå brukeren om å skrive inn planetens navn.
# Det neste vi sjekker for er riktig input av planetnavn (Pluto er ingen planet).
# Dersom planeten heter "Pluto" eller planeten heter "pluto" gis en advarsel, men brukeren får lov til å fortsette:
planetnavn = input("HVa er planetens navn?")
if planetnavn == "Pluto" or planetnavn == "pluto":
    print("Pluto er ikke en planet, men OK.")

# Til sist trenger vi input fra brukeren om planetens tyngdekraft.
# Vi omformer så tallet til desimaltall (float)
planetens_tyngdekraft = input("Hva er planetens tyngdekraft?")
planetens_tyngdekraft = float(planetens_tyngdekraft)

# Dersom tyngdekraften er 0 eller lavere gis en feilmelding, og programmet avsluttes
if planetens_tyngdekraft <= 0:
    print(f"Tyngdekraften {planetens_tyngdekraft} kan ikke være 0 eller lavere.")
    exit()

jordens_tyngdekraft = 9.807

# Utregning for å finne brukerens vekt på den oppgite planeten:
din_masse = din_vekt / jordens_tyngdekraft
din_planetvekt = din_masse * planetens_tyngdekraft
# Runder av vekten til to desimaler:
din_planetvekt = round(din_planetvekt, 2)

# Til sist skrives det ut en melding til brukeren med info om planeten og brukerens vekt på denne:
print(f"Din vekt på planeten {planetnavn}, med en tyngdekraft på {planetens_tyngdekraft} m/s2 er {din_planetvekt} kg")
