from time import sleep 
import smbus
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
from sonar import Distance_Sensor
from functions import  Walk_test
from mpu6050 import mpu6050


try :
	mpu = mpu6050(0x68)   	
	while True :
		print("Temp :" , mpu.get_temp())
		accel_data = mpu.get_accel_data()
		print("Ax =" , accel_data['x'])
		print("Ay =" , accel_data['y'])
		print("Az =" , accel_data['z'])
		gyro_data = mpu.get_gyro_data()
		print("Gx =" , gyro_data['x'])
		print("Gy =" , gyro_data['y'])
		print("Gy =" , gyro_data['z'])

		if Distance_Sensor() >= 10 :

			print("good")
			Walk_test(False)
		else :
			Walk_test(True)
			print("sak it")
			break

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    GPIO.cleanup()
