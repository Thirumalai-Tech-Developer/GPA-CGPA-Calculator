cgpaorgpa = input("Calculate for (CGPA/GPA) : ").lower()
if cgpaorgpa == "gpa":
    totalsub = int(input("No Of Subjects: "))
    totallab = int(input("No Of Labs: "))
    naanmudhalvan = input("Do you have NaanMudhalvan(Y/N) : ").lower()
    print("Grade points simply put like this \n   o , a+ , a , b+ , b , c , u ")
    def gpa():
        def marks(grademark):
            if grademark == "o":
                return 10
            elif grademark == "a+":
                return 9
            elif grademark == "a":
                return 8
            elif grademark == "b+":
                return 7
            elif grademark == "b":
                return 6
            elif grademark == "c":
                return 5
            elif grademark == "u":
                return 0
            else:
                return 0
            
        total = 0
        totalcredit = 0

        for i in range(totalsub):
            grademark = input(f"Enter Sub{i+1} Grademark: ").lower()
            creditmark = int(input(f"Enter Sub{i+1} creditmark: "))
            grade = marks(grademark)
            if grade == 0:
                creditmark = 0
            mark = grade * creditmark
            total += mark
            totalcredit += creditmark

        for j in range(totallab):
            grademark = input(f"Enter Lab{j+1} Grademark: ").lower()
            creditmark = int(input(f"Enter Lab{j+1} creditmark: "))
            grade = marks(grademark)
            if grade == 0:
                creditmark = 0
            mark = grade * creditmark
            total += mark
            totalcredit += creditmark

        if naanmudhalvan == "y":
            grademark = input("Enter NaanMudhalvan Grademark : ").lower()
            creditmark = int(input("Enter NaanMudhalvan creditmark : "))
            grade = marks(grademark)
            if grade == 0:
                creditmark = 0
            mark = grade * creditmark
            totalcredit += creditmark
            total += mark

        print(total / totalcredit)
    gpa()
    
elif cgpaorgpa == "cgpa":
    totalsem = int(input("Enter no of semester : "))
    print("Simply put the gpa value ")
    def cgpa():
        totalcgpa = 0
        for i in range(totalsem):
            total = float(input(f"Enter Sem{i+1} GPA : "))
            totalcgpa += total
        print(totalcgpa/totalsem)
    cgpa()