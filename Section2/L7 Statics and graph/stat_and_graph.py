import numpy as np
import matplotlib.pyplot as plt  # matplotlib is a package is used for the graph 

axes_values = np.arange(-100,100,10)

dx, dy=np.meshgrid(axes_values,axes_values) # meshgrid function is used for to take grid

print "dx:"
print dx

print "dy:"
print dy

