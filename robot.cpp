#include <stdlib.h>
#include <stdio.h>
#include <curses.h>
#include "robotarm.h"


int main(void) {
	try {
		initscr();
		timeout(-1);
		
		printf("Robot arm interface by P. Dring\n");
		
		printf("Grip commands: i, o, p\n\r");
		printf("Base commands: k, l, ;\n\r");
		printf("Wrist commands: w, s, x\n\r");
		printf("Elbow commands: e, d, c\n\r");
		printf("Shoulder commands: r, f, v\n\r");
		printf("Toggle LED: space\n\r");
		printf("Quit: q\n\r");
		
		
		RobotArm roboarm;
		
		roboarm.connect();
		bool LED = false;
		bool running = true;
		while(running) {
			int key = getch();
			switch(key) {
				// grip
				case 'i': roboarm.setGrip(RobotArm::ARM_OPEN); break;
				case 'o': roboarm.setGrip(RobotArm::ARM_STOP); break;
				case 'p': roboarm.setGrip(RobotArm::ARM_CLOSE); break;
				
				// base
				case 'k': roboarm.setBase(RobotArm::ARM_ANTICLOCKWISE); break;
				case 'l': roboarm.setBase(RobotArm::ARM_STOP); break;
				case ';': roboarm.setBase(RobotArm::ARM_CLOCKWISE); break;
				
				// wrist
				case 'w': roboarm.setWrist(RobotArm::ARM_UP); break;
				case 's': roboarm.setWrist(RobotArm::ARM_STOP); break;
				case 'x': roboarm.setWrist(RobotArm::ARM_DOWN); break;
				
				// elbow
				case 'e': roboarm.setElbow(RobotArm::ARM_UP); break;
				case 'd': roboarm.setElbow(RobotArm::ARM_STOP); break;
				case 'c': roboarm.setElbow(RobotArm::ARM_DOWN); break;
				
				// shoulder
				case 'r': roboarm.setShoulder(RobotArm::ARM_UP); break;
				case 'f': roboarm.setShoulder(RobotArm::ARM_STOP); break;
				case 'v': roboarm.setShoulder(RobotArm::ARM_DOWN); break;
				
				// LED
				case ' ': roboarm.setLED(LED = !LED); break;
				
				// quit
				case 'q': roboarm.stopAll(); running = false; break;
			}
		}
		
		
		
		roboarm.stopAll();
		
		roboarm.disconnect();
		endwin();
		
	} catch(const char * message) {
		endwin();
		printf("%s\n\r", message);
	}
	
	return 0;
}
