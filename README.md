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
   <code>git clone git://github.com/pddring/robo-arm-pi.git</code>
   
Before you can compile the source, you will need to install certain dependencies:
   <code>sudo apt-get install libusb-dev ncurses-dev build-essential</code>
apt-get lets you install extra programs or libraries and the sudo command is needed to run the apt-get command with elevated security privileges.

The libusb library is essential for controlling the robot arm over the USB interface. The ncurses-dev is used for the sample progra (it lets you detect individual key presses) and the build-essentials gives you the tools to compile the program if you've not already got them.
If you are in a school with a network filter, you may need to set up apt-get to work behind your school proxy. At my school, this can be done by using ntlmaps (http://ntlmaps.sourceforge.net/) and then changing the apt settings (http://www.unixmen.com/apt-get-behind-a-proxy/)   

To compile the source code type:
   <code>make</code>
   
To run the sample program type:
   <code>./robot</code>
   
The default user on a raspberry pi does not have user access to send data down a USB port so you may have to type:
   <code>sudo ./robot</code>
   
You should then be able to control the robot arm using the keyboard controls on screen.
The sample program is designed so that you left hand is oved the WSX/CDE/VFR keys and your right hand is over the IOP/KL; keys and your thumbs are over the space





