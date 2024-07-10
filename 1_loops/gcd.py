x,y = map(int,input("Enter 2 numbers : ").split(' '))

if(x>y):
    small = y
else:
    small = x

for i in range (1, 1+small):
    if ( (x % i == 0) and (y % i == 0) ):
        gcd = i

print("The GCD of ", x, "and ", y, "is : ", gcd)