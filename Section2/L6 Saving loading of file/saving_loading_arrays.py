import numpy as np
arr=np.arange(10)
print arr

#saving single array
np.save('saved_array',arr)
#now_file_is_created = saved_array.npy

new_array=np.load('saved_array.npy')
print new_array


#save multiple array

array_1=np.arange(25)
array_2=np.arange(30)

np.savez('saved_archieve.npz',x=array_1,y=array_2)

load_archieve=np.load('saved_archieve.npz')

print 'load_archieve[x] is'
print load_archieve['x']

print 'load_archieve[y] is'
print load_archieve['y']
