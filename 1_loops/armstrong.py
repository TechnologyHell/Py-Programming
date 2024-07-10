n = input("Enter a number : ")
l = len(n)
x = int(n)
s = 0

while( x!= 0):
    r = x % 10
    s = s + r ** l
    x = x // 10

if ( s == int(n) ) :
    print("Palindrome")
else :
    print("Not Palindrome")