from time import sleep 
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

Stop = False

					
#walk 1 leg  -> ch 0 :: RFH	ch 1 ::	 RFK	ch 2 :: RFA = Right front = [0]leg scheme
#				ch 3 :: LFH	ch 4 ::	 LFK	ch 5 :: LFA = left front  = [5] 
#				ch 6 :: RMH	ch 7 ::	 RMK	ch 8 :: RMA = right mid   = [1]
#				ch 9 :: LMH	ch 10 :: LMK	ch 11 :: LMA = left mid   = [4]
#				ch 12 :: LBH ch 13 :: LBK	ch 14 :: LBA =left back   = [3]

init_position=[100 , 70 , 180 , 100 , 120 , 0 , 100 , 70, 180 , 90 ,120 , 0 , 90 , 120 , 0] # order of the list is the same of the legs
init_position2=[(100 , 70 , 180) , (100 , 70, 180) ,(0,0,0) , (90 , 120 , 0), (90 ,120 , 0) ,(100 , 120 , 0)]
#forw_position=[(90 , 90 , 180) , (125 , 120 , 180 ) ,(0, 0, 0), (55 , 120, 0) , (55 ,90 , 180) , (55 , 120 , 45)]
#backward_position=[(55 , 70 , 180) , (55 , 120 , 180 ) ,(0, 0, 0), (125 , 120, 0) , (125 ,120 , 0) , (125 , 120 , 0)]
FORWARD = 40
BACKWARD = 40
UP = 30
DOWN =30


def initialize() :
	print("Initialinzing ...")
	for x in range(15) :
		kit.servo[x].angle = init_position[x]
		sleep(0.2)
	
# Leg numbering scheme		
#  0 - R Front 0,1,2
#  1 - R Middle 
#  2 - R Rear
#  3 - L Rear
#  4 - L Middle
#  5 - L Front 
legScheme = [ (0,1,2) , (6,7,8) , (15,16,17) , (12,13,14) , (9,10,11), (3,4,5)]

#  We only define 6 leg positions 
#  0 - Forward, Raised
#  1 - Mid, Raised
#  2 - Backward, Raised
#  3 - Forward, Lowered
#  4 - Mid, Lowered (this is the "normal" standing position)
#  5 - Backward, Lowered

# Tripod Gait  

def walking(Stop) :
 	#step 1 raise 3 leg (from backward position)
	while True :
		if Stop == True :
			print("hexapod Halted!")
			break

		gait(5 , 0) #(leg , leg sequence)
		# gait(1 , 0)
		# gait(3 , 0)
		print("sequence 0")
		sleep(1)
		# Step 2 - Moved raised legs forward and others backward
		gait(5 , 1) 
		# gait(1 , 1)
		# gait(3 , 1)
		print("sequence 1")
		sleep(1)
		gait(5 , 2) 
		# gait(1 , 2)
		# gait(3 , 2)
		sleep(1)
		# gait(4 , 0) 
		# gait(0 , 0)
		# print("sequence 2")
		# sleep(1)
		# gait(4 , 1) 
		# gait(0 , 1)
		# print("sequence 3")
		# sleep(1)
		# gait(4 , 2) 
		# gait(0 , 2)
		gait(5 , 0) 
		# gait(1 , 0)
		# gait(3 , 0)
		print("sequence 4")
		sleep(1)
		gait(5 , 3) 
		# gait(1 , 3)
		# gait(3 , 3)
		sleep(1)
		gait(5 , 2) 
		# gait(1 , 2)
		# gait(3 , 2)
		# gait(4 , 0) 
		# gait(0 , 0)
		print("sequence 5")
		sleep(1)
		# gait(4 , 3) 
		# gait(0 , 3)
		# sleep(1)
		# gait(4 , 2) 
		# gait(0 , 2)
		# sleep(1)


###############


def gait(Leg,ls) :
 	if ls == 0  :  #knee up
 		if Leg == 1 or Leg == 0 :
 			kit.servo[legScheme[Leg][1]].angle = init_position2[Leg][1] + UP	#knee
 		else :
 			kit.servo[legScheme[Leg][1]].angle = init_position2[Leg][1] - UP	#knee
 	elif ls == 1 :  # hip -forw
 		if Leg == 1 or Leg == 0 :
 			kit.servo[legScheme[Leg][0]].angle = init_position2[Leg][0] - FORWARD  	#hip
 		else :
 			kit.servo[legScheme[Leg][0]].angle = init_position2[Leg][0] + FORWARD  	#hip
 	elif ls == 2 :  # knee down
 		if Leg == 1 or Leg == 0 :
 			kit.servo[legScheme[Leg][1]].angle = init_position2[Leg][1] 	#knee
 		else :
 			kit.servo[legScheme[Leg][1]].angle = init_position2[Leg][1] 	#knee
 	elif ls == 3 :	#hip back
 		if Leg == 1 or Leg == 0:
 			kit.servo[legScheme[Leg][0]].angle = init_position2[Leg][0] + BACKWARD  	#hip
 		else :
 			kit.servo[legScheme[Leg][0]].angle = init_position2[Leg][0] - BACKWARD  	#hip








initialize()
walking()
sleep(5)
initialize()


for i in range(len(kit.servo)):
	print("i = " + str(i) +' '+ str(kit.servo[i].angle))

# try:
# 	while True :
# 		kit.servo[0].angle = 120
# 		kit.servo[1].angle = 180
# 		kit.servo[2].angle = 30
# 		kit.servo[3].angle = 19
# 		print("LBH =" + str(kit.servo[13].angle) + "LBK = " + str(kit.servo[14].angle) +"LBA = " + str(kit.servo[15].angle))
# 		sleep(0.5)
# 		print("df")
# 		kit.servo[0].angle = 15
# 		#kit.servo[14].angle = 0
# 		#kit.servo[15].angle = 130
# 		kit.servo[3].angle = 155
# 		print("LBH =" + str(kit.servo[13].angle) + "LBK = " + str(kit.servo[14].angle) +"LBA = " + str(kit.servo[15].angle))
# 		sleep(1)



# except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
#     print("Cleaning up!")
#     # for i in range(len(kit.servo)):
#     # 	kit.servo[i].angle = 0
#     # 	sleep(0.2)



