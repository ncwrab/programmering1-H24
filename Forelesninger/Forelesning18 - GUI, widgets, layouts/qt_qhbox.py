import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

# Lager en klasse, Hovedvindu, som skal arve fra klassen QWidget.
# Denne klassen er tenkt å inneholde all kode for å lage GUI som skal vises for vinduet vårt.
class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QHBoxLayout-test')     # Gir vinduet en tittel
        #self.setGeometry(200, 50, 120, 100)       # Gir vinduet avstand fra venstre kant av skjermen, 200, og fra toppen, 50, samt en selvdefinert størrelse, 120x100. Tall er i antall piksler.
                                                        # Fjern '#' foran koden over for å teste. NB, kan påvirke og bli påvirket av spacing og margins i koden under
        layout = QHBoxLayout()                      # Oppretter et layout av klassen QHBoxLayout
        self.setLayout(layout)                      # Sier at denne klassen (Hovedvindu) skal bruke nevnte layout

        button1 = QPushButton('Knapp 1')            # Oppretter en knapp av klassen QPushButton. Gir den teksten 'Knapp 1'
        button2 = QPushButton()                     # Oppretter en knapp av klassen QPushButton
        button2.setText('Knapp 2')                  # Alternativ måte å gi knappen en tekst
        button3 = QPushButton('Knapp 3')            # Oppretter en knapp av klassen QPushButton og gir den en tekst

        layout.addWidget(button1)                   # Legger til button1 i layout (vil bli vist helt til venstre siden den legges til først)
        layout.addWidget(button3)                   # Legger til button3 i layout (vil bli vist etter button1, jmf. append()-metoden vi har sett på tidligere)
        layout.addStretch()                        # Vi kan legge til en stretch, dersom vi ønsker å flytte knapper til en side i vinduet. Hvor i koden vi legger til denne vil påvirke sluttresultatet. Legger vi den til her vil elementer vi allerede har lagt til bli presset til venstre vinduet, mens elementer vi legger til etter vil bli presset til høyre.
                                                        # Fjern '#' foran koden over for å teste
        layout.addWidget(button2)                   # Legger til button2 i layout
                                                        # Endre gjerne verdiene på linjene under for å se forskjellen
        layout.setSpacing(20)                       # Vi kan bestemme avstanden mellom knappene ved å legge til spacing
        layout.setContentsMargins(70, 70, 70, 70)   # Vi kan bestemme avstanden fra vinduskantene elementene skal plasseres

        self.show()                                 # Her har vi lagt show() i klassen. Siden denne ligger i __init__-metoden vil den bli utført når vi oppretter et objekt av Hovedvindu

if __name__ == '__main__':                          # Sjekker om det er denne filen vi starter/kjører. I så tilfelle kjøres koden under.
    app = QApplication(sys.argv)                    # Må alltid med

    vindu = Hovedvindu()                            # Oppretter et objekt av Hovedvindu()-klassen

    sys.exit(app.exec())                            # Må alltid med
