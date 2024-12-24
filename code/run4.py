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
        benny.straight(550)
        benny.turn(25)
        benny.straight(70)
        #-------------------------------------
        # CODE END - 50 Points Secured
        #-------------------------------------