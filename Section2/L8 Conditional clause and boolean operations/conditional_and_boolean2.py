import numpy as np

x= np.array([100,400,500,600]) #each member pf 'a'
y=np.array([10,15,20,25])   #each member of 'b'
condition=np.array([True,True,False,False])  #each member cond.
 #add some boolean expersion

#use loops indirectly to perform this

z=[a if cond else b for a,cond,b in zip(x,condition,y)]   #this is some mushkil so we will do by other method 

print z


#np.where(#condition,#value for yes, #value for No)  #this function is used by the numpy fn.

z2=np.where(condition,x,y)
print z2

z3=np.where(x>0,0,1)
print z3


# some standard function of numpy

#we take sum function first.   sumx

print x.sum()

n=np.array([[1,2],[3,4]])


#column sum

print n.sum(0)   # this is how we find the value of array


print x.mean()
print x.std()
print x.var()


#logical operations and / or operations

condition2= np.array([True,False,False])

print condition2.any()   #or operator
print condition2.all()  #and operator









