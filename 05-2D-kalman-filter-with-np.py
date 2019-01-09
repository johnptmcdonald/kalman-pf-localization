import numpy as np

def filter(x, P):
	for meas in measurements:
		print(meas)
		# prediction
		x = A.dot(x) + B.dot(u) + w
		P = A.dot(P).dot(A.transpose()) + Q

		# update

		Z = np.array(meas)
		y = Z.transpose() - (H.dot(x)) 

		K = P.dot(H.transpose()).dot(np.linalg.pinv(H.dot(P).dot(H.transpose())))

		# use Kalman gain to get new state x
		x = x + (K.dot(y))

		# ...and new state covariance matrix P
		P = (I - (K.dot(H))).dot(P)


		print('x= ', x)
		print('P= ',P)

dt = 1

A = np.array([
	[1, 0, dt, 0],
	[0, 1, 0, dt],
	[0, 0, 1, 0],
	[0, 0, 0, 1],
	])

B = np.array([
	[0, 0, 0.5*dt**2, 0],
	[0, 0, 0, 0.5*dt**2],
	[0, 0, dt, 0],
	[0, 0, 0, dt]
	])

u = np.array([
	[0],
	[0],
	[0],
	[0]
	])

w = np.array([
	[0],
	[0],
	[0],
	[0]
	])

Q = np.array([
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0]
]) #error in calculating the process covariance matrix

P = np.array([
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 1000, 0],
	[0, 0, 0, 1000],
	])

H = np.array([
	[1, 0, 0, 0],
	[0, 1, 0, 0]
	])

R = np.array([
	[0.01, 0.],
	[0, 0.01],
	]) #error in measurement of x and y

I = np.eye(4)

measurements = [[5., 10.], [6., 8.], [7., 6.], [8., 4.], [9., 2.], [10., 0.]]
initial_xy = [4., 12.]

x = np.array(([[initial_xy[0]], [initial_xy[1]], [0.], [0.]])) # initial state (location and velocity)


filter(x, P)
