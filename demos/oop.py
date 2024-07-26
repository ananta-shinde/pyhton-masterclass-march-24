class Student:
     def __init__(self,rollNo,name):
         self.rollNo = rollNo
         self.name = name

student = {}
student["demo"] = 123456
student["xyz"] = 1245545

s1 = Student(45645,"Ananta")
s2 = Student(56565,"Ram")
s1.xyz = 20
studentList = []

studentList.append(s1)
studentList.append(s2)




print(type(s1))
print(s2.rollNo)
print(s1.rollNo)
print(studentList[0].xyz)



