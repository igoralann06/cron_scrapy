from kleinanzeigen import kleinanzeigen
from rebuy_kle import rebuy_kle

def klei_thread():
  while True:
    rebuy_kle()
    kleinanzeigen()

klei_thread()