
# Dette er hovedfilen vår, hvor vi skriver koden som skal kjøres

# importerer klassene Student og Course, som er definert i student.py, slik at vi kan bruke dem til å opprette objekter i denne filen.
from student import Student, Course
# importerer funksjonen vi laget i en separat fil (coursesfunction.py) slik at vi får tilgang til å bruke den i denne filen
import coursesfunction

# Oppretter et objekt av klassen Student
nils_nilsen = Student("Nils", "Nilsen", 22, "It463")

# Oppretter 3 forskjellige objekter av klassen Course
programmering1 = Course("Programmering 1", "ITF10924", 10)
webutvikling = Course("Webutvikling", "ITF67123", 10)
designetellerannet = Course("Design etc", "ITF32789", 10)

# I klassen Student laget vi en metode som het enroll_in_course. Metoden legger til et Course-objekt i Student-klassens liste med kurs studenten har tatt (courses)
# Vi legger til to kurs for denne studenten:
nils_nilsen.enroll_in_course(programmering1)
nils_nilsen.enroll_in_course(webutvikling)

# Prøver en av metodene vi laget i Student-klassen, get_total_credits, som returnerer totalt antall studiepoeng kursene i courses-listen (til Student-objektet nils_nilsen) er 'verdt'
print(nils_nilsen.get_total_credits())

# legger til et kurs til
nils_nilsen.enroll_in_course(designetellerannet)

# Skriver ut oppdatert antall studiepoeng nils_nilsen nå har. Først bruker vi metoden vi definerte i klassen Student. Merk at denne metoden kun fungerer på et objekt av Student-klassen.
print("Studiepoeng, hentet med klassemetode:")
print(nils_nilsen.get_total_credits())
print()

# Vi skriver ut den samme infoen fra nils_nilsen, denne gangen med funksjonen vi laget i egen fil (coursesfunction.py). Siden vi tidligere importerte den, får vi mulighet til å bruke den her.
print("Studiepoeng hentet med funksjon:")
print(coursesfunction.calculate_total_credits(nils_nilsen.courses))

# Funksjonen vi importerte er ikke begrenset til en spesifikk klasse, derfor kan vi bruke den også på en vanlig liste vi måtte ønske:
all_courses = [programmering1, webutvikling, designetellerannet]
print("Studiepoeng fra uavhngig liste:")
print(coursesfunction.calculate_total_credits(all_courses))

# Vil ikke fungere å bruke metoden get_total_credits() fra Student-klassen:
#print(all_courses.get_total_credits())

# For å skrive ut dokumentasjon bruker vi __doc__. Gitt at utvikleren har skrevet dokumentasjon kan vi så få den skrevet ut.
# Merk at vi må ha med 'stien' til den importerte funksjonen. Hvis vi leser det 'bakfra', ber vi her under om dokumentasjon for calculate_total_credits fra coursesfunction(.py)
# Merk også at vi her ikke har med () i funksjonsnavnet
print(coursesfunction.calculate_total_credits.__doc__)

# Eksempel med dokumentasjon for append()-metoden til lister
print(list.append.__doc__)

# Vi kan også skrive ut dokumentasjon for klasser: (her har vi ikke med 'stien', siden vi importerte denne enkeltvis fra modulen vi laget (student.py)
print(Student.__doc__)
