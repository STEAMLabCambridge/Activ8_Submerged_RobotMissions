from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task


#----------------------------------
#Masterpiece,Expert,Audience Member
#----------------------------------
class run1():
    
    def run(self, benny = DriveBase, left_attachment = Motor, right_attachment = Motor):
       benny.straight(-150)
       benny.turn(38)
       benny.straight(-549)
       left_attachment.run_angle(600,450)
       benny.turn(97)