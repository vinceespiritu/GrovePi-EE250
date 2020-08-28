""" EE 250L Lab 02: GrovePi Sensors

List team members here.
Vince Espiritu

Insert Github repository link here.
https://github.com/vinceespiritu/GrovePi-EE250/tree/master/ee250/lab02
"""
"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 4    # D4
    pot = 0		#A0

    setText("Start Measurement")
    setRGB(0,128,64)
    setText(" ")
    buf=" "

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        pot_value = grovepi.analogRead(pot)
        read = grovepi.ultrasonicRead(PORT)


        if(read<pot_value):
            buf = " OBJ PRES"
            setRGB(255,0,0)
        else:
            buf= " "
            setRGB(0,255,0)

        setText_norefresh("{:<6} {:>9}\n{:<6}".format(str(pot_value)+"cm",buf,str(read)+"cm"))

