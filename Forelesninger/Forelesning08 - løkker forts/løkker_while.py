
# while-løkke som teller ned fra 10 og skriver ut hvert tall. Løkka vil gå så lenge teller er større enn 0.
teller = 10
while teller > 0:
    print(teller)
    teller -= 1

# teller er nå 0. Ny while-løkke som denne gangen teller opp til 10 og skriver ut hvert tall
while teller < 11:
    print(teller)
    teller +=1

# teller er nå 11
print(teller)

# Oppretter en liste og ved hjelp av en for-løkke fylles den med 7 tall (0,1,2,3,4,5,6)
liste_med_tall = []
for tall in range(7):
    liste_med_tall.append(tall)
    print(liste_med_tall)
# Istedenfor å bruke en løkke kunne vi gjort det samme på denne måten:
#liste2 = list(range(7))

print() # For å få en tom linje i utskriften

# while-løkke som skal gå så lenge tallet 3 fins i lista, og som for hver iterasjon skal fjerne det bakerste elementet (pop)
while 3 in liste_med_tall:
    liste_med_tall.pop()
    print(liste_med_tall)

print()

# Vi ønsker at en bruker skal kunne styre hvor lenge løkka skal gå. Løkka vil gå så lenge kjør == True
# Ved å ta input fra bruker for hver iterasjon kan kjør endres til False basert på hva brukeren skriver inn
# Løkken(e) i seg selv skriver bare ut "test" og 2 tall for hver iterasjon
# Brukeren kan altså styre hvor mange ganger dette skal skrives ut.
kjør = True
while kjør:
    print("test")
    for nummer in range(2):
        print(nummer)
    en_gang_til = input("Skrive ut en gang til? Y/N")
    kjør = en_gang_til.upper() == 'Y' # kjør settes til enten True eller False avhengig av hva høyre side av = evalueres til.
