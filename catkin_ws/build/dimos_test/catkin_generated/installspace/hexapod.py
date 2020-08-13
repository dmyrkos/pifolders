#!/usr/bin/env python3

# Python ROS
import rospy

from dimos_test.msg import Sonars

from time import sleep
from adafruit_servokit import ServoKit

kit1 =ServoKit(channels=16,address=0x40)
kit2 = ServoKit(channels=16,address=0x41)

# kit1 3 left legs : front leg ch 0 , 1, 2 , middle ch :3 ,4 ,5  back ch 6 ,7 ,8
# kit2 3 right legs : front leg ch 0 , 1, 2 , middle ch :3 ,4 ,5  back ch 6 ,7 ,8
#
#
joint_properties = {

    'LFH': (0, 100, 0, -1), 'LFK': (1, 70, 0, -1), 'LFA': (2, 180, 0, 1),
    'RFH': (3, 90, 0, 1), 'RFK': (4, 120, 0, 1), 'RFA': (5, 130, 610, -1),
    'LMH': (6, 320, 470, -1), 'LMK': (7, 251, 531, -1), 'LMA': (8, 130, 610, 1),
    'RMH': (0, 380, 530, 1), 'RMK': (1, 290, 605, 1), 'RMA': (2, 150, 630, -1),
    'LBH': (6, 350, 500, -1), 'LBK': (4, 200, 515, -1), 'LBA': (5, 180, 660, 1),
    'RBH': (6, 350, 500, 1), 'RBK': (7, 300, 615, 1), 'RBA': (8, 130, 610, -1)
    }

#walk 1 leg  -> ch 0 :: RFH	ch 1 ::	 RFK	ch 2 :: RFA = Right front = [0]leg scheme
#				ch 3 :: LFH	ch 4 ::	 LFK	ch 5 :: LFA = left front  = [5] 
#				ch 6 :: RMH	ch 7 ::	 RMK	ch 8 :: RMA = right mid   = [1]
#				ch 9 :: LMH	ch 10 :: LMK	ch 11 :: LMA = left mid   = [4]
#				ch 12 :: LBH ch 13 :: LBK	ch 14 :: LBA =left back   = [3]

init_position=[100 , 70 , 180 , 100 , 120 , 0 , 100 , 70, 180 , 90 ,120 , 0 , 90 , 120 , 0] # order of the list is the same of the legs
init_position2=[(100 , 70 , 180) , (100 , 70, 180) ,(0,0,0) , (90 , 120 , 0), (90 ,120 , 0) ,(100 , 120 , 0)]
#forw_position=[(90 , 90 , 180) , (125 , 120 , 180 ) ,(0, 0, 0), (55 , 120, 0) , (55 ,90 , 180) , (55 , 120 , 45)]right_ini
right_init = [100,70,180 , 100,70,180 , 100,70,180]
left_init= [100,120,0 , 100,120,0 , 90,120 ,0]
#backward_position=[(55 , 70 , 180) , (55 , 120 , 180 ) ,(0, 0, 0), (125 , 120, 0) , (125 ,120 , 0) , (125 , 120 , 0)]
FORWARD = 40
BACKWARD = 40
UP = 30
DOWN =30

def test_servo():

	rospy.init_node('servo_test', anonymous=True)

	initialize()

	rospy.spin()

def initialize() :

	for i in range(9):
		kit1.servo[i].angle = right_init[i]
		sleep(0.2)
		kit2.servo[i].angle = left_init[i]
		sleep(0.2)

def walking():

	while(True):
		 kit.servo[0].angle = 45
		 sleep(0.5)
		 kit.servo[0].angle = 0
		 sleep(0.5)
		 kit2.servo[0].angle = 45
		 sleep(0.5)
		 kit2.servo[0].angle = 0
		 sleep(0.5)


		 
if __name__ == '__main__':

    test_servo()


	

