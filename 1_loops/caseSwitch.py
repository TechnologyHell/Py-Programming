c = input("Enter a character : ")

x = ord(c)

if ((x>=65 and x<=90) or (x>=97 and x<=122)):
    print("Character")
elif (x>=48 and x<=57):
    print("Integer")
else:
    print("Special Character")