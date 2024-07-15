str = input("Enter a string : ")

c = "qwrtypsdfghjklzxcvbnm"
v = "aeiou"
d = "1234567890"

countc = 0
countv = 0
countd = 0
counts = 0

for i in str.lower():
    if ( i in c ):
        countc = countc + 1
    elif( i in v ):
        countv = countv + 1
    elif( i in d ):
        countd = countd + 1

print("Consonants : %d\nVowels : %d\nDigits : %d\n" % ( countc, countv, countd) )