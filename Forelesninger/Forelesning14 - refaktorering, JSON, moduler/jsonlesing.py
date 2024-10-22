# For å få tilgang til ferdiglagde json-funksjonalitet må vi importere modulen/biblioteket 'json'

import json

# Vi lager dictionary-er (i en liste).
planeter = [{'name': "Merkur", 'tyngdekraft' : 3.7},
            {'name': 'Venus', 'tyngdekraft': 8.87},
            {'name': 'Jorden', 'tyngdekraft': 9.807}
]

# Åpner en fil 'planeter.json' og spesifiserer at vi vil skrive til den med "w".
# ved å benytte dump() kan vi skrive vår dictionary til json-filen
# 'indent=4' er ikke nødvendig å ha med, men dette vil formatere teksten i fila slik at den (muligens) blir mer lesbar for oss.
with open("planeter.json", "w") as utfil:
    json.dump(planeter, utfil, indent=4)

# Åpner filen 'planeter.json' og spesifiserer at vi vil lese fra den med "r".
# Innholdet fra fila lagres i en variabel med load(), så skrives variabelens innhold ut
with open("planeter.json", "r") as fil:
    planeter_fra_fil = json.load(fil)
    print(planeter_fra_fil)

# Oppretter en json-string med noen key:value-par. 
# Legg merke til at json er en string som ser ut som en dictionary.
json_string = '{"dyr":"Hund", "navn": "Fido", "alder":10}'

# Skriver ut innholdet av variabelen, og datatypen
print(json_string)
print(type(json_string))  # datatypen er her str

# For at innholdet skal kunne behandles som en dictionary av python må vi lese inn stringen med loads() (mer at vi har med en s for string)
# Variabelen hund vil nå være en dictionary
# Videre kan vi så hente ut verdier fra dictionaryen på vanlig måte.
hund = json.loads(json_string)
print(hund)
print(type(hund))        # datatypen er nå dict

print(f'Hunden {hund["navn"]} er {hund["alder"]} år gammel.')
