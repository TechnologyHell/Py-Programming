dict1 = {'A' : 1 , 'B' : 2 , 'C' : 3}
dict2 = {'D' : 4 , 'E' : 5}
dict3 = {'F' : 6}

dict = {}

for i in (dict1, dict2, dict3) :
    dict.update(i)

print("Concatenated dictionary : ", dict)