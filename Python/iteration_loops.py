amount = 0
nameList = []

while amount < 5:
    name = input("What's your name: ")
    nameList.append(name)
    amount += 1

print(nameList)

for name in nameList:
    print(name, "has been added to the list")

for i in range(10, 21, 2):
    print(i)