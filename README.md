robo-arm-pi
===========

USB Robotic Arm Interface for Raspberry Pi (in C++)

Created 17th March 2013 by Pete Dring

This project is designed to allow teachers and students to control a robotic arm using a raspberry pi.

The Robotic Arm in question is: http://www.maplin.co.uk/robotic-arm-kit-with-usb-pc-interface-266257. (cost £44.99 at time of writing)

Also available from http://www.owirobot.com/robotic-arm-edge-1/ with a manual controlled and the USB interface sold separately.

This project uses the research posted on http://notbrainsurgery.livejournal.com/38622.html
to create a control interface in C++ that can be used in other programs to control the robot arm with a raspberry pi.

This project includes a library in C++ and a test program that allows the robot arm to be controlled using the keyboard.

To get the code type:
   git clone git://github.com/pddring/robo-arm-pi.git
   
Before you can compile the source, you will need to install certain dependencies:
   sudo apt-get install libusb-dev ncurses-dev build-essential

To compile the source code type:
   make
   
To run the sample program type:
   ./robot
   
The default user on a raspberry pi does not have user access to send data down a USB port so you may have to type:
   sudo ./robot





