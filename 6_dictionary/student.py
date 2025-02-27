n = int(input("Enter the number of students : "))
d = {}

for i in range(n) :
    x = {}
    x['name'] = input("Enter the name of the student : ")
    x["marks"] = int(input("Enter the marks : "))
    d[i] = x

markList = []
for i in d :
    markList.append( d[i]["marks"] )

highest = markList.index(max(markList))

print("Highest Marks : ", d[highest]["marks"], "Scored by : ", d[highest]["name"])