import numpy as np
arr= np.arange(0,12)
print arr


print arr[0:5]  #this is know as slicing 
print arr[2:6]

arr[0:5]=19,20,21,22,23
print arr

#interesting thing and important 

arr2= arr[0:6]
print arr2

arr2[:]=29 #all elements are modified

#print arr2

print arr
