import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


TRIG = 23
ECHO = 24


print ("Distance Measurement In Progress")

def Distance_Sensor() :
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    #print ("Waiting For Sensor To Settle")
    time.sleep(0.5)


    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)


    while GPIO.input(ECHO)==0:
      pulse_start = time.time()


    while GPIO.input(ECHO)==1:
      pulse_end = time.time()


    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print ("Distance:",distance,"cm")
    return distance



# try:
#     while True :
#         Distance_Sensor()
#         print("ss")

# except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
#     print("Cleaning up!")
#     GPIO.cleanup()