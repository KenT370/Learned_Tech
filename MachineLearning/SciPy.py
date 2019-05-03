# SCIPY TUTORIAL


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import linalg, optimize
a = np.r_[3,[0]*5,-1:1:5j] # r means row concatenation bc the arrays are stacked by rows
# np.c_ stacks by coloumns so the # of col must match
print(a)
# 10j(step size): the # of points to produce in the range
# ex. -1 to 1 in 10 #'s (end point inclusive)

# mgrid (allows step size, used to produce N,N-d arrays )
d = np.mgrid[0:5,0:5]
print(d)
b = np.mgrid[0:5:4j,0:5:4j]
print(b)

#Polynomials (expression with variables)
from numpy import poly1d
p = poly1d([3,4,5])
print(p)
print('-'*10)
print(p*p) 
print('-'*10)
print(p.integ(k=6)) # f(x)=x^5-2x^-2+1 add one to the exponent and divide it by the power
# x^6/6 - 2x^-1/-1 + x + C 
print('-'*10)
print(p.deriv())
print('-'*10)
print(p([4,5]))

#Vectorizing functions (vectorize)
#convert an ordinary function that accepts + returns scalars into
#a "vectorized-function' with the same broadcasting rules as other
#Numpy functions
#scalar(variable that holds one val @ a time)
def addsubtract(a,b):
    if a > b:
        return a - b
    else:
        return a + b
#function of two scalar variables + returns a scalar result
vec_addsubtract = np.vectorize(addsubtract)
#now it can take array arguments + return array results
print(vec_addsubtract([0,3,6,9],[1,3,5,7]))
