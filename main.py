import threading
import RPi.GPIO as GPIO
from time import sleep

# SET BOARD OPTIONS
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

entrancePin = 1
led1 = 18
led2 = 23
led3 = 24
led4 = 25
led5 = 8
led6 = 7
turned_on = False

leds = [led1, led2, led3,
       led4, led5, led6]


# SET PIN MODES
GPIO.setup(entrancePin, GPIO.IN)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led5, GPIO.OUT)
GPIO.setup(led6, GPIO.OUT)

def pisca_pisca(speed):
    ct = threading.current_thread()
    while True:
        if getattr(ct, "loop_over", True):
            for i in leds:
                GPIO.output(i, GPIO.HIGH)
                sleep(speed)
            for i in leds:
                GPIO.output(i, GPIO.LOW)
                sleep(speed)
        else:
            pass

if __name__ == '__main__':
    threadCore = threading.Thread(target=pisca_pisca, args=(0.05,))
    threadCore.start()
    while True:
        logicalLevel = GPIO.input(entrancePin)
        if logicalLevel == GPIO.HIGH:
            while (GPIO.input(entrancePin) == True):
                pass
            turned_on = not turned_on

        if turned_on: threadCore.loop_over = True
        else: threadCore.loop_over = False
