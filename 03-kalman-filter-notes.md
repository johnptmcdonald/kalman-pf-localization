http://www.ilectureonline.com/lectures/subject/SPECIAL%20TOPICS/26/190/1962

Kalman filter is an iterative mathematical process that uses a set of equations and consecutive data inputs to quickly estimate the true value, position, velocity, etc. of the object being measured when the measured values contain unpredicted or random error/uncertainty. 

1 - Calculate the Kalman gain (the error or uncertainty).
	This takes two inputs, the uncertainty in the last estimate and the uncertainty we have in the incoming data. The kalman gain is a way of putting more weight on the data that has less uncertainty. 

2 - Calculate the current estimate.
	The Kalman gain is then used to calculate the current estimate from the previous estimate and the new, measured value. The kalman gain can put more weight on one or the other. This is the output that we use to show where the object is. 

3 - Calculate the new error in the estimate. 
	Use the kalman gain and the current estimate to calculate the new estimate's uncertainty. 


==========

More on item 1
The Kalman gain is simply the proportion of the total uncertainty that is accounted for by uncertainty in the current estimate

KG = 	E(est)
	   ----------
   	 E(est) + E(meas)


We use it thus:

new_estimate = old_estimate + KG(measurement - old_estimate)


i.e. a high Kalman gain means we put a lot of weight on the measurement (measurements are accurate, estimates are unstable). A low Kalman gain means we put a lot of weight on the old estimate (measurements are inaccurate, and estimates are stable). Over time the Kalman Gain typically gets smaller (as estimates move to the true value).









