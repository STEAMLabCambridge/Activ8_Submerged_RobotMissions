#Dropping Experts and Audience in different areas

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask

hub = PrimeHub()

class run4():
    
    def run(self, benny = DriveBase, left_attachment = Motor, right_attachment = Motor):
        print('Activ8')