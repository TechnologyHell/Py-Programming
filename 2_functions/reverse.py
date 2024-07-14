def rev(num):
    new = 0
    while(num!=0):
        r = num % 10
        new = new * 10 + r 
        num = num // 10
    return new


number = int(input("Enter a number : "))
reverse = rev(number)

print("Reverse : ", reverse)