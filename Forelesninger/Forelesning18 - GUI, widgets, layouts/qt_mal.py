# Denne koden kan fungere som en mal for å lage et GUI
# Inneholder det mest nødvendige. Bygg ut klassen Hovedvindu med egen kode.
# Ønsker man funksjonalitet fra andre moduler må de importeres

import sys
from PyQt6.QtWidgets import QApplication, QWidget
#from PyQt6.QtWidgets import *                  # Kan brukes istedenfor linja over for å importere alt fra QtWidgets

class Hovedvindu(QWidget):
    def __init__(self, *args, **kwargs):        # *args er for å lese argumenter fra kommandolinja, **kwargs brukes når vi ikke vet hvor mange argumenter vi ender opp med. Ikke nødvendig å ha med *args og **kwargs dersom vi ikke skal starte fra kommandolinjen eller ha parametere.
        super().__init__(*args, **kwargs)

        # sett vindustittel
        self.setWindowTitle('Mitt vindu')

        # Vis vinduet
        self.show()


if __name__ == '__main__':                      # Sjekker om det er denne filen vi starter/kjører. I så tilfelle kjøres koden under. Hadde vi derimot importert denne fila til en annen og kjørt den andre ville ikke koden under bli utført.
    app = QApplication(sys.argv)

    # Lage hovedvinduet
    window = Hovedvindu()

    # start event loop-en (appen)
    sys.exit(app.exec())
