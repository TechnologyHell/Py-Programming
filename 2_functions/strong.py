def factorial(n):
    f=1

    while( n!=0 ):
        f = n * f
        n -= 1
    
    return f


def strong(num):
    sum = 0
    n = num

    while(n!=0):
        dig = n % 10
        f = factorial(dig)
        sum += f
        n = n // 10

    return sum



number = int(input("Enter a number : "))

res = strong(number)

if ( res == number ) :
    print("Yes it is a Strong Number")
else : 
    print("Not a Strong number")