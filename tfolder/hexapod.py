#!/usr/bin/env python3

# Python ROS
#import rospy
from time import sleep
from adafruit_servokit import ServoKit


jp = {
    'LFH': (0,100), 'LFK': (1,110), 'LFA': (2,0),
    'LMH': (3,100), 'LMK': (4,110), 'LMA': (5,0),
    'LBH': (6,100), 'LBK': (7,110), 'LBA': (8,0),
    'RFH': (0,100), 'RFK': (1,70), 'RFA': (2,180),    
    'RMH': (3,100), 'RMK': (4,70), 'RMA': (5,180),
    'RBH': (6,100), 'RBK': (7,70), 'RBA': (8,180)
    }

left_j= ['LFH', 'LFK','LFA','LMH','LMK','LMA','LBH','LBK','LBA']

kitL = ServoKit(channels=16,address=0x41)
kitR = ServoKit(channels=16,address=0x40)



class Hexapod:

	def __init__(self):
		self.left_front = Leg('left front', 'LFH', 'LFK', 'LFA')
		self.right_front = Leg('right front', 'RFH', 'RFK', 'RFA')
		self.left_middle = Leg('left middle', 'LMH', 'LMK', 'LMA')
		self.right_middle = Leg('right middle', 'RMH', 'RMK', 'RMA')
		self.left_back = Leg('left back', 'LBH', 'LBK', 'LBA')
		self.right_back = Leg('right back', 'RBH', 'RBK', 'RBA')

		self.legs = [self.left_front, self.right_front,
					self.left_middle, self.right_middle,
					self.left_back, self.right_back]

		self.right_legs = [self.right_front, self.right_middle, self.right_back]
		self.left_legs = [self.left_front, self.left_middle, self.left_back]
		# self.kit = kitL if self.right
		


		self.tripod1 = [self.left_front, self.right_middle, self.left_back]
		self.tripod2 = [self.right_front, self.left_middle, self.right_back]

		self.hips, self.knees, self.ankles = [], [], []

		for leg in self.legs:
			self.hips.append(leg.hip)
			self.knees.append(leg.knee)
			self.ankles.append(leg.ankle)


	def initialize(self):
		for leg in self.legs:
			leg.off()
	

	def walking(self,steps):
		for step in range(steps) :
			self.tripod_gait(self.tripod1,0)
			sleep(0.2)
			self.tripod_gait(self.tripod1,1)
			sleep(0.2)
			self.tripod_gait(self.tripod1,2)
			sleep(0.2)	
			self.tripod_gait(self.tripod2,3)
			sleep(0.2)
			self.tripod_gait(self.tripod2,0)
			sleep(0.2)
			self.tripod_gait(self.tripod2,1)
			sleep(0.2)
			self.tripod_gait(self.tripod2,2)
			sleep(0.2)
			self.tripod_gait(self.tripod1,3)
			sleep(0.2)
			if step == steps-1:
				self.tripod_gait(self.tripod2,3) #last step to actually go in the init position 

		for t1,t2 in zip(self.tripod1,self.tripod2) :
			print("hope it qw ::: " ,t1.hip ,t2.hip,"knee :: ",t1.knee ,t2.knee)

			
	def tripod_gait(self,tr1,seq):
		if seq == 0 :
			for t in tr1:
				print("hey22",t.knee)
				t.knee.move(30)
				print("hey223 seq 0",t.knee)
		elif seq == 1:
			for t in tr1:
				t.hip.move(-30)
				print("hey seq 1",t.hip)
		elif seq == 2 :
			for t in tr1:
				t.knee.move(-30)
				print("hey seq 2",t.knee)
		elif seq == 3 :
			for t in tr1:
				print("hey seq 3before -==-=-=",t.hip,t.knee)
				t.off()
				print("hey seq 3",t.hip,t.knee)


	def rotate_clockwise(self,steps,t):
		for step in range(steps) :
			self.rotation_seq(self.tripod2,0)
			sleep(t)
			self.rotation_seq(self.tripod2,1)
			sleep(t)
			self.rotation_seq(self.tripod2,2)
			sleep(t)	
			self.rotation_seq(self.tripod1,3)
			sleep(t)
			self.rotation_seq(self.tripod1,0)
			sleep(t)
			self.rotation_seq(self.tripod1,1)
			sleep(t)
			self.rotation_seq(self.tripod1,2)
			sleep(t)
			self.rotation_seq(self.tripod2,3)
			sleep(t)

	def rotation_seq(self,tr1,seq):
		if seq == 0 :
			for t in tr1:
				print("seq 0 in rotation",t.knee)
				t.knee.move(30)
				print("hey223 seq 0",t.knee)
		elif seq == 1:
			if tr1 == self.tripod2 :
				for t in tr1:
					if t.hip.name == 'LMH':
						t.hip.move(30)
						print("hey seq 1",t.hip)
					else :
						t.hip.move(-30)
			else:
				for t in tr1:
					if t.hip.name == 'RMH':
						t.hip.move(-30)
						print("hey seq 1",t.hip)
					else :
						t.hip.move(30)
		elif seq == 2 :
			for t in tr1:
				t.knee.move(-30)
				print("hey seq 2",t.knee)
		elif seq == 3 :
			for t in tr1:
				print("hey seq 3before -==-=-=",t.hip,t.knee)
				t.off()
				print("hey seq 3",t.hip,t.knee)

 




