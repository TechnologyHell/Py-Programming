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

    if ( num == sum ) :
        return 1
    else : 
        return 0



number = int(input("Enter a number : "))

strong_number = strong(number)

if ( strong_number ) :
    print("Yes it is a Strong Number")
else : 
    print("Not a Strong number")