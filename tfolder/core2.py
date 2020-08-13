from time import sleep 
import smbus
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
from sonar import Distance_Sensor
from functions import  Walk_test
from mpu6050 import mpu6050



def check() :

	if Distance_Sensor() <=10 :
		return "sak"
	



try :
		
	while True :
		if check() == "sak" :
			print("too close ")
			break
		print("checking")

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    GPIO.cleanup()


# mpu = mpu6050(0x68)   
# 		print("Temp :" , mpu.get_temp())
# 		accel_data = mpu.get_accel_data()
# 		print("Ax =" , accel_data['x'])
# 		print("Ay =" , accel_data['y'])
# 		print("Az =" , accel_data['z'])
# 		gyro_data = mpu.get_gyro_data()
# 		print("Gx =" , gyro_data['x'])
# 		print("Gy =" , gyro_data['y'])
# 		print("Gy =" , gyro_data['z'])