class Leg:
	def __init__(self, name, hip_key, knee_key, ankle_key):
		
		self.hip =Joint("hip",hip_key)
		self.knee = Joint("knee",knee_key)
		self.ankle = Joint("ankle",ankle_key)
		self.name = name
		self.joints = [self.hip, self.knee, self.ankle]

 #    def pose(self, hip_angle = 0, knee_angle = 0, ankle_angle = 0):

 #        self.hip.pose(hip_angle)
 #        self.knee.pose(knee_angle)
 #        self.ankle.pose(ankle_angle)

	# def move(self, knee_angle = None, hip_angle = None, offset = 100):
 #        """ knee_angle < 0 means thigh is raised, ankle's angle will be set to the specified 
 #            knee angle minus the offset. offset best between 80 and 110 """
	# 	if knee_angle == None: knee_angle = self.knee.hip_angle
	# 	if hip_angle == None: hip_angle = self.hip.angle
	# 	self.pose(hip_angle, knee_angle, knee_angle - offset)

	# def replant(self, raised, floor, offset, t = 0.1):
	# 	pass
	def do_move(self):
		for joint in self.joints:
			joint.move(30)
			
	def off(self):
		for joint in self.joints:
			joint.off()

	def __repr__(self):
		return 'leg: ' + self.name


class Joint:
	
	def __init__(self, joint_type, jkey):
		self.joint_type, self.name =  joint_type, jkey
		self.channel, self.angle = jp[jkey]

	def move(self, angle):
		if self.name in left_j:
			kitL.servo[self.channel].angle = self.angle - angle
			self.angle = kitL.servo[self.channel].angle
			print("move joint",kitL.servo[self.channel].angle,"sds--=",self.angle)
		else:
		 	kitR.servo[self.channel].angle = self.angle + angle
		 	self.angle = kitR.servo[self.channel].angle
		# kit.servo[self.channel].angle = self.angle


	def off(self):
		if self.name in left_j:
			#print("off joint :" ,self.name, self.angle)
			kitL.servo[self.channel].angle = jp[self.name][1]
			self.angle = kitL.servo[self.channel].angle
			print(self.name, self.angle)
		else:
		 	kitR.servo[self.channel].angle = jp[self.name][1]
		 	self.angle = kitR.servo[self.channel].angle
		 	print(self.name, self.angle)


	def __repr__(self):
		return 'joint: ' + self.joint_type + ' : ' + self.name + ' angle: ' + str(self.angle)



hex1 = Hexapod()
hex1.initialize()
#print(hex1.tripod1[1].knee)
#hex1.walking(3)
print(" -------------- ")
hex1.rotate_clockwise(2,1)
# print(hex1.right_back.knee.angle)
#hex1.walking()
# print(hex1.right_back.knee.angle)
#hex1.initialize()





