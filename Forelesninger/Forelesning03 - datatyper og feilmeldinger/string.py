# Printer en string. Vi bruker her " "
print("A string")

# Også en string. Her bruker vi ' '
print('Also a string')

# Hvis vi ønsker å inkludere " eller ' i teksten har vi følgende valg:

# String med " som en del av den
print('We can put quotes inside a string: "First, solve the problem. Then, write the code." ')

# String med ' som en del av den
print("With apostrophe: It's harder to read code than to write it. - Joel Spolsky")

# String med både " og ' som en del av den
print('''Why not both?: "It's harder to read code than to write it." - Joel Spolsky''')

# Oppretter to variabler. Hvilken datatype er innholdet?
quote = "It's harder to read code than to write it."
author = "Joel Spolsky"

print(author)

# Her ønsker vi å bruke de to variablene over som en del av teksten vi printer ut
# Vi har flere måter å få til dette på
# 1) , gjør at dataen til hver variabel printes "hver for seg"
print('A quote: "', quote, '" - ', author )

# 2) + gjør at vi kombinerer alle string-verdiene (concatenate) og lager en hel string før den printes
# Dette fungerer bare når vi har string-verdier, ikke med f.eks. int
print('A quote: "' + quote, '" - ' + author)

# 3) Bruker den innebygde print-format til å lage en streng med verdiene fra variablene
# Legg merke til at vi her må ha en f helt i starten i parentesen
# Denne metoden kan også håndtere variabler med andre datatyper enn string.
print(f'A quote: "{quote}" - {author}')
