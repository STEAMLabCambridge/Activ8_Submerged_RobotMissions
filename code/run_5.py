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

        benny.settings(straight_acceleration=600, straight_speed=600)
        benny.straight(220)
        right_attachment.run_angle(500,-170)
        benny.straight(760)
        right_attachment.run_angle(500,210)
        wait(100)
        benny.settings(straight_acceleration=100, straight_speed=100)
        benny.straight(-380)
        benny.settings(straight_acceleration=600, straight_speed=600)
        left_attachment.run_angle(600,250)
        benny.turn(-35)
        benny.straight(260)
        benny.settings(straight_acceleration=400, straight_speed=600)

        benny.straight(-230)
        benny.turn(10)
        benny.settings(straight_acceleration=800, straight_speed=800)
        benny.straight(400)
        benny.turn(32)
        benny.straight(510)
        #benny.turn(50)
        #benny.straight(-300)
        #benny.turn(-15)
        benny.straight(400, Stop.COAST)

        benny.settings(195,733,132,595)
