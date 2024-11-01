# Vårt første GUI

# Vi trenger å importere et par klasser
from PyQt6.QtWidgets import QApplication, QWidget
import sys

# Vi må alltid ha med et QApplication-objekt når vi lager et GUI. Gir det navnet app. sys.argv lar oss sende med parametere dersom vi bruker kommandolinjen.
# (Dersom vi vet at vi aldri kommer til å starte via kommandolinjen kan vi istedenfor sys.argv sende med [] (en tom liste) )
app = QApplication(sys.argv)    # må alltid med

# Vi lager et vindu. Vinduet lager vi her som et QWidget-objekt
vindu = QWidget()

# Klassen QWidget har en rekke metoder, her bruker vi metoden setWindowTitle() til å gi vinduet en tittel
vindu.setWindowTitle('Hello world!')
# Vi bestemmer størrelsen vinduet skal ha når det vises (vi kan derimot 'dra i hjørnene' og endre størrelsen når vi kjører koden)
vindu.resize(300, 100)
# Flytter vinduet til en ny startposisjonskoordinater. 
# Merk at første verdi, 700, er avstand i piksler fra venstre side av skjermen. Andre verdi er avstand fra toppen av skjermen.
vindu.move(700, 300)

# For å vise vinduet må vi kalle show(), ellers vil det ikke vises når vi kjører koden
vindu.show()

# Egentlig vises ikke appen vår før følgende linje blir kjørt. Det er app.exec() som sørger for dette, og må derfor alltid være med når vi lager GUI. sys.exit() sørger for at appen vår "leker fint" med maskinen vår dersom vi kjører den fra kommandolinjen
sys.exit(app.exec())    # må alltid med
