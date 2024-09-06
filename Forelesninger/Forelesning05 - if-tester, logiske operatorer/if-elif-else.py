

# Eksempel på hvordan vi også kan evaluere om noe er True i variabler
# Innholdet i variabelen er_x_større_enn_y vil bli av datatypen bool (True eller False)
# Det vanligste er dog allikevel å definere betingelsene direkte i en if-test
# Felles er at betingelsen i if-testen sjekkes, dersom den blir True vil else-delen hoppes over
#
x = 3
y = 300
er_x_større_enn_y = y < x

# Vi kan så bruke variabelens innhold i en if-test:
if er_x_større_enn_y == True:
    print(f"\n{y} er mindre enn {x}")
else :
    print(f"{y} er ikke mindre enn {x}")

# Eksempel med elif og else. Merk at disse IKKE er uavhengige. 
# Det innebærer at kun én av kodeblokkene vil bli kjørt, avhengig av hva betingelsene evalueres til
# Betingelsene vil bli testet sekvensielt helt til en blir evaluert til True, de resterende vil bli hoppet over.

number = -10

if number > 0:
    print(f"{number} er et positivt tall")
elif number < 0:
    print(f"{number} er et negativt tall")
elif number < 0:
    print(f"{number} er et negativt tall")
else:
    print(f"{number} er 0")


# Det er vanlig å definere betingelser ved å benytte variabler, heller enn å definere verdier direkte
# Her lagres verdiene i to variabler 
navn = "nils-Christian"
navn2 = "Nils-CHRIstian"

# som så sjekkes for likhet. Ved å bruke den innebygde funksjonen lower() vil innholdet i begge variablene 
# (som inneholder data av typen string) bli omgjort til små bokstaver før de sjekkes for likhet.
# Prøv å fjerne .lower() fra betingelsen og se hva evalueringen av if-testen blir da.

if navn.lower() == navn2.lower():
    print(" Navnene er like")
else:
    print("Navnene er IKKE like")
    
print(navn2.lower())
