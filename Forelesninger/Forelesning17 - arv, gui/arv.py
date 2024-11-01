
# Definerer en klasse kalt Animal.
# Klassen har 2 attributter/lokale variabler som må spesifiseres gjennom parameterne når vi oppretter et objekt av klassen
# Vi forutsetter at alle dyr har et egennavn (litt kunstnerisk frihet, for det er jo ikke egentlig slik) og en alder
# navn og alder lagres i lokale variabler av __init__()-funksjonen
# Vi lager også en metode (funksjon tilhørende en klasse), get_name(). Denne skal returnere navnet når vi kaller den.
class Animal:
    def __init__(self, name, age):
        self.navn = name
        self.alder = age

    def get_name(self):
        return self.navn


# Definerer en ny klasse, Honeybadger (honninggrevling). Siden en honninggrevling er et dyr må den ha et navn og en alder. 
# Istedenfor å opprette egne attributter for navn og alder i denne klassen lar vi den derfor arve disse fra klassen Animal.
#   class Honeybadger(Animal) betyr at den nye klassen vår Honeybadger skal arve fra Animal. 
# I Honeybadgers __init__-metode tar vi også med en tredje parameter, sgiven, og gir denne en standardverdi på 0
# name og age lar vi __init__-metoden vi arvet fra Animal håndtere
#   Det gjør vi ved å kalle super().__init(name, age). Merk at ikke self ikke skal være med som parameter her!
#   super() titter på klassen 'utenfor' Honeybadger, altså den nedarvede klassen Animal i dette tilfellet
class Honeybadger(Animal):
    def __init__(self, name, age, sgiven=0):
        super().__init__(name,age)
        self.sgiven = sgiven


# Oppretter et objekt av Honeybadger-klassen, kaller dette for dyr1. Siden sgiven har en standardverdi er det ikke nødvendig å sende med en verdi for denne (men vi kan om vi vil)
dyr1 = Honeybadger("Nils-Christian", 3, )

# Prøver å bruke metoden vi arvet fra Animal på dyr1 (som altså er et Honeybadger-objekt)
print(dyr1.get_name())
# Vi kan også hente verdier direkte fra objektet dyr1
print(dyr1.sgiven)

#print(type(dyr1))
