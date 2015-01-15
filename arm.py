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

    def connect(self):
        """
        Connects to the robot arm. This is called automatically -
        you don't need to call this function in your code.
        """
        self.dev = usb.core.find(idVendor=0x1267, idProduct=0x0)
        if self.dev == None:
            raise ValueError("Could not connect to robot arm")
        
        if self.dev.is_kernel_driver_active(0) is True:
            print "but we need to detach kernel driver"
            self.dev.detach_kernel_driver(0)
            print "claiming device"
            usb.util.claim_interface(self.dev, 0)
            print "release claimed interface"

        usb.util.release_interface(self.dev, 0)
        print 'Now reading data'
        #dev.attach_kernel_driver(0)
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
        @param light_status: Boolean. True to turn the LED on
        """
        self.check_connection()
        if light_status:
            self.led_state = 1
        else:
            self.led_state = 0

        self.dev.ctrl_transfer(0x40, 0x6, 0x100, 0, [0, 0, self.led_state], 0)

    def grip(self, direction, time_ms):
        """
        Moves the robot arm
        """
        self.check_connection()
        if direction:
                self.grip_state = 2
        else:
                self.grip_state = 1
        self.dev.ctrl_transfer(0x40, 0x6, 0x100, 0, [self.grip_state, 0, self.led_state], 0)
        time.sleep(time_ms / 1000.0)
        self.stop()
        
    def stop(self):
        """
        Stops moving the robot arm
        """
        self.check_connection()
        self.dev.ctrl_transfer(0x40, 0x6, 0x100, 0, [0, 0, 0], 0)



