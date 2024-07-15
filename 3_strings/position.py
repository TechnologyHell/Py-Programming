str = input("Enter a string : ")
find = input("Enter the word to find : ")

words = str.split()

if (find in words):
    pos = words.index(find) + 1
    print("Found at position : ",pos)

else:
    print("Word not found")