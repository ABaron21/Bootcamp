file = open("example.txt", "w")

for n in range(1, 6):
    newline = "This is team" + str(n) + "\n"
    file.write(newline)

file.close()

file = open("example.txt", "r+")

file.write("This is a new line\n")
file.seek(0)
print(file.read())
