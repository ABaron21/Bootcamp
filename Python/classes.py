from msilib.schema import Class


class Student:
    def avgmark(totalmark):
        avg = (totalmark/3)
        return f"Your average mark is {avg}"

    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_


John = Student("John", "21", "Maths")
test1 = int(input("First test result: "))
test2 = int(input("Second test result: "))
test3 = int(input("Last test result: "))
totalmark = (test1 + test2 + test3)

print(getattr(John, "class_"))
print(Student.avgmark(totalmark))
