# 도 음 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# PWM 인스턴스 생성
# 주파수 설정(4옥타브 도음 : 262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(50)    # duty cycle (0~100)


# 도레미파솔라시도 소리내기
melody = (262, 294, 330, 349, 392, 440, 494, 523)
melody1 = (392, 392, 440, 440, 392, 392, 330)
melody2 = (392, 392, 330, 330, 294)
melody3 = (392, 330, 294, 330, 262)

try:
    # pwm.ChangeFrequency(262)
    # time.sleep(1)
    for i in melody1:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.5)
    for i in melody2:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(1.5)
    for i in melody1:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.5)
    for i in melody3:s
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(1.5)

finally:
    pwm.stop()
    GPIO.cleanup()