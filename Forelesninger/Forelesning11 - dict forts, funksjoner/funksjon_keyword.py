
# Vi definerer en funksjon
# Den har to parametere, karakternavn og spill
# Den skal så skrive ut en kort tekst basert på disse
# Her har vi gitt spill en standardverdi (spill=Super Mario Bros)
# Her vil det si at dersom vi kun sender med ett argument, vil det bli lagret som karakternavn, mens spill vil få standardverdien vi har spesifisert

def skriv_ut_spillkarakter(karakternavn, spill="Super Mario Bros"):
    print(f"{karakternavn} er en karakter i spillet {spill}")

# Vi sender med to argumenter:
skriv_ut_spillkarakter("Mario", "Super Mario Bros")
# Se hva som skjer når vi sender med argumentene i 'feil' rekkefølge
skriv_ut_spillkarakter("Super Mario Bros", "Mario")

# Vi ser at det også vil fungere å kun sende med ett argument
skriv_ut_spillkarakter("Mario")
# Vi bruker keywords (spill= og karakternavn= ), merk at når vi gjør dette er ikke rekkefølgen viktig, og vi overstyrer også standardverdien
skriv_ut_spillkarakter(spill="The legend of Zelda", karakternavn="Link")

# Hva skjer når vi ikke sender med argumenter, selv om funksjonen krever det
skriv_ut_spillkarakter() # (Vi får feilmelding)
