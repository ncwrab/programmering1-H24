
# Å skrive til fil har en lignende framgangsmåte som å lese fra en fil.
# Legg merke til at når vi ønsker å skrive til en fil må vi spesifisere det ved å legge til "w" eller "a" når vi åpner filen.
# "w" står for write, og om vi bruker denne vil alt innholdet i filen bli overskrevet hver gang vi åpner og skriver til den.
# "a" står for append, og om vi bruker denne tekst vi skriver til filen bli lagt til bakerst i fila (slik som det fungerer med f.eks lister.
# Tidligere innskrevet innhold vil altså beholdes, i tillegg til det nye innholdet vi skriver inn.
# Løkken sørger for at vi kan skrive inn linje for linje i fila, helt til vi skriver 'q', som vil avbryte løkka.

with open("testmappe/tekstfil.txt", "a") as fil:
    while True:
        brukerinput = input(": ")

        if brukerinput == "q":
            break

        fil.write(brukerinput + "\n")
