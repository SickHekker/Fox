import time, Robot, curses

LEFT_TRIM   = 0
RIGHT_TRIM  = 0


robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

speed = 100
turn = 100

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
		robot.stop()
            elif char == ord('w'):
                robot.forward(speed)
            elif char == ord('s'):
                robot.backward(speed)
            elif char == ord('d'):
                robot.right(turn)
            elif char == ord('a'):
                robot.left(turn)
            elif char == ord('e'):
                robot.stop()
 	    elif char == ord('1'):
		speed = 75
	    elif char == ord('2'):
		speed = 100
	    elif char == ord('3'):
		speed = 150
	    elif char == ord('4'):
		speed = 200
	    elif char == ord('5'):
		speed = 250
            elif char == ord('r'):
		turn = 75
	    elif char == ord('t'):
		turn = 100
	    elif char == ord('y'):
		turn = 150
		

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin() 

