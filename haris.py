#Libraries
import RPi.GPIO as GPIO
import time
from time import sleep
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.setup(26,GPIO.OUT)
pwm = GPIO.PWM(26,50)
pwm.start(0)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.00ms to LOW
    time.sleep(00)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if name == 'main':
    try:
        while True:
            dist = distance()
            if dist >= 10.0:
                print("DOOR OPEN")
                pwm.ChangeDutyCycle(5) 
                time.sleep(1)
            else:
                print("DOOR CLOSED")
                pwm.ChangeDutyCycle(10)
                time.sleep(1)
            #print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
	pwm.stop()
        print("Measurement stopped by User")
        GPIO.cleanup()