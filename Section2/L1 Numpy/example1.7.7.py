#example of two dimensional array 
import numpy as np

my_list1 =[1,2,3,4]
my_list2=[6,7,8,9]

#my_array1=np.array(my_list1)

my_array=np.array([my_list1,my_list2])


#usage of shape function
#print my_array.shape

#finding out the database of the members of the array

#print my_array.dtype

#zeros,ones,empty,eye,arrange

#new_array1=np.zeros(5) #create a new numpy array with (1*5).All elements are zeroes

#new_array1=np.ones([5,5]) #all elements are 1 
 
#new_array1=np.empty(5)

new_array1=np.eye(5)

print new_array1
