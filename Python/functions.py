def grade(mark):
    overall_percentage = (mark/175) *100
    if overall_percentage >= 80:
        final_grade = "A"
        return f"Congrats you achieved an {final_grade}"
    elif overall_percentage < 80 and overall_percentage >= 60:
        final_grade = "B"
        return f"Congrats you achieved a {final_grade}"
    elif overall_percentage < 60 and overall_percentage >= 45:
        final_grade = "C"
        return f"Congrats you achieved a {final_grade}"
    else:
        final_grade = "Failed"
        return f"I'm sorry but you {final_grade}"

homework = int(input("Homework score: "))
assessment = int(input("Assessment score: "))
final_exam = int(input("Final Exam score: "))
mark = (homework + assessment + final_exam)

print(grade(mark))

