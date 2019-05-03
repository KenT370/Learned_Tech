# -*- coding: utf-8 -*-
'''
Numpy Tutorial
'''
import matplotlib.pyplot as plt
import numpy as np
a = np.arange(15).reshape(3, 5)
print(np.shape(a))
print(a.ndim)
d = a.dtype.name
l = a.itemsize
b = a.size
e = type(a)

# Array Creation
a = np.array([3,4,5])
b = np.array([(3,4,5),(4,5,6)],dtype = complex)
e = np.zeros((3,4))
d = np.ones((2,3))
u = np.arange(10,30,5)
# To get a specific number of elements 
# use linspace
c = np.linspace(0,2,9)

a = np.array([[1,1],[0,1]])
b = np.array([[2,0],[3,4]])
# regualr elemental product
c = a * b
#matrix product
d = a @ b
# +=(adds elements up) and *=(multiplies all elements by #)
a *= 3
b += a
b = np.arange(12).reshape(3,4)
# if axis = 0 then it specifies columns
# if axis = 1 then it specifies rows
b.sum(axis = 0)
#cumulative sum 
b.cumsum(axis = 0)

a = np.arange(10)**3
#reverses a
a[ : :-1]

b = np.array([[1,2,3],[3,4,5],[2,4,2]])
# To iterate over an array but if you want to focus on each element
# use flat
for element in b.flat:
    print(element)
# versus using the standard way which only goes by row
for row in b:
    print(row)
# Changing the Shape of an Array
# to create a random array
b = np.floor(10*np.random.random((3,4)))
b.shape
''' b.ravel returns a flattened array
# b.reshape(6,2) returns an array with a modified shape
# b.T returns the transposed array
# ravel can be changed from C-style to Fortran style if need be
# Reshape modifies the shape but 
# ndarray.resize modifies the array
'''
b.reshape(3,-1)
# the column is modified to fit 3 rows

# Stacking Arrays
c = np.floor(10*np.random.random((3,4)))
a = np.vstack((b,c)) #vertically stacks
d = np.hstack((b,c)) #horizontally stacks
# np.column_stack stacks 2 1D arrays into a 2D array
# row_stack is equivilant to vstack
# for arrays with more than 2D hstack stacks along the 2nd axes + 
# vstack stacks along the 1st
# Concatenate allows for more flexibility

#Splitting an array
np.hsplit(c,2) #split into 2 arrays
np.hsplit(a,(3,4)) #split after the 3rd and 4th column
# vsplit is along the vertical axis and
# array_split allows one to specify the axis

# COPIES AND VIEWS
# 3 cases
# 1. No Copy at All
e = c # no new object is created, e and c are the same name for the same ndarray
e.shape = 3,4 #it also changes the shape of c

# 2. View or Shallow Copy
e = c.view() # e is not c but e is a view of the data
e.shape = 3,4 #c's shape doesn't change
e[0,1] = 1234 #c's data changes

#3. Deep Copy
e = c.copy() # e is not c 
e[0,0]= 9999 #anything done has no affect on c 

#FANCY INDEXING AND INDEX TRICKS
#Indexing with Arrays of Indices
j = np.arange(12)**2
d = np.array([[3,4],[9,7]])
j[d] # produces an array filled with values of j
# search of the max val of a time-dep series
time = np.linspace(20,145,5)
data = np.sin(np.arange(20).reshape(5,4))
ind = data.argmax(axis = 0)
time_max = time[ind]#times corresponding to the index
data_max = data[ind,range(data.shape[1])] #data[ind[0],0]
b = data.max(axis=0) #does the same thing as ^^
a = np.arange(5)
a[[0,0,2]] = [1,2,3] #zero's get converted to 1, then zeros get converted to 
# 2 then 2's get converted to 3

# Tricks and Tips
a = np.arange(30)
a.shape = 2,-1,3 #-1 means 'whatever size is needed'
# Vector stacking
# in matlab it's m = [x;y] but in Numpy it's 
# column_stack dstack hstack vstack

#Histogram
# pylab.hist plots the histogram auto and np.histogram generates the data
 
#build a vector of 1000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2,0.5
v = np.random.normal(mu,sigma,1000)
#plot a normalized histogram with 50 bins
plt.hist(v,bins = 50, density = 1)
plt.show()

#Compute the histogram with numpy
(n,bins) = np.histogram(v,bins=50,density = True)
plt.plot(.5*(bins[1:]+bins[:-1]),n)
plt.show()









