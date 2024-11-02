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
        benny.straight(550) # heads straight to coral nursery
        benny.turn(90) # turn to face Kraken Treasure and Shipwreck 
        benny.straight(150) # drive halfway to shipwreck
        benny.settings(straight_acceleration=160, straight_speed=160) #changes settings
        benny.straight(130) # straight to shipwreck and collects treasure chest
        right_attachment.run_angle(600,-350) # collect krill
        benny.straight(-250) # goes back to coral nursery
        benny.settings(turn_acceleration=90,turn_rate=90) # changes settings
        benny.turn(-90) # turn to face home area
        benny.settings(straight_acceleration=700, straight_speed=650) # change settings
        benny.straight(-800) # return to home area
        
        #-------------------------------------
        # CODE END - 50 Points Secured
        #-------------------------------------