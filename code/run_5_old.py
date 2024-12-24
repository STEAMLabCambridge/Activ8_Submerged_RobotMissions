#####################################################
###Title:- Submerged season Run 5
###Description:- research vessel
###Author Vihaan
###Changelog :- V.1 Intial version
######################################################
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task

hub = PrimeHub()

class run5():
    
    def run(self, benny = DriveBase, left_attachment = Motor, right_attachment = Motor):
        benny.straight(200)
        benny.turn(-45)
        benny.straight(355)
        benny.turn(-45)
        benny.straight(305)
        benny.turn(60)
       
        benny.straight(180)
        benny.straight(-400)
        benny.turn(75)
        left_attachment.run_angle(300,350)
        benny.straight(300)
        left_attachment.run_angle(300,-350)
        benny.settings(195,733,132,595)
