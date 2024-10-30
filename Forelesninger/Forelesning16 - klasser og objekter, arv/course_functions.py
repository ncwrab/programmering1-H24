# I denne filen har vi med kun en funksjonsdefinisjon.
# Denne skal vi importere som en modul til hovedfilen vår (studentreg.py)


def calculate_total_credits(kurs):
    """
    Funksjonen skal regne ut antall studiepoeng fra en hvilken som helst liste med Course-objekter.
    :param kurs: En liste med objekter av typen Course (list).
    :return: Antall studiepoeng totalt for kursene i listen (int).
    """
    total_credits = 0
    for element in kurs:
        total_credits += element.credits
    return total_credits
