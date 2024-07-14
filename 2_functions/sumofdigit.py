def sod(x):
    sum = 0
    while(x!=0):
        r = x%10
        sum = sum + r
        x = x//10
    return sum

num = int(input("Enter a number : "))
sum = sod(num)

print("Sum of digits of ", num, "is : ", sum)