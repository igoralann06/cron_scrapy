from kleinanzeigen import kleinanzeigen
from rebuy_kle import rebuy_kle
from rebuy import rebuy
from vinted import main as vinted

from threading import Thread

con = sqlite3.connect("awin.db")
cur = con.cursor()

def klei_thread():
  while True:
    kleinanzeigen()

def vinted_thread():
  while True:
    vinted()

rebuy_kle()
rebuy()
Thread(target=klei_thread).start()
Thread(target=vinted_thread).start()