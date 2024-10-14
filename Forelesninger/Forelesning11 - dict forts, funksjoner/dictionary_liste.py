
# Lager en liste der elementene er dictionaries. Her har listen 3 elementer.
brettspill = [
    {'tittel' : 'Dixit', 'spilletid' : 30, 'aldersgrense' : 8, 'år' : 2008},
    {'tittel' : 'Pandemic', 'spilletid' : 45, 'aldersgrense' : 8, 'år' : 2008},
    {'tittel' : 'Wingspan', 'spilletid' : 40, 'aldersgrense' : 10, 'år': 2019 },
]

# Itererer gjennom listen og skriver ut noen verdier fra dictionaryene
for spill in brettspill:
    print(f"{spill['tittel']} er ment for spillere fra {spill['aldersgrense']} år og oppover.")

# Legger til et element (som er en dictionary) i listen:
brettspill.append({'tittel':'Mysterium', 'spilletid' : 42, 'aldersgrense': 10, 'år': 2015})
print(brettspill)
