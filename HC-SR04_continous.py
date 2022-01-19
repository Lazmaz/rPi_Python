import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

echo = 24
trig = 23
led = 25

GPIO.setup(echo, GPIO.IN)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

try:
    while True:
        GPIO.output(trig, False)
        time.sleep(0.001)

        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)
    
        #pulseIn
        while GPIO.input(echo)==0:
            pulseStart = time.time()

        while GPIO.input(echo)==1:
            pulseEnd = time.time()

        duration = pulseEnd - pulseStart

        #measure distance 
        distance = duration * 17150

        distance = round(distance, 2)

        if distance < 10:
            GPIO.output(led, True)
        else:
            GPIO.output(led, False)

        print ("Distance: ",distance,"cm")
except KeyboardInterrupt:
    print ("Setting all GPIO pins to default")
    GPIO.cleanup()
    print("exiting program") 