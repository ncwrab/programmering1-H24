
print("Skriver ut tallene fra 0 til 10:")
for tall in range(11):
    print(tall)

print("Skriver ut tallene fra og med 1 til og med 9:")
for tall in range(1,10):
    print(tall)

print("Skriver ut tallene fra og med 1000 til og med 9001:")
for tall in range(1000, 9002):
    print(tall)

print("Skriver ut tall fra og med 1000 til og med 9000, med intervall på 1000. Legger dem i en liste:")

nummere = []
for tall in range(1000, 9902, 1000):
    print(tall)
    nummere.append(tall)

print("tallene i den nye lista:")
for tall in nummere:
    print(tall)

print(f"Minste tall i lista:")
print(min(nummere))

print(f"Største tall i lista: {max(nummere)}")

print("Summen av verdiene i lista:")
print(sum(nummere))
