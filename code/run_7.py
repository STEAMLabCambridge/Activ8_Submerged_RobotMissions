from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

class run7():
    
    def run(self, benny = DriveBase, left_attachment = Motor, right_attachment = Motor):
        benny.settings(straight_acceleration=300, straight_speed=800)
        right_attachment.run_angle(600,-30)
        benny.straight(450)
        right_attachment.run_angle(900,-1015)
        benny.straight(310)
        benny.turn(45)
        benny.settings(straight_acceleration=400, straight_speed=400)
        benny.straight(130)
        left_attachment.run_angle(100,-35)
        wait(1000)
        #left_attachment.run_angle(600,50)
        benny.settings(straight_acceleration=800, straight_speed=800)
        benny.straight(-200)
        benny.turn(-60)
        benny.settings(straight_acceleration=900, straight_speed=900)
        benny.straight(-900, Stop.COAST)
        benny.settings(195,733,132,595)


        

        