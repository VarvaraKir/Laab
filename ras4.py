import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) 
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        print('0 - 255')
        input_value = input()

        if (input_value.isdigit() and int(input_value) %1 == 0 and 0 <= int(input_value) <= 255):
            num = int(input_value)
            print(decimal2binary(num))
            GPIO.output(dac, decimal2binary(num))
            u = (3.3 / 256) * num 
            print (u)
        else:
            print ('is not digit')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
