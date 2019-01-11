import numpy as np


def filter(x, P):
	for Z in measurements:
		Z = np.matrix([Z])
		print(Z)
		print()
		# PREDICTION
		#Transition matrix A converts old x to new x. B is transition matrix that converts u into an adjustment for position and velocity, where u is external motion/acceleration.
		# w is the process noise term 
		x = A*x + B*u + w 
		
		# update the covariance matrix based on kinematic equations
		# Q is the process noise covariance matrix
		P = A*P*A.T + Q
		
		# MEASUREMENT
		# H turns state x into equivalent measurement of JUST position (no velocities)
		# y is thus a matrix of differences between measured and observed positions in the two dimensions (+ve if measured is greater)
		# i.e. the 'residual'
		y = Z.T - H*x
		
		# intermediate step for Kalman gain: S is the total uncertainty 
		S = H*P*H.T + R
		
		# calculate Kalman gain
		# equivalent to K = (error in estimate)/(error in estimate + error in measurement)
		K = P*H.T * np.linalg.pinv(S)

		# use Kalman gain to get new predicted x
		# move the prediction towards the measurement in an amount dependent on the Kalman gain
		x = x + K*y
		
		# use Kalman gain to get new predicted covariance matrix
		P = (I - K*H) * P
	
		print('x= ', x)
	
		print('P= ', P)
	

########################################


measurements = [[5., 10.], [6., 8.], [7., 6.], [8., 4.], [9., 2.], [10., 0.]]
initial_xy = [4, 12]

dt = 1

x = np.matrix([[initial_xy[0]], [initial_xy[1]], [0.], [0.]]) # initial state (location and velocity)

P =  np.matrix([
		[0,0,0,0],
		[0,0,0,0],
		[0,0,1000,0],
		[0,0,0,1000]
	]) 

# state transition matrix (converts old state to new state)
# based upon new_pos = old_pos + dt * velocity
A = np.matrix([
		[1., 0., dt, 0.],
		[0., 1., 0., dt],
		[0., 0., 1., 0],
		[0., 0., 0., 1.]
	]) 

# state transition matrix (adjusts new state to account for acceleration)
# based upon new_pos = old_pos + dt * velocity + (acceleration*dt**2)/2
B = np.matrix([
		[0, 0, 0.5*dt**2, 0],
		[0, 0, 0, 0.5*dt**2],
		[0, 0, dt, 0],
		[0, 0, 0, dt]
	])

# control vector of external force (i.e. acceleration)
u = np.matrix([
		[0],
		[0],
		[0],
		[0]
	])

# process noise term in calculation of new state
w = np.matrix([
		[0],
		[0],
		[0],
		[0]
	])

# measurement function: reflects the fact that we observe x and y but not the two velocities
H = np.matrix([
		[1., 0., 0., 0.],
		[0., 1., 0., 0.],
	]) 

# measurement error
R =  np.matrix([
		[10, 0],
		[0, 10]
	])

# error term for calculating covariance matrix
Q = np.matrix([
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0]
	])

# identity matrix
I = np.eye(4)

filter(x, P)
