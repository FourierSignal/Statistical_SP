import numpy as np
import matplotlib.pyplot as plt


'''

Random process: composed of several random variables 
 
white process is seen as a random process composing several iid random variables 

iid Random varibale 
----------------------
iid - independently and identically distributed
identically distributed - follow same distribution
independently distributed - independent of each other

white process is seen as a random process composing several random variables following the same Probability Distribution Function (PDF).

'''



'''
white noise process: random process composing several random variables which are iid

white noise signal: samples that independent and are generated from  same pdf.
'''


'''

generating White Gaussian Noise signal(normal distribution,with zero mean and standard deviation=1) of length 10 using randn.
'''

mu=0
sigma=1;
gaussian_white_noise= sigma * np.random.randn(10) + mu

print(gaussian_white_noise)
print(gaussian_white_noise.shape)


'''

generating White Uniform Noise signal(uniform distribution,with mean=3 and sd=1) of length 10 using rand.
'''

mu=3
sigma=1;
uniform_white_noise= sigma * np.random.rand(10) + mu
print(uniform_white_noise)
print(uniform_white_noise.shape)
