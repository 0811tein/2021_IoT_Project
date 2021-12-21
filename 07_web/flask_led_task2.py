from flask import Flask, render_template
import RPi.GPIO as GPIO

# Flask 객체 생성
# __name__은 파일명
LED_RED_PIN = 5
LED_BLUE_PIN = 6

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED_PIN, GPIO.OUT)
GPIO.setup(LED_BLUE_PIN, GPIO.OUT)


# 라우팅을 위한 뷰 함수
@app.route("/")
def hello():
    return render_template("led2.html")
@app.route("/<color>/<op>")
def led_op(color, op):
    if color == "red":
        if op == "on":
            GPIO.output(LED_RED_PIN, GPIO.HIGH)
            return "LED RED ON"
        elif op == "off":
            GPIO.output(LED_RED_PIN, GPIO.LOW)
            return "LED RED OFF"
        else:
            return "ERROR"
    elif color == "blue":
        if op == "on":
            GPIO.output(LED_BLUE_PIN, GPIO.HIGH)
            return "LED BLUE ON"
        elif op == "off":
            GPIO.output(LED_BLUE_PIN, GPIO.LOW)
            return "LED BLUE OFF"
        else:
            return "ERROR"

# 터미널에서 직접 실행 시킨 경우
if __name__ == "__main__":
    try:
        app.run(host = "0.0.0.0")
    finally:
        GPIO.cleanup()