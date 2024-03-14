# <35  grade : F
# 35-50  grade : C
# 50-60  grade : B
# 60-75grade : A
# 75 above grade : A+

marks = float(input("Enter your marks in percentage"))

if(marks < 35):
    print("You got F grade")
if(marks>=35 and marks<50):
    print("You got C grade")
if (marks >= 50 and marks < 60):
    print("You got B grade")
if(marks>=60 and marks<75):
    print("You got A grade")
if(marks>=75):
    print("You got A+ grade")



