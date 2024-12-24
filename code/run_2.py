#####################################################
###Title:- Submerged season Run 2
###Description:- Coral Nursery and Coral Scuba Diver  and Shark collecting
###Author Siddharth, Saketh
###Changelog :- V.1 Intial version
######################################################
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

class run2():
    
    def run(self, benny = DriveBase, left_attachment = Motor, right_attachment = Motor):
        benny.settings(straight_acceleration=800, straight_speed=800)
        benny.settings(turn_acceleration=300, turn_rate=300)
        benny.straight(200) # Straight to  nursery
        benny.turn(25)# Turn towards coral reef to avoid hitting coral nursery
        benny.straight(570)# Move towards coral nursery
        benny.turn(-110) #turn towards coral nursery
        benny.settings(straight_acceleration=200, straight_speed=200)
        left_attachment.run_angle(600,250) #let the attachment fall for coral tree picking
        benny.straight(165) # move towards the nursery 
        wait(200)
        right_attachment.run_angle(600,-300)# lowers attachment to release the shark 
        right_attachment.run_angle(600,250)# lift the attachement to lift the tree
        left_attachment.run_angle(900,-220) # same repeat
        benny.settings(straight_acceleration=900, straight_speed=900)
        benny.straight(-200) # go back straight 
        benny.turn(-60) # turn to go home
        benny.straight(600, Stop.COAST) # forward to home
        benny.settings(195,733,132,595)
