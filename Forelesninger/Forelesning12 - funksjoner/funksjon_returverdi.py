#import math
# Istedenfor å importere hele modulen slik som over kan vi importere enkeltdeler hver for seg slik som under
from math import log

# Funksjon som skal regne om fra hundeår til menneskeår og returnere antall menneskeår
def hundealder_til_menneskealder(hundealder):
    menneskealder = 16 * log(hundealder) + 31
    return menneskealder

print(hundealder_til_menneskealder(50))

menneskealder = hundealder_til_menneskealder(10)
print(menneskealder)

# Funksjon som regner ut pris på en vare med moms (når vi vet prisen uten moms)
def inkluder_moms(pris, moms=0.25):
    pris_med_moms = pris + (pris * moms)
    return pris_med_moms
# Kaller på funksjonen, med 100 som argument
#inkluder_moms(100)

# Vi kan også bruke innholdet i en variabel som argument
# Her lager vi en variabel og setter den til 100
pris_uten_moms = 100
# Vi bruker så variabelen som argument når vi kaller på funksjonen
print(inkluder_moms(pris_uten_moms))
