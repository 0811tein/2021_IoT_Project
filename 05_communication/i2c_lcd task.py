from lcd import drivers
import datetime
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
DHT_PIN = 23
display = drivers.Lcd()

try:
    while True:
        now=datetime.datetime.now()
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            display.lcd_display_string(now.strftime("%x%X"), 1)
            display.lcd_display_string(f'%.1f*C, %.1f%%' % (t, h), 2)
            time.sleep(0.5)
finally:
    print("Cleaning up!")
    display.lcd_clear()

