from lcd import drivers
import time
import Adafruit_DHT
import datetime


display = drivers.Lcd()

sensor = Adafruit_DHT.DHT11
PIN = 14

try:
    while True:
        h, t = Adafruit_DHT.read(sensor, PIN)
        if h is not None and t is not None:
            now = datetime.datetime.now()
            printa = (now.strftime("%x%X"))
            
            display.lcd_display_string(printa,1)
            display.lcd_display_string('%.1f*, %.1f%%' %(t,h), 2)

        else:
            print("Read error")
        time.sleep(1)

finally:
    display.lcd_clear()
    print("End of Program")
