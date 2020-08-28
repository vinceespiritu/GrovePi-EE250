Name:  Vince Espiritu
Email: vespirit@usc.edu
USCID: 1472908880
Lab 2 Reflection Answers

1.)	 git clone git@github.com:my-name/my-imaginary-repo.git
	 touch my_second_file.py
	 git add my_second_file.py
	 git commit -m "update"
	 git push

2.) At first, I was editing my files on my VM then pushing it to Github to access it on my RPi. However, I got tired of the process so I just directly edit my files on my RPi using VIM. I was trying to install sublime on my RPi but for some reason it's not compatible with RPi. For the next lab, I would try to find a text editor that would allow me to edit several files at a time like in MS Visual Studio Code.

3.) The function ultrasonicRead has a 60ms delay to satisfy the wait time for the firmware to finish,which is 50ms. The RPi uses the I2C protocol to communicate on the GrovePi when it tries to read the ultrasonic ranger output using the 'grovepi' library. 
