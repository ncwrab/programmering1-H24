
# lager en liste
brettspill = ["Ubongo", "Pandemic", "Ticket to ride", "Monopol", "Mysterium", "Pandemic Legacy: Season 0",
              "Pandemic Legacy: Season 1", "Pandemic Legacy: Season 2", "Ludo"]
# skriver ut listeelementene fra og med index 4 til 7 (7 blir altså ikke skrevet ut)
print(brettspill[4:7])

# skriver ut elementer fra index -3 til enden på lista
for spill in brettspill[-3:]:
    print(spill)

# sorterer lista
brettspill.sort()
print(brettspill)

# skriver ut de tre første spillene i (den nå alfabetisk sorterte) lista
første_spill = brettspill[:3]
print(første_spill)

# skriver ut annenhvert spill i lista
print(brettspill[::2])

# lager en variabel som skal inneholde teksten fra element -3 i lista
tekst = brettspill[-3]
print(tekst)

# viser at slicing også fungerer på en tekst (string)
print(f"\n {tekst[7:13]}")

# skriver ut index -1 fra stringen (siste tegn i stringen)
print(tekst[-1])

# slicer og skriver ut tegn i stringen fra og med index -8 til enden på stringen
print(tekst[-8:])
