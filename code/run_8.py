from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

class run8():
    
    def run(self, benny = DriveBase, left_attachment = Motor, right_attachment = Motor):
        benny.settings(straight_acceleration=600, straight_speed=600)
        benny.straight(600)
        benny.turn(-35)
        benny.straight(236) 
        right_attachment.run_angle(270,560)
        right_attachment.run_angle(270,-200)
        benny.straight(-170)
        benny.turn(-27)
        benny.straight(50)
        #right_attachment.run_angle(270,-120)
        #benny.settings(straight_acceleration=900, straight_speed=900)
        benny.straight(250)
        benny.turn(10)
        benny.straight(170)
        benny.turn(10)
        left_attachment.run_angle(250,200)
        wait(500)
        left_attachment.run_angle(270,-200)
        benny.settings(straight_acceleration=900, straight_speed=900)
        benny.straight(-260)
        benny.turn(-45)
        benny.straight(250)