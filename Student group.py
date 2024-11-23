print ("This program is used for to check the students are present in same group or not")
Group_A = ["Alice","Bob","Charlie"]
Group_B = ["David","Eve","Frank"]
student_name = input("Please enter the student name\n").title()
student_name1 = input("Enter the Student1:\n").title()
student_name2 = input("Enter the Student2:\n").title()
if student_name in Group_A:
    print(f"{student_name} is in Group A")
elif student_name in Group_B:
     print(f"{student_name} is in Group B")
else:
    print(f"{student_name.capitalize()} are not in any group")
if student_name1 == student_name2:
    print(f"{student_name1} and {student_name2} are the same")
else:
     print(f"{student_name1} and {student_name2} are not the same")