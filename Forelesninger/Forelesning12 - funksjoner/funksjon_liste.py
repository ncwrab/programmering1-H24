# Funksjon som skal skrive ut hvert element i en liste, på hver sin linje
# Legg merke til at parameternavnet er generelt og brukes kun internt i funksjonens kodeblokk
# Ved å abstrahere slik vil funksjonen fungere med hvilken som helst liste

def print_list(list_to_print):
    for element in list_to_print:
        print(element)

brettspill = ['Ubongo', 'Pandemic', 'Ludo', 'Monopol', 'Mysterium']
random_liste = [42, 1000, 3.14, 9001, 'Norge', 'Python']

print_list(brettspill)
print_list(random_liste)
