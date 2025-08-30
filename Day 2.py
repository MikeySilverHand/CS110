import numpy as np
import math

a = np.array([1,2,3])
b = np.array([[1,2],[3,4]])

print(f"This is array A: {a}")
print(f"This is array B: {b}")

#This will print out shape like (nxm)
print(a.shape)
print(b.shape)

#it will print out the dimension
print(b.ndim)

#It will print out how many current elements there are in x array
print(b.size)

#What is its data type
print(b.dtype)

#Make an array filled with zeros
print(np.zeros((2,3)))

#Make an array filled with ones
print(np.ones((2,3)))

#first number is the starting point; the second number is the increasing element; thing number is how many elements are between the first two numbers
print(np.linspace(0,1,5))

#Area calculation
b = 6 #inch
h = 4 #inch

Area = b*h
print(f"Area of the square is: {Area}")

#Circle
r = 3
pi = math.pi

AreaC = pow(r,2)*pi
print(f"The area of a circle with radius {r} is: {AreaC}")

def cir(r):
  return np.pi * pow(r,2)

r = 3

Area2 = cir(r)

print(f"The area of a circle with radius {r} is: {Area2}")