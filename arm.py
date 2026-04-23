"""
USB robot arm API
Written by P. Dring and J. Doyle


Usage:

# import the arm module
from arm import Arm

# connect to the USB Arm module
arm = Arm()

# turn led on
arm.set_led(True)

# changes the grip
arm.grip(True, 200)

# turn led off
arm.set_led(False)
"""
import usb.core
import time

class Arm:
    """
    USB Robot Arm class
    """

    dev = None

    led_state = 0
    grip_state = 0

    STOP = 0
    OPEN = 2
    CLOSE = 1
    UP = 1
    DOWN = 2
    CLOCKWISE = 1
    ANTICLOCKWISE = 2
    OFF = 0
    ON = 1

    def __init__(self):
         self.commands = [0,0,0]
         """
         Byte 1:
            Bit: 		Function:
            0-1			Grip (00 stop, 01 close, 10 open)
            2-3			Wrist (00 stop, 01 up, 10 down)
            4-5			Elbow (00 stop, 01 up, 10 down)
            6-7			Shoulder (00 stop, 01 up, 10 down)
            
         Byte 2: 
            0-1			Base (00 stop, 01 clockwise, 10 anti clockwise)
            
         Byte 3:
            0			LED (0 off, 1 on)
            """
    def send_command(self):
        """
        Send a command to the robot arm. This is called automatically"""
        self.check_connection()
        self.dev.ctrl_transfer(0x40, 0x6, 0x100, 0, self.commands, 0)
                 
    def connect(self):
        """
        Connects to the robot arm. This is called automatically -
        you don't need to call this function in your code.
        """
        self.dev = usb.core.find(idVendor=0x1267, idProduct=0x0)
        if self.dev == None:
            raise ValueError("Could not connect to robot arm")
        
        if self.dev.is_kernel_driver_active(0) is True:
            print("but we need to detach kernel driver")
            self.dev.detach_kernel_driver(0)
            print("claiming device")
            usb.util.claim_interface(self.dev, 0)
            print("release claimed interface")

        usb.util.release_interface(self.dev, 0)
        self.dev.set_configuration()

    def check_connection(self):
        """
        Establishes a usb connection to the robot arm if
        one hasn't already been established
        """
        if self.dev == None:
            self.connect()

    def set_led(self, light_status):
        """
        Turns the LED on or off
        @param light_status: ON or OFF
        """
        self.commands[2] = light_status & 0x3
        self.send_command()

    def grip(self, direction=OPEN, time_ms=0):
        """
        Opens or closes the gripper
        @param direction: OPEN or CLOSE
        @param time_ms: how long to move the gripper for (in milliseconds). If 0, the gripper will move until stop() is called.
        """
        self.commands[0] = (direction & 0b00000011) | (self.commands[0] & 0b11111100)
        self.send_command()

        if time_ms > 0:
            time.sleep(time_ms / 1000.0)
            self.stop()

    def wrist(self, direction=UP, time_ms=0):
        """
        Moves the wrist up or down
        @param direction: UP or DOWN
        @param time_ms: how long to move the wrist for (in milliseconds). If 0, the wrist will move until stop() is called.
        """
        self.commands[0] = ((direction & 0b00000011) << 2) | (self.commands[0] & 0b11110011)
        self.send_command()

        if time_ms > 0:
            time.sleep(time_ms / 1000.0)
            self.stop()

    def elbow(self, direction=UP, time_ms=0):
        """
        Moves the elbow up or down
        @param direction: UP or DOWN
        @param time_ms: how long to move the elbow for (in milliseconds). If 0, the elbow will move until stop() is called.
        """
        self.commands[0] = ((direction & 0b00000011) << 4) | (self.commands[0] & 0b11001111)
        self.send_command()

        if time_ms > 0:
            time.sleep(time_ms / 1000.0)
            self.stop()

    def shoulder(self, direction=UP, time_ms=0):
        """
        Moves the shoulder up or down
        @param direction: UP or DOWN
        @param time_ms: how long to move the shoulder for (in milliseconds). If 0, the shoulder will move until stop() is called.
        """
        self.commands[0] = ((direction & 0b00000011) << 6) | (self.commands[0] & 0b00111111)
        self.send_command()

        if time_ms > 0:
            time.sleep(time_ms / 1000.0)
            self.stop()

    def base(self, direction=CLOCKWISE, time_ms=0):
        """
        Moves the base clockwise or anti-clockwise
        @param direction: CLOCKWISE or ANTICLOCKWISE
        @param time_ms: how long to move the base for (in milliseconds). If 0, the base will move until stop() is called.
        """
        self.commands[1] = (direction & 0b00000011) | (self.commands[1] & 0b11111100)
        self.send_command()

        if time_ms > 0:
            time.sleep(time_ms / 1000.0)
            self.stop()
        
    def stop(self):
        """
        Stops moving the robot arm. Leaves the LED unchanged
        """
        self.commands[0] = 0
        self.commands[1] = 0
        self.send_command()



if __name__ == "__main__":
    # connect to the USB Arm module
    arm = Arm()

    # turn led on
    arm.set_led(Arm.ON)

    # changes the grip
    arm.grip(Arm.OPEN, 500)
    arm.grip(Arm.CLOSE, 500)

    # turn led off
    arm.set_led(Arm.OFF)

    arm.base(Arm.CLOCKWISE, 500)
    arm.base(Arm.ANTICLOCKWISE, 500)
    arm.set_led(Arm.ON)

    arm.shoulder(Arm.UP, 500)
    arm.shoulder(Arm.DOWN, 500)
    arm.set_led(Arm.OFF)

    arm.elbow(Arm.UP, 500)
    arm.elbow(Arm.DOWN, 500)
    arm.set_led(Arm.ON)

    arm.wrist(Arm.UP, 500)
    arm.wrist(Arm.DOWN, 500)
    arm.set_led(Arm.OFF)



