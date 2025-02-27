car1 = {
    'brand' : 'Ford' ,
    'model' : 'Mustang' , 
    'year' : 1964
}

x = car1.keys()
print("Initial Keys : ", x)

car1["color"] = "red"

print("After update : ", x)

#get specific value
print("Car Color : ", car1['color'])

#Check for key
if "year" in car1 :
    print("Present")

print("Model : ", car1.get("model"))

x = int(input("Enter the age of the car :" ))
car1[year]