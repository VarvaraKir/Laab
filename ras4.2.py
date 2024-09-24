import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    num = int(input())
    GPIO.output(dac, decimal2binary(num))
    u = (3.3 / 256) * num 
    print (u)
    t = int(input('Write time in seconds'))
    t = t/512

    while True:

        for i in range(256):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(t)
            
        for i in range (255, -1, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(t)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
