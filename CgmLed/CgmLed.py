from __future__ import division
import time
import urllib
import json

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)

from luma.core import legacy
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

while True:
    try:
        url = "http://cgm.dmar.me.uk/api/v1/entries/current.json"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        sgv = data[0]['sgv']
        direction = data[0]['direction']
        
        sgv_int = int(sgv)
        mmol_float = round(sgv / 18, 1) 
        mmol = str(mmol_float)
        
        if "up" in direction.lower():
            direction = "U"
        elif  "down" in direction.lower():
            direction = "D"
        else:
           direction = "F"

        mmol = mmol + direction

        with canvas(device) as draw:
            legacy.text(draw, (0, 0), mmol, fill="white", font=proportional(CP437_FONT))
        
        time.sleep(60)
    except:
        with canvas(device) as draw:
            legacy.text(draw, (0, 0), "Offline", fill="white", font=proportional(CP437_FONT))
  