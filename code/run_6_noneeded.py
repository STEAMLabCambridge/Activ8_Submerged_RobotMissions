from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

class run6():
    
    def run(self, benny = DriveBase, left_attachment = Motor, right_attachment = Motor):
        #for i in range(1):
        benny.settings(straight_acceleration=400, straight_speed=400)
        benny.straight(170)
        right_attachment.run_angle(500,-125)
        benny.settings(straight_acceleration=700, straight_speed=700)
        benny.straight(550)
        benny.straight(-75)
        right_attachment.run_angle(500,150)
        benny.straight(-175)
        benny.curve(100,55)
        benny.curve(100,-45)
        benny.straight(450)
        left_attachment.run_angle(200,50)
        left_attachment.run_angle(200,50)
        benny.settings(straight_acceleration=400, straight_speed=400)
        benny.straight(-200)
        benny.turn(-90)
        benny.straight(-50)
        benny.straight(305)
        benny.turn(90)
        benny.settings(straight_acceleration=200, straight_speed=200)
        benny.straight(750)
        benny.turn(45)
        benny.straight(-600)
        benny.turn(20)
        benny.straight(1000)
        benny.settings(195,733,132,595)

        
        