# Lager en klasse, Student. __init__-metoden (funksjonen) må alltid være med i hver klasse vi lager. 
# __init__ kjøres automatisk når vi oppretter et objekt av klassen.
# Første parameter skal alltid være self.
# Etter self, velger vi å ta med 4 parametere, som må fylles inn når vi bruker klassen. 
# Disse 4 parameterne lagres så som variabler/attributter i klassen. Legg merke til at vi må ha med self foran hvert variabelnavn.
# Variabelen courses gjør vi ikke noe med foreløpig, utover å si at det skal være en liste.
class Student:
    def __init__(self, first_name, last_name, age, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.courses = []

    # Vi lager en metode (funksjon som tilhører en klasse) for å returnere fornavn og etternavn tilhørende et objekt av Student-klassen
    # Denne metoden (funksjonen) kan kun brukes på Student-objekter
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

# Instansierer to objekter av Student-klassen. De 4 parameterne vi laget selv må fylles ut ved opprettelsen.
nils_nilsen = Student("Nils", "Nilsen", 22, "IT345")
anne_annesen = Student("Anne", "Annesen", 23, "IT678")

# Skriver ut litt informasjon fra de to forskjellige objektene.
print(f"{nils_nilsen.first_name} {nils_nilsen.last_name} er {nils_nilsen.age} år.")
print(f"{anne_annesen.first_name} {anne_annesen.last_name} er {anne_annesen.age} år.")
# Prøver metoden vi definerte for Student-klassen og ser at den fungerer som forventet.
print(nils_nilsen.get_full_name())
print(anne_annesen.get_full_name())

# To be continued..
