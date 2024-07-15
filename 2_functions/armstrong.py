def armstrong(num):
    
    nod = len(num)
    sum = 0
    x = int(num)

    while(x!=0):
        rem = x % 10
        sum = sum + (rem ** nod)
        x = x//10
    
    if( int(num) == sum):
        return 1

    

number = input("Enter a number : ")
result = armstrong(number)

if(result):
    print("Yes it is an Armstrong Number")
else:
    print("Not it is not an Armstrong Number")