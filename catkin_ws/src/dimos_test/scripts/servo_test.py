#!/usr/bin/env python3

# Python ROS
import rospy

from time import sleep
from adafruit_servokit import ServoKit

kitL =ServoKit(channels=16,address=0x40)
kitR = ServoKit(channels=16,address=0x41)

# kit1 3 left legs : front leg ch 0 , 1, 2 , middle ch :3 ,4 ,5  back ch 6 ,7 ,8
# kit2 3 right legs : front leg ch 0 , 1, 2 , middle ch :3 ,4 ,5  back ch 6 ,7 ,8
#
#
#joint properties
jp = {
    'LFH': (0,100), 'LFK': (1,110), 'LFA': (2,0),
    'LMH': (3,100), 'LMK': (4,110), 'LMA': (5,0),
    'LBH': (6,100), 'LBK': (7,110), 'LBA': (8,0),
    'RFH': (0,100), 'RFK': (1,70), 'RFA': (2,180),    
    'RMH': (3,100), 'RMK': (4,70), 'RMA': (5,180),
    'RBH': (6,100), 'RBK': (7,70), 'RBA': (8,180)
    }
#leg schemes
ls = {
			'L1' : ('LFH','LFK','LFA') , 'L2' : ('LMH','LMK','LMA'), 'L3' : ('LBH','LBK','LBA') ,
			'R1' : ('RFH','RFK','RFA') , 'R2' : ('RMH','RMK','RMA') ,'R3' : ('RBH','RBK','RBA') 
		}


right_init = [100,70,180 , 100,70,180 , 100,70,180]
left_init= [100,110,0 , 100,110,0 , 100,110 ,0]


FORWARD = 30
BACKWARD = -40
UP = 30
DOWN = -30

def test_servo():

	rospy.init_node('servo_test', anonymous=True)

	initialize()

	rospy.spin()

def initialize() :

	for i in range(9):
		kitL.servo[i].angle = left_init[i]
		sleep(0.2)
		kitR.servo[i].angle = right_init[i]
		sleep(0.2)



#  We only define 6 leg positions 
#  0 - Forward, Raised
#  1 - Mid, Raised
#  2 - Backward, Raised
#  3 - Forward, Lowered
#  4 - Mid, Lowered (this is the "normal" standing position)
#  5 - Backward, Lowered

# Tripod Gait  

def gait(Leg,sequence,direction) :

	if sequence == 0: #raise knee 
		for l in Leg :
			if l=='L1' or l=='L2' or l=='L3': 
				kitL.servo[ls[l][1]].angle =  jp[ls[l][1]] + UP
			else :
				kitR.servo[ls[l][1]].angle =  jp[ls[l][1]] - UP
	elif sequence == 1: #move hip fwd 
		for l in Leg :
			if l=='L1' or l=='L2' or l=='L3': 
				kitL.servo[ls[l][0]].angle =  jp[ls[l][1]] + FORWARD
			else :
				kitR.servo[ls[l][0]].angle =  jp[ls[l][1]] - FORWARD
	elif sequence == 2: # down knee 
		for l in Leg :
			if l=='L1' or l=='L2' or l=='L3': 
				kitL.servo[ls[l][1]].angle =  jp[ls[l][1]] + DOWN
			else :
				kitR.servo[ls[l][1]].angle =  jp[ls[l][1]] - DOWN
	elif sequence == 3: #move hip back 
		for l in Leg :
			if l=='L1' or l=='L2' or l=='L3': 
				kitL.servo[ls[l][0]].angle =  jp[ls[l][1]] + 60
			else :
				kitR.servo[ls[l][0]].angle =  jp[ls[l][1]] - 60
	else :
		pass


def tripod_gait(steps,direction):
	for s in steps :
		kitL.servo[jp['LFK'][0]].angle = jp['LFK'][1] + UP
		kitL.servo[jp['LFK'][0]].angle = jp['LFK'][1] + UP
		kitL.servo[jp['LFK'][0]].angle = jp['LFK'][1] + UP


# na valw metavlith gia direction // anti gia contiuous walking mporw na kanw steps
def walking(steps):
 
 	
	for s in steps :
		gait(['L1','R2','L3'],0,'fwd')
		sleep(0.2)
		gait(['L1','R2','L3'],1,'fwd')
		sleep(0.2)
		gait(['L1','R2','L3'],2,'fwd')
		sleep(0.2)
		gait(['R1','L2','R3'],0,'fwd')
		sleep(0.2)
		gait(['R1','L2','R3'],1,'fwd')
		sleep(0.2)
		gait(['R1','L2','R3'],2,'fwd')
		sleep(0.2)
		gait(['L1','R2','L3'],0,'fwd')
		sleep(0.2)
		gait(['L1','R2','L3'],3,'fwd')
		sleep(0.2)
		gait(['L1','R2','L3'],2,'fwd')
		sleep(0.2)
		gait(['R1','L2','R3'],0,'fwd')
		sleep(0.2)
		gait(['R1','L2','R3'],3,'fwd')
		sleep(0.2)
		gait(['R1','L2','R3'],2,'fwd')
		sleep(0.2)




		 
if __name__ == '__main__':

    test_servo()


	

