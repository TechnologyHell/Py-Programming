car1 = {
    'brand' : 'Ford' ,
    'model' : "Mustang", 
    "color" : "red"
}

att = input("Enter the attribute for the car : ")
val = input("Enter the value : ")

car1[att] = val

print("Updated Dict : ", car1)

a2 = input("Enter the attribute to remove : ")

#popitem() removes last attribute
car1.pop(a2)

print("Updated Dict : ", car1)