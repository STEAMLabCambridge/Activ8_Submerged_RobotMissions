######################################################
###Title:- Submerged season Run 1 
###Description:- Collect samples, Krill, Angler Fish
###Author Siddharth 
###Changelog :- V.1 Intial version
######################################################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask

hub = PrimeHub()

class run1():
    
    def run(self, benny = DriveBase, left_attachment = Motor, right_attachment = Motor):
        print(benny.settings())
        print(benny.state())
        benny.settings(turn_acceleration=100, turn_rate=100)

        right_attachment.run_angle(900,-900)# Move linear actuator left to avoid hitting shipping lanes
        benny.settings(straight_speed=500, straight_acceleration=500)
        benny.straight(600)#670 # Initial straight##
        benny.settings(turn_acceleration=200, turn_rate=200)

        benny.turn(20) #8 # turn before picking up the plankton
        benny.straight(145) ##95 straight turn before picking up the plankton
        right_attachment.run_angle(900,550)# run the linear actuator to right to pick plankton
        right_attachment.run_angle(900,-650)# run the linear actuator to left after picking plankton
       
        benny.turn(-107) ##98 turn before the sonar discovery
        benny.straight(450)#670 # go straight
        #right_attachment.run_angle(900,200) # 
        
        #benny.turn(5)
        ##benny.straight(250) # once out go straight to angler fish so jbeam hits the angler fish
        #right_attachment.run_angle(900,230) # move linear actuator to left to push angler fish
        benny.turn(-10)
        benny.straight(210) # move forward to push the angle fish 

        #benny.straight(50)# go straight to make sure the jbeam fully get the angler fish
        benny.straight(-50)# move back to go to the seabed sample
        benny.turn(10)# turn right to the seabed sample
        benny.straight(110) # now move towards seabed sample
        right_attachment.run_angle(900,150) # extend the arm to get in the circle of thesample 
        benny.straight(150) # move forwards to lift the sample directly
        right_attachment.run_angle(600,160)## 
        #benny.turn(-26)
        #benny.straight(-100)
        benny.straight(120)
        right_attachment.run_angle(600,-340) ## Picking up all thr krills and coral
        benny.straight(200)
        benny.turn(-56) ## added this to navigate around the two mission  - nursery and shipwrek
       # right_attachment.run_angle(600,-250)##
        benny.settings(straight_acceleration=900, straight_speed=900) # change settings
        benny.straight(680, Stop.COAST) # go  to left launch area
        benny.settings(195,733,132,595)


       
