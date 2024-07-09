import math

print("Enter the sides of triangle : ")
a = float(input())
b = float(input())
c = float(input())

s = (a+b+c)/2

n = (s * (s-a) * (s-b) * (s-c))

area = math.sqrt(n) 

print("Area : ", area)