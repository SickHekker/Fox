# Made by: SickHekker

import time, Robot, curses

LEFT_TRIM   = 0
RIGHT_TRIM  = 0


robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

# Default speeds for when the program starts
speed = 100
turn = 100

try:
        while True:   
            char = screen.getch()
	# Pressing Q stops the robot and returns you to the commandline
            if char == ord('q'):
                break
		robot.stop()
	# If you press W will keep driving forward until you press E to stop it
            elif char == ord('w'):
                robot.forward(speed)
	# If you press S will keep driving forward until you press E to stop it
		elif char == ord('s'):
                robot.backward(speed)
	# If you press D will keep rotating to the right until you press E to stop it
            elif char == ord('d'):
                robot.right(turn)
	# If you press A will keep turning left until you press E to stop it
            elif char == ord('a'):
                robot.left(turn)
	# If you press E you stop the tank
            elif char == ord('e'):
                robot.stop()
	# Setting speeds for rotation
 	    elif char == ord('1'):
		speed = 50
	    elif char == ord('2'):
		speed = 100
	    elif char == ord('3'):
		speed = 150
	    elif char == ord('4'):
		speed = 200
	    elif char == ord('5'):
		speed = 255
            elif char == ord('r'):
		turn = 50
	    elif char == ord('t'):
		turn = 100
	    elif char == ord('y'):
		turn = 150
		

finally:
    #Close down curses
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin() 

