import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFormLayout

# Lager en klasse, Hovedvindu, som skal arve fra klassen QWidget.
# Denne klassen er tenkt å inneholde all kode for å lage GUI som skal vises for vinduet vårt.
class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Oppmeldingsskjema')                    # Gir vinduet en tittel
        self.setGeometry(100, 100, 300, 100)                        # Gir vinduet en selvdefinert størrelse
        layout = QFormLayout()                                      # Oppretter et layout av klassen QFormLayout
        self.setLayout(layout)                                      # Sier at denne klassen (Hovedvindu) skal bruke nevnte layout

        layout.addRow('Navn:', QLineEdit(self))                     # Legger til en linje i layoutet med addRow(). Første del skal være teksten 'Navn:', andre del skal være en QLineEdit
        layout.addRow('Epost:', QLineEdit(self))                    # Legger til en linje i layoutet med addRow(). Første del skal være teksten 'Epost:', andre del skal være en QLineEdit
        layout.addRow('Passord:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))            # Legger til en linje i layoutet med addRow(). Første del skal være teksten 'Passord:', andre del skal være en QLineEdit. echoMode sier noe om hvordan teksten skal vises til brukeren, her skal teksten være 'skjult'.
        layout.addRow('Bekreft passord:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))    # Legger til en linje i layoutet med addRow(). Første del skal være teksten 'Bekreft passord:', andre del skal være en QLineEdit. echoMode sier noe om hvordan teksten skal vises til brukeren, her skal teksten være 'skjult'.
        layout.addRow(QPushButton('Meld meg opp'))                  # Legger til en linje i layoutet med addRow(). Her legges det til en knapp med en tekst på.

        self.show()                                         # Her har vi lagt show() i klassen. Siden denne ligger i __init__-metoden vil den bli utført når vi oppretter et objekt av Hovedvindu


if __name__ == '__main__':                      # Sjekker om det er denne filen vi starter/kjører. I så tilfelle kjøres koden under.
    app = QApplication(sys.argv)                # Må alltid med

    vindu = Hovedvindu()                        # Oppretter et objekt av Hovedvindu()-klassen

    sys.exit(app.exec())                        # Må alltid med
