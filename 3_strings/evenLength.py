words = input("Enter a string : ")

count = words.split(' ')

print("Even length words in the input are : ")
for i in count:
    if( len(i) % 2 == 0 ):
        print(i)
