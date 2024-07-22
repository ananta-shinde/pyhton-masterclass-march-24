
#entity : dictionary
#collection : list
class Student:
    def __init__(self):
        self.rollNo = input("Enter roll No")
        self.name = input("Enter name")
        self.branch = input("enter branch")


studentList = []

s1 = Student()
s2 = Student()
print(s1.rollNo)
print(s2.name)
