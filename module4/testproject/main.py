grades = {"ravi": 23, "jake": 43, "joll": 53, "conc": 43, "sai": 53}
total = 0
for score in grades.values():
    total += score
print(total / len(grades))
top_name = ""
top_score = 0
for name, score in grades.items():
    if score > top_score:
        top_score = score
        top_name = name
print(top_name, top_score)
student_name = input("Enter a student name: ")
print(grades.get(student_name, "Not found"))
