# 도 음 출력하기
import RPI.GPIO as GPIO
import time

BUZZER_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# PWM 인스턴스 생성
# 주파수 설정(4옥타브 도음 : 262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10)    # duty cycle (0~100)

time.sleep(2)
pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()