from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
#Initialisae the robot 
# Step 1 - Initialize the drive base 
# Step 2 - Initialize the front and right motors 
# Step 3 - Initialize the left and right color sensors in the front
#---------------------------------------------------------------------

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A)

# Initialize the drive base. 
# In our robot, the wheel diameter is 88mm.
# The distance between the two wheel-ground contact points is 145mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=97)
# Use the gyro for improved accuracy.
drive_base.use_gyro(True)

#Initialize the front and back motors 
front_motor = Motor(Port.D)
back_motor = Motor(Port.C)

# Initialize the color sensors.
right_sensor = ColorSensor(Port.F)
left_sensor = ColorSensor(Port.E)


# drive_base.settings(straight_speed=600,straight_acceleration=500)

# Code for Mission 15 Research Vessel

for i in range(1):
    drive_base.straight(170)
    benny.run_angle(500,-150)
    benny.straight(550)
    benny.straight(-75)
    benny.run_angle(500,150)
    benny.straight(-200)
    benny.curve(100,55)
    benny.curve(100,-45)
    benny.straight(350)
    benny.straight(-350)
    benny.curve(-100,-45)
    benny.straight(-50)
    benny.curve(-100,45)
    benny.straight(-500)

# End of boat delivery

