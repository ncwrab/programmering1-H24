
number = 0

# OBS. Merk at indenteringen/innrykk er helt nødvendig å ha med i if-tester.
# Innrykket viser at en kodeblokk 'tilhører' if-testen. 
# Legg også merke til at vi må ha med : etter betingelsen.

# De tre if-testene under er uavhengige, og alle vil bli kjørt hver for seg, uansett utfall av de andre if-testene.

# Sjekker om tallet er positivt (større enn 0)
if (number > 0):
    print(f"{number} er et positivt tall")

# Sjekker om tallet er negativt (mindre enn 0)
if (number < 0):
    print(f"{number} er et negativt tall")

# Sjekker om tallet er nøyaktig 0
if (number == 0):
    print(f"{number} er 0")

# Vi kan også sjekke for likhet i strings. Under vil betingelsen evalueres til False og ingenting vil bli skrevet ut.
# Betingelsen blir False fordi høyre side har stor forbokstav og dermed ikke er lik venstre side.
if ("text" == "Text"):
    print("venstre side er lik høyre side")
    

# Eksempel på at vi også kan sjekke om innholdet i en variabel evalueres til True, og i så tilfelle kjøre kode.
dolphins_sleep_with_their_eyes_open = True

if dolphins_sleep_with_their_eyes_open == True :
    print(f"\n Delfiner sover med \n ett øye åpent")
