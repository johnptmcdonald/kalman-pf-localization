http://www.ilectureonline.com/lectures/subject/SPECIAL%20TOPICS/26/190/1962

Kalman filter is an iterative mathematical process that uses a set of equations and consecutive data inputs to quickly estimate the true value, position, velocity, etc. of the object being measured when the measured values contain unpredicted or random error/uncertainty. 

#1 - Calculate the Kalman gain (the error or uncertainty).
	This takes two inputs, the uncertainty in the last estimate and the uncertainty we have in the incoming data. The kalman gain is a way of putting more weight on the data that has less uncertainty. 

#2 - Calculate the current estimate.
	The Kalman gain is then used to calculate the current estimate from the previous estimate and the new, measured value. The kalman gain can put more weight on one or the other. This is the output that we use to show where the object is. 

#3 - Calculate the new error in the estimate. 
	Use the kalman gain and the current estimate to calculate the new estimate's uncertainty. 


==========

#More on item 1 - Calculate the Kalman gain
The Kalman gain is simply the proportion of the total uncertainty that is accounted for by uncertainty in the current estimate

KG = 	E(est)
	   ----------
   	 E(est) + E(meas)


#More on item 2 - Calculate the current estimate
We use the Kalman Gain in step 2 like this:

new_estimate = old_estimate + KG(measurement - old_estimate)


i.e. a high Kalman gain means we put a lot of weight on the measurement (measurements are accurate, estimates are unstable). A low Kalman gain means we put a lot of weight on the old estimate (measurements are inaccurate, and estimates are stable). Over time the Kalman Gain typically gets smaller (as estimates move to the true value).

#More on item 3 - Calculate the new error in the estimate

new_E(est) = (1 - KG) * old_E(est)

The new uncertainty in the estimate is the same as the old uncertainty reduced by a factor of how certain we are of the measurement we just made. i.e. if KG is high (we trust measurements) then we multiply the old error estimate by a very small number, so the new error estimate will be very small. 


==================

#Matrix format of the Kalman Filter

##The state matrix
The state matrix represents the current state. In the 1D model it has x-position and x-velocity.

X<sub>k</sub> = AX<sub>k-1</sub> + BU<sub>k</sub> + w<sub>k</sub>

X(k) = AX(k-1) + BU(k) + w(k)

(where 
	X = state matrix
	U = control variable matrix
	w = process noise
	A, B = transition matrices
)

i.e. The state matrix X at time k is equal to the previous state matrix multiplied by A (plus a control variable matrix U * B, plus noise w)

A and B are just transition matrices that correspond to the physical laws of how velocity/acceleration affect the state matrix.

Typically, position and velocity are kept in the state matrix, while acceleration is considered an external influence on the state, so is stuck into the U matrix. 

http://www.ilectureonline.com/lectures/subject/SPECIAL%20TOPICS/26/190/1971 


##The measurement

Y<sub>k</sub> = CX<sub>k</sub> + Z<sub>k</sub>

Y(k) = CX(k) + Z(k)

(where
	Y = observation
	X = state matrix
	C = observation transition matrix
)

C is how we extract the observables from the state matrix.

================
#The covariance matrices
P is the state covariance matrice (the error in the estimate)

Q is the process noise covariance matrice (errors in the process, e.g. not taking wind into account). This keeps the state covariance matrix from becoming too small.

R is the measurement covariance matrix (the error in the measurement).

P<sub>k</sub> = AP<sub>k-1</sub>A<sup>T</sup> + Q

K<sub>k</sub> = (P<sub>k</sub>H<sup>T</sup>)/(HP<sub>k</sub>H<sup>T</sup> + R)

i.e. the kalman gain is the same as it is above. 

##What is a covariance matrix?
[
	x-variance,     x-y-covariance,
	y-x-covariance, y-variance
]

where x-y-covariance is the same as the y-x-covariance. 

===========

#1D (x, x_dot) matrix example

##1 - make prediction based on initial estimates
X<sub>k</sub> = AX<sub>k-1</sub> + BU<sub>k</sub> + w<sub>k</sub>

http://www.ilectureonline.com/lectures/subject/SPECIAL%20TOPICS/26/190/1975

(where
	X<sub>k</sub> = predicted state at time k
	X<sub>k-1</sub> = previous state (at time k-1)	
	A = matrix that allows us to make an estimate from the previous state based on kinematic equations
	U = control variable matrix (external factors)
	B = matrix that allows us to make an estimate from the U based on kinematic equations
	w = process noise (noise in the process of making estimates)
)

##2 - Calculate initial process covariance matrix 
In the process we have some errors in the calculation. If x error is 20m and x_dot error is 5m/s, process covariance matrix P is:
[
	400, 100
	100, 25
]


We often set the covariances to zero, i.e.

[
	400, 0
	0,   25
]

##3 - Calculate predicted process covariance matrix from initial covariance matrix

P<sub>k</sub> = AP<sub>k-1</sub> A<sup>T</sup> + Q<sub>k</sub>

Where Q is the error in calculating the process covariance matrix

##4 Calculate kalman gain
K =  P<sub>k</sub>H<sup>T</sup>
	---------------------------
   HP<sub>k</sub>H<sup>T</sup> + R

Where H is just a matrix that shapes the other matrices. R is the observation errors (in the same shape/format as the covariance matrix)

##5 calculate the new observed matrix 
http://www.ilectureonline.com/lectures/subject/SPECIAL%20TOPICS/26/190/5793
Y<sub>k</sub> = CY<sub>km</sub> + Z<sub>k</sub>

Y is the observed state matrix. 

where Z is the observation error due to delays/electronics etc. Frequently zero. 

C is the matrix to transform the observation into the same shape as the state matrix

##6 combine predicted state with observation to make NEW predicted state.
X<sub>k</sub> = X<sub>kp</sub> + K(Y<sub>k</sub> - HX<sub>kp</sub>)

X<sub>k</sub> = new prediction
X<sub>kp</sub> = old prediction
K = Kalman gain
Y<sub>k</sub> = measurement
H = transformation matrix (often the identity matrix)

##7 Update process covariance matrix (ready for next iteration)

P<sub></sub>k = (I - KH)P<sub>kp</sub>


