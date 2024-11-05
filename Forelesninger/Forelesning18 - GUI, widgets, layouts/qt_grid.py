import sys
from PyQt6.QtWidgets import *

# Lager en klasse, Hovedvindu, som skal arve fra klassen QWidget.
# Denne klassen er tenkt å inneholde all kode for å lage GUI som skal vises for vinduet vårt.
class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Gridlayout')                       # Gir vinduet en tittel
        self.setGeometry(100, 100, 700, 700)             # Gir vinduet en selvdefinert størrelse

        layout = QGridLayout()                                  # Oppretter et layout av klassen QGridLayout
        self.setLayout(layout)                                  # Sier at denne klassen (Hovedvindu) skal bruke nevnte layout

        min_label = QLabel()                                    # Oppretter en label
        min_label.setText('Dette er en label')                  # Legger tekst på labelen
        layout.addWidget(min_label,0,0)                  # Legger til labelen i layoutet, med koordinater 0,0

        min_knapp = QPushButton('min knapp')                    # Oppretter en knapp med klassen QPushButton, gir den teksten 'min knapp'
        layout.addWidget(min_knapp, 0,1)                 # Legger til knappen i layoutet, med koordinater 0,1

        min_inputlinje = QLineEdit()                            # Oppretter en inpulinje med klassen QLineEdit
        min_inputlinje.setPlaceholderText('Enkel linje, dette er standardtekst')    # Gir den en placeholdertekst
        layout.addWidget(min_inputlinje, 0, 2)           # Legger til inputlinja i layoutet, med koordinatene 0,2

        min_radioknapp = QRadioButton('radioknapp')             # Oppretter en radioknapp med klassen QRadioButton, og gir den en tekstbeskrivelse
        layout.addWidget(min_radioknapp, 1,0)            # Legger til radioknappen i layoutet, med koordinatene 1,0

        min_sjekkboks = QCheckBox('Avkrysningsboks')            # Oppretter en avkrysningsboks med klassen QCheckBox, gir den en tekstbeskrivelse
        layout.addWidget(min_sjekkboks, 1, 1)            # Legger til avkrysningsboksen i layoutet, med koordinatene 1,1

        min_comboboks = QComboBox()                             # Oppretter en rullegardinmeny med klassen QComboBox
        min_comboboks.setPlaceholderText('Velg ett alternativ:')    # Gir den en placeholdertekst
        min_comboboks.addItem('Alternativ 1')                   # Legger til et valg i menyen
        min_comboboks.addItem('Alternativ 2')                   # Legger til et valg til i menyen
        layout.addWidget(min_comboboks, 1,2)             # Legger menyen til i layoutet, med koordinater 1,2

        min_tekst = QTextEdit()                                 # Oppretter en tekstboks (flere linjer) med klassen QTextEdit
        min_tekst.setPlaceholderText('Brukerinput, flere linjer')   # Gir boksen en placeholdertekst
        layout.addWidget(min_tekst, 2, 0)                # Legger til tekstboksen i layoutet, med koordinatene 2,0

        min_beskjed = QMessageBox()                             # Oppretter en melding til bruker med klassen QMessageBox
        min_beskjed.setText('Hei bruker, dette er en beskjed til deg!')     # Bestemmer teksten som skal vises til bruker
        layout.addWidget(min_beskjed, 2,2)               # Legger til boksen i layoutet, med koordinatene 2,1

        min_slider = QSlider()                                  # Oppretter en slider med klassen QSlider
        min_slider.setRange(10, 80)                   # Velger hva som er minimum- og maksimumverdi
        layout.addWidget(min_slider, 2,1)                # Legger den til i layoutet, med koordinatene 2,2

        self.show()                                             # Her har vi lagt show() i klassen. Siden denne ligger i __init__-metoden vil den bli utført når vi oppretter et objekt av Hovedvindu

if __name__ == '__main__':                                      # Sjekker om det er denne filen vi starter/kjører. I så tilfelle kjøres koden under.
    app = QApplication(sys.argv)                                # Må alltid med

    vindu = Hovedvindu()                                        # Oppretter et objekt av Hovedvindu()-klassen

    sys.exit(app.exec())                                        # Må alltid med
