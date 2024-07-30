from rebuy import rebuy
from vinted import main as vinted

def vinted_thread():
  while True:
    rebuy()
    vinted()
    
vinted_thread()