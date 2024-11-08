import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

# Lager en klasse, Hovedvindu, som skal arve fra klassen QWidget.
# Denne klassen er tenkt å inneholde all kode for å lage GUI som skal vises for vinduet vårt.
class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Test av knappbinding')         # Gir vinduet en tittel
        self.setGeometry(100, 100, 300, 100)                # Gir vinduet en selvdefinert størrelse

        layout = QVBoxLayout()                              # Oppretter et layout av klassen QVBoxLayout
        self.setLayout(layout)                              # Sier at denne klassen (Hovedvindu) skal bruke nevnte layout

        knapp = QPushButton()                               # # Oppretter en knapp med klassen QPushButton
        knapp.setText('Min knapp')                          # Gir knappen teksten 'Min knapp'
        knapp.clicked.connect(self.knapp_trykket)           # Kobler hendelsen clicked (knappen blir trykket på) til funksjonen 'knapp_trykket'
        layout.addWidget(knapp)                             # Legger til knappen i layoutet

        self.show()                                         # Her har vi lagt show() i klassen. Siden denne ligger i __init__-metoden vil den bli utført når vi oppretter et objekt av Hovedvindu

# Definerer funksjonen/metoden knapp_trykket
    # Denne funksjonen skal kjøres hver gang knappen vår blir trykket på
    # Den inneholder kun en print, og vil derfor skrive ut hver gang knappen trykkes
    def knapp_trykket(self):
        print('Knappen ble trykket!')


if __name__ == '__main__':                  # Sjekker om det er denne filen vi starter/kjører. I så tilfelle kjøres koden under.
    app = QApplication(sys.argv)            # Må alltid med
    vindu = Hovedvindu()                    # Oppretter et objekt av Hovedvindu()-klassen
    sys.exit(app.exec())                    # Må alltid med
