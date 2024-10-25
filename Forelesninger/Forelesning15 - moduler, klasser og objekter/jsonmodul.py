# importerer modulen json, slik at vi får tilgang på funksjoner derfra.
import json


# Definerer en funksjon for å skrive til en json-fil fra en dictionary
# parameterne skal være dictionaryen vi vil skrive til fil, samt filnavnet vi ønsker

def skriv_json(dictionary, filnavn):
    try:
        with open(filnavn, "w") as fil:
            json.dump(dictionary, fil, indent=4)
    except FileNotFoundError:
        print("Fant ikke filen.")

# Definerer en funksjon for å lese fra en json-fil og returnere innholdet (for bruk senere)
# Siden vi behandler filer, så tar vi med et par feil som kan oppstå og håndterer dem i funksjonen
def les_json(filnavn):
    try:
        with open(filnavn) as fil:
            dict_fra_fil = json.load(fil)
    except FileNotFoundError:
        print("Fant ikke filen.")
    except json.decoder.JSONDecodeError:
        print("Filen inneholder ikke JSON.")
    else:
        return dict_fra_fil
