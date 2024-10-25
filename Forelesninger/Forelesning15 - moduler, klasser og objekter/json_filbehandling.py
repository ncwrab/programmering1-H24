
# Dette er 'programmet' vårt. Vi importerer modulen vi laget, jsonmodul.py, og bruker funksjonene vi definerte der.

import jsonmodul


# Lager en dictionary, som vi ønsker å skrive til en json-fil senere
planet = {"navn" : "Merkur", "tyngdekraft" : 3.73}

# Lagrer filnavnet vi ønsker å bruke i en variabel
file_name = "planet.json"

# Bruker skriv_json()-funksjonen vi definerte i vår jsonmodul, og sender med variablene vi akkurat opprettt som argumenter
# Vi får nå opprettet en ny fil med navnet planet.json, og som inneholder en string med vår dictionary 
jsonmodul.skriv_json(planet, file_name)

# Bruker les_json()-funksjonen vi definerte i vår jsonmodul. Variabelen her, dictionary_from_file settes til innholdet av filen (som ble returnert av funksjonen vår).
dictionary_from_file = jsonmodul.les_json(file_name)

# Skriver ut innholdet i variabelen får å se at innholdet er som forventet
print(dictionary_from_file)
print(type(dictionary_from_file))
# Variabelen er nå datatype dictionary, og vi kan bruke den som det, f.eks ved å hente ut enkeltverdier ved å skrive inn nøkkelen/key.
print(dictionary_from_file["navn"])
