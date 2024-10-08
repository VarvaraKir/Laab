import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

dac=[8,11,7,1,0,5,12,6] 
comp=24
troyka=13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(element) for element in bin(decimal)[2:].zfill(8)]

def adc(value):
    sign = decimal2binary(value)
    GPIO.output(dac, sign)
    return sign

try:
    while True:
        k = 0
        for value in range (7, -1, -1):
            signal = adc(value)
            k += 2**value
            t = decimal2binary(k) 
            GPIO.output(dac, t)
            time.sleep(0.1)
            compnum = GPIO.input(comp)

            if compnum > 0:
                k -=2**value
            u = (3.3 / 256) * k
            print (u)
               
       

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
  