mark = int(input("Please enter your mark?\n"))

if mark > 85:
    print("Distinction")
elif mark <= 85 and mark >= 65:
    print("Pass")
else:
    print("Fail")