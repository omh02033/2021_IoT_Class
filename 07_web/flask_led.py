from flask import Flask
import RPi.GPIO as GPIO

LED_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)


app = Flask(__name__)

@app.route("/")
def hello_woeld():
    return'''
    <p>Hello, Flask!</p>
    <a href="/led/on">LED ON</a>
    <a href="led/off">LED OFF<a>
    '''

@app.route("/led/<cmd>")
def led_op(cmd):
    print(cmd)
    if cmd == "on":
        GPIO.output(LED_PIN,GPIO.HIGH)
        return'''
        <p>LED ON</p>
        <p></p>
        <a href="/">Go Home</a>
        '''
    elif cmd == "off":
        GPIO.output(LED_PIN,GPIO.LOW)
        return'''
            <p>LED OFF</p>
            <p></p>
            <a href="/">Go Home</a>
            '''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()