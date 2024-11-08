import sys, random
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QFormLayout, QComboBox, QDoubleSpinBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon


planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()

        # Setter tittel og størrelse på vinduet, og legger også til et ikon
        self.setWindowTitle('Planetvekt')
        self.setGeometry(100, 100, 500, 400)
        vinduicon = QIcon('bilder/sun.png')
        self.setWindowIcon(vinduicon)

        # Oppretter et gridlayout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Lager en label som skal plasseres øverst i layoutet
        self.topplabel =QLabel()
        self.topplabel.setText("Hva er din vekt på en annen planet?")
        self.layout.addWidget(self.topplabel, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)  # 0,0 er koordinatene, 1 er antall rader topplabel skal strekke seg over, og 2 er antall kolonner den skal strekke seg over. alignment sentrerer widgeten .

        # TODO: skjema, bilder, hendelser, metoder

        self.show()                                                 # Må være med for at vinduet skal vises


# Må alltid med:
if __name__ == '__main__':
    app = QApplication(sys.argv)
    vindu = Hovedvindu()
    sys.exit(app.exec())

# To be continued..
