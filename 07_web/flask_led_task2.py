from flask import Flask, render_template
import RPi.GPIO as GPIO

RED_LED_PIN = 4
BLUE_LED_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN,GPIO.OUT)
GPIO.setup(BLUE_LED_PIN,GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello_woeld():
    return render_template("led2.html")

@app.route("/led/<opp>/<cmd>")
def led_op(opp,cmd):
    print(opp)
    if opp == "red":
        print(cmd)
        if cmd == "on":
            GPIO.output(RED_LED_PIN,GPIO.HIGH)
            return "RED ON"
        elif cmd == "off":
            GPIO.output(RED_LED_PIN,GPIO.LOW)
            return "RED OFF"
    
    elif opp == "blue":
        print(cmd)
        if cmd == "on":
            GPIO.output(BLUE_LED_PIN,GPIO.HIGH)
            return "BLUE ON"
        elif cmd == "off":
            GPIO.output(BLUE_LED_PIN,GPIO.LOW)
            return "BLUE OFF"


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()