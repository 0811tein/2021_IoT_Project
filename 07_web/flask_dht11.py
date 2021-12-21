from flask import Flask, render_template
import Adafruit_DHT
import json

sensor = Adafruit_DHT.DHT11
PIN = 23


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("dht11.html")


@app.route("/monitor")
def monitoring():
    try:
        h, t = Adafruit_DHT.read_retry(sensor, PIN)
        if h is not None and t is not None:
            obj = {'humidity': h, 'temperature': t}
            return json.dumps(obj)
        else:
            return 'Read error'
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        print("clean up")