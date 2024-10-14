import random


# skjelett av en funksjon

def funksjon(): #(def <navn på funksjon>():
    # logikk
    return #verdi

# For å bruke/kjøre funksjonen sier vi at vi kaller på funksjonen. Det gjør vi slik (siden den ikke utfører noe,
funksjon()

# En funksjon som skal skrive ut hei, med litt pynt over og under
def skriv_hei():
    print("--------")
    print("--Hei---")
    print("--------")
    return

# Hver gang vi kaller funksjonen vil den utføre koden/logikken sin. Her kaller vi på funksjonen 3 ganger på rad:
skriv_hei()
skriv_hei()
skriv_hei()

# funksjon med to parametere (tall_en og tall_to)
# funksjonen skal returnere et tilfeldig tall mellom tall_en og tall_to hver gang vi kaller funksjonen
def gi_tilfeldig_tall(tall_en, tall_to):
    tilfeldig_tall = random.randrange(tall_en, tall_to)
    return tilfeldig_tall
    #print(tilfeldig_tall)


# Når vi kaller en funksjon som har parametere må vi 'sende dem med' hver gang vi kaller den
# Når vi 'sender med' verdier slik, kalles de argumenter
print(gi_tilfeldig_tall(100, 1000))

# Vi kan bruke funksjoner for å sette verdien til en variabel
# Her vil variabelen 'tallet' bli satt til verdien som funksjonen returnerer
tallet = gi_tilfeldig_tall(10, 1300)
print("variabelen 'tallet's verdi:")
print(tallet)
