print("==================================")
print("      ATTENDANCE CALCULATOR")
print("==================================")

name = input("Enter student name: ")
sub= input("enter subject name: ")
total = int(input("Enter total number of classes conducted: "))
a = int(input("Enter classes you attended: "))

if total <= 0:
    print("Total classes should be greater than 0.")

elif a < 0 or a > total:
    print("Invalid attendance details.")

else:
    attendance = (a / total) * 100

    print("---------- RESULT ----------")
    print("Student Name:", name)
    print("subject:", sub)
    print("Total Classes:", total)
    print("Classes attended:", a)
    print("Attendance:", attendance, "%")

    if attendance >= 90:
        print("Remark: Excellent")
        print("Status: Eligible")

    elif attendance >= 85:
        print("Remark: Good")
        print("Status: Eligible")

    elif attendance >= 75:
        print("Remark: Satisfactory-can be improved")
        print("Status: Eligible")

    elif attendance >= 65:
        print("Remark: low Attendance")
        print("Status: Not Eligible")

    else:
        print("Remark: Very Low Attendance")
        print("Status: Not Eligible")

    if attendance < 75:
        c = 0

        while ((a + c) / (total + c)) * 100 < 75:
            c= c+1

        print("you need to attend ", c , " classes consecutively to reach 75% attendence")
