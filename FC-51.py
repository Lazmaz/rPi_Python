import RPi.GPIO as GPIO
import time #gives us acces to sleep

GPIO.setmode(GPIO.BCM) #alternative is GPIO.BOARD

signal = 21

GPIO.setup(signal, GPIO.IN)

try:
    while True:  #1 = True, loops everything within 
        val = GPIO.input(signal) #Read FC-51 out pin
        print(val)
        time.sleep(0.5)
except KeyboardInterrupt:
    print ("Setting all GPIO pins to default")
    GPIO.cleanup()  #Sets all GPIO pins to default state, you cant run it if its in the beginning of a program
    print("exiting program")

#gives you the ability to interupt the program by typing "ctrl+c" cleaning up all off your pins