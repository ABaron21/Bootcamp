file = open("example.txt", "w")
file_content = file()
file.seek(0)

file.write("This is a new line\n" + file_content)
file.seek(0)
file_content = file.read()
file.close()

print(file_content)
