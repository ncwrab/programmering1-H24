
# Vi putter kode som kan feile (kode vi ikke har 100% kontroll på) i try-delen:
# Her vil variablene tall1 og tall2 settes til input fra brukeren. Disse kan feile fordi vi ikke har kontroll på hva brukeren gir som input.
# Vi forventer et tall, men dersom brukeren skriver inn en bokstav vil koden vår feile, og derfor legger vi det i try-blokken.
# 'svar' kan feile dersom brukeren skriver inn 0 som tall2. Da vil koden vår forsøke å dele på 0, som ikke er mulig.
# Vi legger derfor også dette i try-blokken.
try:
    tall1 = int(input("Skriv inn et tall:"))
    tall2 = int(input("Skriv inn et tall til:"))
    svar = tall1 / tall2

# Feilmeldingen vi får dersom brukeren prøver å skrive inn f.eks en bokstav er ValueError.
# Vi forutser at dette KAN skje, og lager derfor en except-del som håndterer tilfellene der dette forekommer:
except ValueError:
    print("Du skrev inn en ugyldig verdi")

# Feilmeldingen vi får dersom brukeren prøver å skrive inn 0 som tall2 er ZeroDivisionError.
# Vi forutser at dette KAN skje, og lager derfor en except-del som håndterer tilfellene der dette forekommer:
except ZeroDivisionError:
    print("Du kan ikke dele på 0!")

# Kode som i utgangspunktet ikke kan feile legger vi i en else-del:
else:
    print(svar)
