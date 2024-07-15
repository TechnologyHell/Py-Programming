word_1 = input("Enter 1st word : ")
word_2 = input("Enter 2nd word : ")

if( sorted(word_1) == sorted(word_2) ):
    print("Anagram")
else:
    print("Not anagram")