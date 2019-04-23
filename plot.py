# Author : Babu Baskaran 
# Date   : 08/04/2019 Time : 22:00 pm
# Solution for problem number 10
# Version 1.0
# reference https://matplotlib.org/tutorials/introductory/pyplot.html
# import matplotlib for ploting
import matplotlib.pyplot as plt
# assigning list of range 0,4 to x
x = list(range (0,4))
# assigning x square into y
y = [i**2 for i in x]
# assigning 2x into z
z = [i*2 for i in x]
# plot function x
plt.plot(x)
# plot function y
plt.plot(y)
#plot function z
plt.plot(z)
# title of the graph display
plt.title('Graph Plotting in the rage [0,4]')
# plot x axis 
plt.xlabel('x')
#plot y axis
plt.ylabel('y')
# creating the plot grid
plt.grid(True)
# calling the values of each variables
plt.legend(['y = x', 'y=x^2', 'y=2x'], loc='upper left')
# output the plot
plt.show()
