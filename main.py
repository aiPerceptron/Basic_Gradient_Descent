"""
This code makes it so I can get from a high place on my terrain to a low place.

With only knowing the slope, I can traverse the terrain and make it to the bottom -
I don't know what the actual terrain is here.
For this problem, the slope is 2x-4. The unknown terrain is x^2 - 4x.
I can decode the terrain into a slope by using the formula below: 

If the terrain is x the slope is 1
If the terrain is x^2 the slope is 2x
If the terrain is x^3 the slope is 3x^2

If the terrain is x^n the slope is nx^(n-1)
"""
import matplotlib.pyplot as plt
import numpy as np
x = 4
lr = 0.1 
x_values = []
y_values = []

for i in range(25):
    x = x - lr * (2*x-4) # the slope of the terrain
    x_values.append(x)
    print(x)

# X ** 2 - 4x
x_plot = np.linspace(-10,24,25)
y_plot = x_plot ** 2 - 4 * x_plot
x_values= np.array(x_values)
    
y_values = x_values ** 2 - 4 * x_values

plt.plot(x_plot,y_plot)
plt.scatter(x_values,y_values)
