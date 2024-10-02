brettspill = {
    'tittel' : 'Dixit',
    'spilletid' : 30,
    'aldersgrense' : 8,
}

# Itererer gjennom og skriver ut nøklene/keys i dictionaryen med en for-løkke. Hvis vi ikke spesifiserer noe vil vi få ut nøklene.
for key in brettspill:
    print(f"{key} ")

# Løkken under gir samme resultat som løkken over, men her har vi spesifisert (med .keys()) at det er nøklene vi er ute etter. Dette kan være lurt å gjøre for å unngå misforståelser.
for key in brettspill.keys():
    print(key)

# Itererer gjennom og skriver ut verdiene/values i dictionaryen med en for-løkke. Vi må spesifisere med .values().
for value in brettspill.values():
    print(value)

# Itererer gjennom og skriver ut både nøkkel/key OG verdi/value som fins i dictionaryen med en for-løkke. Vi bruker .items() til dette.
# Merk at vi her bruker TO hjelpevariabler (key, value) som holder på key og value hver for seg
for key, value in brettspill.items():
    print(f"{key} - {value}")
