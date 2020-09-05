Vince Espiritu <vespirit@usc.edu>
USC ID: 1472908880
Lab 3 Writeup

1.) How did the reliability of UDP change when you added 50% loss to your local environment? Why did this occur?
	ANSWER: It's been greatly reduced that it wasn't able to completely receive all the data that I have sent consecutively. This occurred because I was sending data too fast that it cannot processed the whole data quickly. Hence, it completely dropped the data since it cannot understand it or an error occurred. UDP can detect errors and data loss but it won't be able to recover the data loss.

2.) How did the reliability of TCP change? Why did this occur?
	ANSWER: The relaiability of TCP did not change but it's has slower response than before. The reliability didn't change because TCP can detect and recover data loss unlike UDP that can only detect errors and have no way to recover it. The slower response occurred because it's trying to recover the 50% of the data that has been lost.

3.) How did the speed of the TCP response change? Why might this happen?
	ANSWER: The speed of the TCP response has been cut to half because half of the data has been lost. Hence, the TCP spent time recovering that data loss.