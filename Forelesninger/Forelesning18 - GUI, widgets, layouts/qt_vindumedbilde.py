from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
import sys

# Lager en klasse, Vindu, som skal arve fra klassen QWidget.
# Denne klassen er tenkt å inneholde all kode for å lage GUI for vinduet vårt.
class Vindu(QWidget):
    # En klasse må alltid ha en __init__-metode. Denne skal også bruke super sin __init__ (altså init-metoden til QWidget).
    def __init__(self):
        super().__init__()                      # Kaller init-metoden til QWidget (som er parent til vår Vindu-klasse)
        self.setWindowTitle('Enkelt vindu')     # Gir vinduet en tittel
        self.resize(300, 300)                   # Gjør om størrelsen, slik at vinduet er 300x300 piksler ved oppstart

        label1 = QLabel()                       # Oppretter en label (av klassen QLabel) som skal inneholde tekst
        label1.setText("Hello world!")          # Gir widgeten/labelen et tekstinnhold

        label_img = QLabel()                    # Oppretter en label (av klassen QLabel) som skal inneholde et bilde
        pixmap = QPixmap('pony.jpg')            # Lager pixmap av en bildefil
        label_img.setPixmap(pixmap)             # Gir widgeten/labelen et bildeinnhold (pixmappet av bildefilen)

        layout = QVBoxLayout()                  # Oppretter et layout av klassen QVBoxLayout. Dette er et vertikalt layout
        self.setLayout(layout)                  # sier at denne klassen (Vindu) skal bruke nevnte layout
        layout.addWidget(label1)                # Legger til tekstlabelen i layout
        layout.addWidget(label_img)             # Legger til bildelabelen i layout




app = QApplication(sys.argv)                    # Må alltid med
vindu = Vindu()                                 # Lager et objekt av Vindu()-klassen
vindu.show()                                    # vinduet skal vises på skjermen
sys.exit(app.exec())                            # Må alltid med
