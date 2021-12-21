from flask import Flask
import RPi.GPIO as GPIO

# Flask 객체 생성
# __name__은 파일명
LED_RED_PIN = 22
LED_BLUE_PIN = 27

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED_PIN, GPIO.OUT)
GPIO.setup(LED_BLUE_PIN, GPIO.OUT)


# 라우팅을 위한 뷰 함수
@app.route("/")
def hello():
    return '''
        <p>Hello, Flask</p>
        <a href="/led/red/on">LED RED ON</a>
        <a href="/led/red/off">LED RED OFF</a> <br>
        <a href="/led/blue/on">LED BLUE ON</a>
        <a href="/led/blue/off">LED BLUE OFF</a>
    '''
@app.route("/led/<color>/<op>")
def led_op(color, op):
    if color == "red":
        if op == "on":
            GPIO.output(LED_RED_PIN, GPIO.HIGH)
            return '''
        <p>LED ON</p>
        <a href="/">Go Home</a>
    '''
        elif op == "off":
            GPIO.output(LED_RED_PIN, GPIO.LOW)
            return '''
        <p>LED OFF</p>
        <a href="/">Go Home</a>
    '''
    elif color == "blue":
        if op == "on":
            GPIO.output(LED_BLUE_PIN, GPIO.HIGH)
            return '''
        <p>LED ON</p>
        <a href="/">Go Home</a>
    '''
        elif op == "off":
            GPIO.output(LED_BLUE_PIN, GPIO.LOW)
            return '''
        <p>LED OFF</p>
        <a href="/">Go Home</a>
    '''

# 터미널에서 직접 실행 시킨 경우
if __name__ == "__main__":
    try:
        app.run(host = "0.0.0.0")
    finally:
        GPIO.cleanup()