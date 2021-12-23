import RPi.GPIO as GPIO
import time

LED_PIN_1 = 4
LED_PIN_2 = 17
LED_PIN_3 = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)

for i in range(10):
    GPIO.output(LED_PIN_1, GPIO.HIGH)
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN_1, GPIO.LOW)
    print("led off")
    GPIO.output(LED_PIN_2, GPIO.HIGH)
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN_2, GPIO.LOW)
    print("led off")
    GPIO.output(LED_PIN_3, GPIO.HIGH)
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN_3, GPIO.LOW)
    print("led off")
    
GPIO.cleanup()