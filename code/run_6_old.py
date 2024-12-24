from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

class run6():
    
    def run(self, benny = DriveBase, left_attachment = Motor, right_attachment = Motor):
        
        benny.settings(straight_speed=800, straight_acceleration=800)
        benny.straight(380)
        benny.turn(45)
        benny.straight(70)
        right_attachment.run_angle(400,-360)
        benny.straight(-180)
        right_attachment.run_angle(800,160)
        benny.turn(-90)
        benny.settings(straight_speed=400, straight_acceleration=400)
        benny.straight(180)       
        benny.settings(straight_speed=900, straight_acceleration=900)
        benny.straight(-600, Stop.COAST)
        benny.settings(195,733,132,595)
