
# Oppretter en tuppel med 3 elementer. Legg merke til at vi bruker () når vi oppretter en tuppel
beste_brettspill2024 = ("Hitster", "Sushi Go Party", "Flamme Rouge BMX")

# Vi kan skrive ut elementer fra tuppelen på 'vanlig' måte
print(beste_brettspill_2024[1])

# Vi kan iterere gjennom elementene i tuppelen på 'vanlig' måte
for spill in beste_brettspill_2024:
    print(spill)

# Operasjonene under er ulovlige for en tuppel (kan ikke legge til, fjerne eller endre i en tuppel)
# ta bort # på en linje av gangen for å teste selv

#beste_brettspill_2024[3] = "Monopol"
#beste_brettspill_2024.append("Monopol")
#beste_brettspill_2024.pop()

# Vi kan kopiere fra en tuppel til ny variabel. Siden vi kopierer inn en string, vil spill2 være av datatypen string
spill2 = beste_brettspill_2024[1]
print(spill2)

# .append() er ikke lov på en string. Fjern # for å teste.
#spill2.append("Monopol")

# .pop() er ikke lov på en string. Fjern # for å teste.
#spill2.pop()
