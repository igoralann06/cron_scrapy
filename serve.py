from kleinanzeigen import kleinanzeigen
from rebuy import rebuy
from vinted import main as vinted

from threading import Thread

def klei_thread():
  while True:
    kleinanzeigen()


def vinted_thread():
  while True:
    vinted()

rebuy()
Thread(target=klei_thread).start()
Thread(target=vinted_thread).start()