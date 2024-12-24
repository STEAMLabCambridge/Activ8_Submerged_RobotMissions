#####################################################
###Title:- Submerged season Run 4
###Description:- scuba hanging
###Author Siddharth, Saketh
###Changelog :- V.1 Intial version
######################################################
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task

class run4 ():
#------------------------------------------
# Code for the robot
#------------------------------------------
    def run(self, benny = DriveBase, left_attachment = Motor, right_attachment = Motor):
        print(benny.settings())
        
        benny.settings(straight_acceleration=500, straight_speed=500)
        benny.straight(500)
        benny.turn(45)
        benny.straight(270)
        benny.turn(-45)
        benny.settings(straight_acceleration=800, straight_speed=800)
        benny.straight(140)
        right_attachment.run_angle(600,-150)
        left_attachment.run_angle(400,150)
        benny.settings(straight_acceleration=900, straight_speed=900)
        benny.straight(-160)
        benny.turn(45)
        benny.settings(straight_acceleration=900, straight_speed=900)
        benny.straight(-800, Stop.COAST)     
        
        #-------------------------------------
        # CODE END - 50 Points Secured
        #-------------------------------------