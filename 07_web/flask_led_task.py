from flask import Flask
import RPi.GPIO as GPIO

RED_LED_PIN = 4
BLUE_LED_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN,GPIO.OUT)
GPIO.setup(BLUE_LED_PIN,GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello_woeld():
    return'''
    <p>Hello, Flask!</p>
    <a href="/led/red/on">RED LED ON</a>
    <a href="led/red/off">RED LED OFF<a>
    <p></p>
    <a href="/led/blue/on">BLUE LED ON</a>
    <a href="led/blue/off">BLUE LED OFF<a>
    '''

@app.route("/led/<opp>/<cmd>")
def led_op(opp,cmd):
    print(opp)
    if opp == "red":
        print(cmd)
        if cmd == "on":
            GPIO.output(RED_LED_PIN,GPIO.HIGH)
            return'''
            <p>RED LED ON</p>
            <p></p>
            <a href="/">Go Home</a>
            '''
        elif cmd == "off":
            GPIO.output(RED_LED_PIN,GPIO.LOW)
            return'''
                <p>RED LED OFF</p>
                <p></p>
                <a href="/">Go Home</a>
                '''
    
    elif opp == "blue":
        print(cmd)
        if cmd == "on":
            GPIO.output(BLUE_LED_PIN,GPIO.HIGH)
            return'''
            <p>BLUE LED ON</p>
            <p></p>
            <a href="/">Go Home</a>
            '''
        elif cmd == "off":
            GPIO.output(BLUE_LED_PIN,GPIO.LOW)
            return'''
                <p>BLUE LED OFF</p>
                <p></p>
                <a href="/">Go Home</a>
                '''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()