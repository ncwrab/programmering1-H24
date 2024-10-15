import random

brettspill = ['Ubongo', 'Pandemic', 'Ludo', 'Monopol', 'Mysterium']

# Funksjonen skal velge et tilfeldig spill fra en liste og returnere navnet på spillet
def velg_tilfeldig_brettspill(spilliste):                # Som parameter skal funksjonen ta en liste
    indexnummer = random.randrange(len(spilliste))       # Finner et tilfeldig tall mellom 0 og en mindre enn antall elementer i lista
    return spilliste.pop(indexnummer)                    # Innholdet på den tilfeldige indexen returneres og slettes (pop) fra lista

valgt_brettspill = velg_tilfeldig_brettspill(brettspill)

print(f"Du valgte {valgt_brettspill}")
print(brettspill)
# Siden vi sendte med den originale lista (brettspill) til funksjonen og slettet et element vil lista nå ha ett element mindre etter å ha kalt funksjonen 1 gang. For hver gang funksjonen kalles vil ett element fra lista slettes.
# Dersom vi ikke ønsker at elementar skal slettes kunne vi heller sendt med en kopi av lista [:] slik:
# valgt_brettspill = velg_tilfeldig_brettspill(brettspill[:])    # En kopi ssendes med som argument

print(brettspill)
