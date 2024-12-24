#####################################################
###Title:- Submerged season Run 3
###Description:- Kraken's treasure chest, Raising the mast and krill
###Author Yuteng, Saketh, Siddarth
###Changelog :- V.1 Intial version
######################################################
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task

class run3():
#------------------------------------------
# Code for the robot
#------------------------------------------
    def run(self, benny = DriveBase, left_attachment = Motor, right_attachment = Motor):
        print(benny.settings())
        benny.settings(straight_acceleration=600, straight_speed=600) #changes settings
        benny.straight(558) # heads straight to coral nursery
        benny.turn(90) # turn to face Kraken Treasure and Shipwreck 
        benny.straight(150) # drive halfway to shipwreck
        benny.settings(straight_acceleration=100, straight_speed=200) #changes settings
        benny.straight(100) # straight to shipwreck and collects treasure chest
        right_attachment.run_angle(600,225) # collect krill
        benny.straight(-250) # goes back to coral nursery
        benny.settings(turn_acceleration=90,turn_rate=90) # changes settings
        benny.turn(110) # turn to face home area
        benny.settings(straight_acceleration=600, straight_speed=600) #changes settings
        benny.straight(350,Stop.COAST) # return to home area
        benny.settings(195,733,132,595)

        
        #-------------------------------------
        # CODE END - 50 Points Secured
        #-------------------------------------