import numpy as np
import matplotlib.pyplot as plt  # matplotlib is a package is used for the graph 

axes_values = np.arange(-100,100,10)

dx, dy=np.meshgrid(axes_values,axes_values) 

# meshgrid function is used for to take grid (meshgrid() function for creating a rectangular grid with the help of the given 1-D arrays that represent the Matrix indexing or Cartesian indexing. ... From the coordinate vectors, the meshgrid() function returns the coordinate matrices.)

#print "dx:"
#print dx

#print "dy:"
#print dy


function = 2*dx*3*dy  # this function is used for pixels or you can say that formula to that we define 

print function    # this is used to print the simple function


plt.imshow(function)    

# plt.imshow is a function of metaplotlib which is used for show the function in a better way

plt.title("function of plot 2*dx*3*dy")  
# title function is used to give the title of the image 


plt.colorbar() 
# this function is used for the colobar of graph

plt.savefig('myfig.png')  

# plt.savefig function is used to save the file in the computer 
