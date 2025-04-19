from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task

from run_1 import run1
from run_2 import run2
from run_3 import run3
from run_4 import run4
from run_5 import run5
from run_6 import run6
from run_7 import run7
from run_8 import run8
#from run_9 import run9

#Create hub object for PrimeHub 

hub = PrimeHub()
#------------------------------------------------------------------
# Setup the robot 
# Step 1 - Set up the drive base 
# Step 2 - Set up  the front and back motors 
# Step 3 - Set up the left and right color sensors in the front
#---------------------------------------------------------------------

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A)

# Initialize the drive base. 
# In our robot, the wheel diameter is 88mm.
# The distance between the two wheel-ground contact points is 145mm.
benny = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=141)
# Optionally, uncomment the line below to use the gyro for improved accuracy.
benny.use_gyro(True)

#Initialize the front abnd back motors 
left_attachment = Motor(Port.D)
right_attachment = Motor(Port.C)

# Initialize the color sensors.
right_sensor = ColorSensor(Port.F)
left_sensor = ColorSensor(Port.E)
#Create the instances of each run 
run1 = run1()
run2 = run2()
run3 = run3()
run4 = run4()
run5 = run5()
run6 = run6()
run7 = run7()
run8 = run8() 
#run9 = run9()
# Let's offer these menu options. You can add as many as you like.
menu_options = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
menu_index = 0

while True:

    # Normally, the center button stops the program. But we want to use the
    # center button for our menu. So we can disable the stop button.
    hub.system.set_stop_button(None)

    while True:

        hub.display.char(menu_options[menu_index])

        # Wait for any button.
        pressed = ()
        while not pressed:
            pressed = hub.buttons.pressed()
            wait(10)
        
        # Wait for the button to be released.
        while hub.buttons.pressed():
            wait(10)

        # Now check which button was pressed.
        if Button.CENTER in pressed:
            # Center button, so the menu is done!
            break
        elif Button.LEFT in pressed:
            # Left button, so decrement menu menu_index.
            menu_index = (menu_index - 1) % len(menu_options)
        elif Button.RIGHT in pressed:
            # Right button, so increment menu menu_index.
            menu_index = (menu_index + 1) % len(menu_options)
        

    # Now we want to use the Center button as the stop button again.
    hub.system.set_stop_button(Button.CENTER)

    # Based on the selection, choose a program.
    selected = menu_options[menu_index]
    if selected == "1":
        run1.run(benny, left_attachment, right_attachment) 
        menu_index = 1 # increase the menu index to point to next program
    elif selected == "2":
        run2.run(benny, left_attachment, right_attachment)
        menu_index = 2
    elif selected == "3":
        run3.run(benny, left_attachment, right_attachment)
        menu_index = 3
    elif selected == "4":
        run4.run(benny, left_attachment, right_attachment)
        menu_index = 4
    elif selected == "5":
        run5.run(benny, left_attachment,right_attachment)
        menu_index = 5
    elif selected == "6":
        run6.run(benny, left_attachment, right_attachment)
        menu_index = 6
    elif selected == "7":
        run7.run(benny, left_attachment, right_attachment)
        menu_index = 7
    elif selected == "8":
        run8.run(benny, left_attachment, right_attachment)
        menu_index = 8
        break
    #elif selected == "9":
     #   run9.run(benny, left_attachment, right_attachment)
       # menu_index = 9
      #  break 
