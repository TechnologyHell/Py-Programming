def sumofdivisor(x):
    sum = 0
    for i in range(1,x):
        if (x%i==0):
            sum = sum + i
    return sum

a = int(input("Enter 1st numebr : "))
b = int(input("Enter 2nd number : "))

if( sumofdivisor(a) == b and sumofdivisor(b) == a) :
    print("Amicable")
else:
    print("Not Amicable")