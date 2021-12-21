import RPi.GPIO as GPIO
import time

LED_RED = 10
LED_YELLOW = 9
LED_GREEN = 11
GPIO.setmode(GPIO.BCM)   # GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_RED, GPIO.OUT)  # GPIO.OUT or GPIO.IN
GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)

for i in range(1):
    GPIO.output(LED_RED, GPIO.HIGH) # 1
    print("led RED on")
    time.sleep(2)
    GPIO.output(LED_RED, GPIO.LOW) # 0
    print("led RED off")
    time.sleep(2)
    GPIO.output(LED_YELLOW, GPIO.HIGH) # 1
    print("led YELLOW on")
    time.sleep(2)
    GPIO.output(LED_YELLOW, GPIO.LOW) # 0
    print("led YELLOW off")
    time.sleep(2)
    GPIO.output(LED_GREEN, GPIO.HIGH) # 1
    print("led GREEN on")
    time.sleep(2)
    GPIO.output(LED_GREEN, GPIO.LOW) # 0
    print("led GREEN off")
    time.sleep(2)

GPIO.cleanup() # GPIO 핀상태 초기화