import math

x1, y1 = map(int,input("Enter coordinates for point A : ").split(' '))
x2, y2 = map(int,input("Enter coordinates for point B : ").split(' '))

d = pow( (x1-x2) , 2 ) + pow( (y1-y2) , 2 )
sq = math.sqrt(d)

print("The distance between the given points is : ", sq)