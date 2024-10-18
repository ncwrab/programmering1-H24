
# Vi åpner filen zen_of_python.txt og kaller dette for 'fil' (vi kan velge dette navnet selv).
# For å lese innholdet og behandle det bruker vi så den innebygde funksjonen .read() og lagrer det i variabelen 'innhold'.
# Deretter skriver vi ut innholdet, og vi skriver ut hvilken datatype variabelen 'innhold' er ved hjelp av type().
# Ved å bruke denne metoden med with ... as slipper vi å tenke på å lukke filen etter at vi er ferdig med å behandle den.
with open("zen_of_python.txt") as fil:
    innhold = fil.read()
    print(innhold)
    print(type(innhold))

# Vi åpner filen zen_of_python.txt og kaller dette nå for 'ny_fil' (siden vi selv kan velge hva vi vil navngi det).
# Ved å nå bruke readlines() vil variabelen vår 'linjeliste' bli en liste der hver linje fra filen blir elementene i denne listen.
# Vi skriver den ut, og skriver ut datatypen til 'linjeliste'.
with open("zen_of_python.txt") as ny_fil:
    linjeliste = ny_fil.readlines()
    print(linjeliste)
    print(type(linjeliste))

# Vi kan også bruke variabler for å åpne filer. Her lagrer vi filnavnet i en variabel..
filnavn = "zen_of_python.txt"

# .. og bruker så variabelen for å åpne filen:
with open(filnavn) as fil:
    # Vi kan skrive ut en linje av gangen ved å bruke readline()
    print(f"\n{fil.readline()} - første linje")
    print(f"\n{fil.readline()} - andre linje")
    print(f"\n{fil.readline()} - tredje linje")

# Vi bør bruke en try-except-blokk når vi åpner filer, for å unngå feilmeldinger som at filen ikke finnes
# Her lagrer vi filnavnet i en ny variabel (med vilje et navn på en fil som ikke eksisterer)
filnavn2 = "zen_of_python6.txt"

# Vi åpner så filen i en try-blokk. Dersom filen ikke eksisterer fra før vil vi få feilmeldingen FileNotFoundError.
# Vi forutser at dette KAN skje, og lager derfor en except-del som håndterer tilfellene der dette forekommer:
try:
    with open(filnavn2) as fil:
        print(fil.read())
except FileNotFoundError:
    print("Filen finnes ikke")
