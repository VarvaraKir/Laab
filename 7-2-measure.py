import RPi.GPIO as GPIO
import time 
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)


dac=[8,11,7,1,0,5,12,6] 
comp=24
troyka=13

GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(element) for element in bin(decimal)[2:].zfill(8)]

def adc():
    k = 0
    for value in range (7, -1, -1):
        k += 2**value
        t = decimal2binary(k)             
        GPIO.output(dac, t)
        time.sleep(0.01)
        compnum = GPIO.input(comp)

        if compnum > 0:
            k -=2**value
        print(k)
    
    return k
try: 
    N = 0
    a = 0
    res = []
    start = time.time()
    GPIO.output(13, 1)
    while a < 205:
        N +=1
        a = adc()
        res.append(a)
    GPIO.output(13, 0)

    while a > 120:
        a = adc()
        if a != 0:
            N +=1
            res.append(a)
        else:
            N += 1
            res.append(a)
            break

    print("График будет примерно сейчас!")
    stop = time.time()
    dec = stop - start

    plt.plot(res)
    plt.show()

    c = 1/dec

    res = [str(item) for item in res]
    with open("res.txt", "w") as outfile:
        outfile.write("\n".join(res))
    
    with open("measure.txt", "w") as outfile:
        outfile.write("period: " + " " + "c" + "\n")
        outfile.write("step: " + " " + "0.013")


finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
