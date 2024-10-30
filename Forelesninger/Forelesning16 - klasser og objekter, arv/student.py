# Denne filen skal brukes som en modul vi kan importere til hovedfilen vår (studentreg.py)
# I denne filen er det ingen kode som kjører direkte, kun definisjon av to klasser, Student og Course.

# Lager en klasse, Student. __init__-metoden (funksjonen) må alltid være med i hver klasse vi lager.
# __init__ kjøres automatisk når vi oppretter et objekt av klassen.
# Første parameter skal alltid være self.
# Etter self, velger vi å ta med 4 parametere, som må fylles inn når vi bruker klassen. 
# Disse 4 parameterne lagres så som variabler/attributter i klassen. Legg merke til at vi må ha med self foran hvert variabelnavn.
# Variabelen courses gjør vi ikke noe med foreløpig, utover å si at det skal være en liste.

# Her er det i tillegg laget dokumentasjon for noen funksjoner. Når vi dokumenterer en funksjon/metode eller en klasse bruker vi """ <dokumentasjon> """ (tre dobbelfnutter før og etter)
# All dokumentasjon som finnes innenfor """ """ kan vi senere skrive ut i programkoden vår
# Merk at dokumentasjonen MÅ komme først i deinisjonene våre, altså rett etter aller første linje.
# I dokumentasjonen tar vi med kort beskrivelse av tenkt virkemåte.
# I tilfeller der funksjoner/metoder har parametere og/eller en returverdi beskriver vi disse i dokumentasjonen.
# Å ha med hvilke datatyper som forventes eller returneres er veldig relevant i dokumentasjonen.
class Student:
    """
    Klassen student
    """
    def __init__(self, first_name, last_name, age, student_id):
        """
        INIT, kjøres automatisk ved opprettelse av et objekt av denne klassen
        :param first_name: Studentens fornavn (str)
        :param last_name: Studentens etternavn (str)
        :param age: Studentens alder (int)
        :param student_id: Studentens studentnummer (str)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.courses = []
    # Vi lager en metode (funksjon som tilhører en klasse) for å returnere fornavn og etternavn til et objekt av Student-klassen
    # Denne metoden (funksjonen) kan kun brukes på Student-objekter
    def get_full_name(self):
        """
        Få tak i det fulle navnet til studenten
        :return: Fornavn etternavn (str)
        """
        return self.first_name + " " + self.last_name

    def get_total_credits(self):
        total_credits = 0
        for course in self.courses:
            total_credits += course.credits
        return total_credits

    def enroll_in_course(self, course):
        self.courses.append(course)


# Lager en klasse, Course. Også her må __init__ være med. Første parameter er igjen self, så kommer de parameterne vi legger til selv.
class Course:
    def __init__(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits
