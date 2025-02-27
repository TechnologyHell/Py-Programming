dict = {'A' : 10 , 'B' : 21 , 'C' : 32 , 'D' : 43}

print("Initial dictionary : ", dict)

n = int(input("Enter the value to multiply : "))

for i in dict :
    if ( dict[i] % 2 == 0) :
        dict[i] = dict[i] * n

print("Dictionary after multiplying even occurances with %d : ", n, dict)