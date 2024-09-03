
# Starter med å opprette en variabel med navn x og setter den til verdien 5
x = 5
print(f"x = {x}")

# Variabelen overskrives med ny verdi, den nye verdien er den nåværende verdien pluss 3
x += 3  # x = x + 3
print(f"x = {x}")
x = x + 3       # Dette er den 'vanlige' måten et slikt regnestykke ville blitt skrevet på. Merk at vi her legger til 3 igjen etter at vi la til 3 på linje 7.
print(x)

# Ny verdi settes til nåværende verdi minus 3
x -= 2 # x = x - 2
print(f"x = {x}")

# Ny verdi settes til nåværende verdi ganger 2
x *= 2 # x = x * 2
print(f"x = {x}")

# Ny verdi settes til nåværende verdi delt på 3
x /= 3 # x = x/3
print(f"x = {x}")

# Ny verdi settes til nåværende verdi modulus 3. (Modulus gir oss resten, etter å ha dividert x sin verdi på 5)
x %= 5 # x = x % 5
print(f"x = {x}")

# Ny verdi settes til nåværende verdi opphøyd i 2 ('i annen')
x **= 2  # x = x ** 2
print(f"x = {x}")

# Ny verdi settes til nåværende verdi delt på 3, rundet ned til nærmeste hele tall
x //= 3 # x = x // 3
print(f"x = {x}")
