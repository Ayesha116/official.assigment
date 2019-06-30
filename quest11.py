#write a python program to compute the distance between two points
import math
a = int(input("enter co-ordinate of x1: " ))
b= int(input("enter co-ordinate of x2: " ))
c= int(input("enter co-ordinate of y1: " ))
d= int(input("enter co-ordinate of y2: " ))
distance = math.sqrt(((b-a)**2)+((d-c)**2))
print("distance between two points is", distance)