def palindrome(x):
    for i in range (len(x)):
        if(x[i] != x[len(x) - i - 1]):
            return 0
        
a = input("Enter your input : ")

if(palindrome(a) == 0):
    print("Not Palindrome")
else:
    print("Palindrome")