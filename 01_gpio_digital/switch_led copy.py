import RPi.GPIO as GPIO

LED_PIN1 = 9
SWITCH_PIN1 = 26
LED_PIN2 = 10
SWITCH_PIN2 = 19
LED_PIN3 = 11
SWITCH_PIN3 = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(SWITCH_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운저항
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(SWITCH_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운저항
GPIO.setup(LED_PIN3, GPIO.OUT)
GPIO.setup(SWITCH_PIN3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운저항

try:
    while True:
        val1 = GPIO.input(SWITCH_PIN1)  # 누르지 않은 경우 0, 눌렀을 때는 1
        print(val1)
        GPIO.output(LED_PIN1, val1)
        val2 = GPIO.input(SWITCH_PIN2)  # 누르지 않은 경우 0, 눌렀을 때는 1
        print(val2)
        GPIO.output(LED_PIN2, val2)
        val3 = GPIO.input(SWITCH_PIN3)  # 누르지 않은 경우 0, 눌렀을 때는 1
        print(val3)
        GPIO.output(LED_PIN3, val3)

finally:
    GPIO.cleanup()
    print('cleanup and exit')