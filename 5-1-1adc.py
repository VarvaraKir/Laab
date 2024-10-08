import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

dac=[8,11,7,1,0,5,12,6] 
comp=14
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
        for value in range (256):
            signal = adc(value)
            GPIO.output(dac, signal)
            u = (3.3 / 256) * value
            time.sleep(0.01)
            compnum = GPIO.input(comp)

            if compnum > 0:
                print ('ADC value =', value, ' U=', u)
                break
       

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

        