r = int(input("Enter the upper limit : "))

a,b = 1,2
c = a+b
s = 0

while ( c < r ) : 
    c = a + b
    print(c, end = ' ')
    a = b
    b = c
    if(c % 2 == 0):
        s = s + c

print("\nSum of even fibonacci series under ", r, " is : ", s)