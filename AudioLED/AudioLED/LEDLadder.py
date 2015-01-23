from time import sleep
import RPi.GPIO as GPIO
import ptvsd

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)
GPIO.setup(22, GPIO.IN)

#GPIO.setup(11, GPIO.OUT)
#GPIO.setup(13, GPIO.OUT)
#GPIO.setup(15, GPIO.OUT)
#GPIO.output(11, GPIO.LOW)
#GPIO.output(13, GPIO.LOW)
#GPIO.output(15, GPIO.LOW)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.LOW)


# state - decides what LED should be on and off
state = 0

# increment - the direction of states
inc = 1

try:
    while True:

	    # state toggle button is pressed
        if ( GPIO.input(17) == True ):

            if (inc == 1):
                state = state + 1;
            else:
                state = state - 1;

            # reached the max state, time to go back (decrement)
            if (state == 4):
                inc = 0
            # reached the min state, go back up (increment)
            elif (state == 0):
                inc = 1

            if (state == 1):
                GPIO.output(18, GPIO.HIGH)
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)
            elif (state == 2):
                GPIO.output(18, GPIO.HIGH)
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)
            elif (state == 3):
                GPIO.output(18, GPIO.HIGH)
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(24, GPIO.HIGH)
                GPIO.output(25, GPIO.LOW)
            elif (state == 4):
                GPIO.output(18, GPIO.HIGH)
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(24, GPIO.HIGH)
                GPIO.output(25, GPIO.HIGH)
            else:
                GPIO.output(18, GPIO.LOW)
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)
            print("pressed B1 ", state)

        # reset button is pressed
        if ( GPIO.input(22) == True ):

            state = 0
            inc = 1
            GPIO.output(18, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)

            print("pressed B2 ", state)

        sleep(0.2);

except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  

GPIO.cleanup()           # clean up GPIO on normal exit  
