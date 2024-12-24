from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task

hub = PrimeHub()

class run6():
    
    def run(self, benny = DriveBase, left_attachment = Motor, right_attachment = Motor):
        
        benny.settings(straight_speed=800, straight_acceleration=800)
        right_attachment.run_angle(400,-180)
        benny.straight(245)
        left_attachment.run_angle(400,-75)
        benny.settings(straight_speed=500, straight_acceleration=800)
        left_attachment.run_angle(400,-100)

        async def forward_artificial():
            await multitask(left_attachment.run_angle(900,-400),benny.straight(500))

        run_task(forward_artificial())