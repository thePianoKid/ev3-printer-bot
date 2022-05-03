#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


ev3 = EV3Brick()
drive = Motor(Port.C)
SPEED = 100


# Helper functions
def moveForward(rot):
    """Moves the robot forward

    Parameter
    ---------
    rot (float): number of cycles the motor completes

    Returns
    -------
    null
    """
    deg = rot * -360 # convert rotations to degrees
    drive.run_target(SPEED, deg, Stop.BRAKE)


# Write your program here.
moveForward(0.5)