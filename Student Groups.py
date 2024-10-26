Group_A = str(["Alice", "Bob", "Charlie"])
Group_B = str(["David", "Eve", "Frank"])
student_name = input("Enter the username: ").capitalize()
student_name1 = input("Enter the student name1: ").capitalize()
student_name2 = input("Enter the student name2: ").capitalize()
if student_name in Group_A:
    print(f"{student_name} is in Group A")
else:
    print(f"{student_name} is not in Group A")
if student_name1==student_name2:
    print(f"{student_name1} and {student_name2} are the same")
else:
    print(f"{student_name1} and {student_name2} are not the same")