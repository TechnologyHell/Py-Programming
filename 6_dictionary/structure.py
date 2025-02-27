item1 = {
    'Name' : 'Aman' ,
    'Age' : 21 ,
    'Stream' : 'CSE'
}

item2 = {
    'Name' : 'Ajay' ,
    'Age' : 23 ,
    'Stream' : 'AIML' ,
    'Age' : 25 
}

print("Length of each dataset : ", len(item2))
print("Age of item2 : ", item2['Age'])  #newer value is taken

print(type(item1))

thisdict = dict(Name = "Rahul" , Age = 28 , Stream = "ECE")
print("Dictionary Constructor :", thisdict)