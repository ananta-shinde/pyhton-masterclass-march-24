from studentManager import StudentManager
from student import Student

class College :

    def __int__(self,id,name):
        self.college_id = id
        self.name = name
        self.email = ""
        self.address = ""
        self.contact = ""
        self.studentManger = StudentManager()

    def createNewStudent(self):
        prn = input("enter student prn :")
        name = input("enter student name :")
        email = input("enter student email : ")
        newStud = Student(prn,name,email)
        self.studentManger.addNewStudent(newStud)

    def getStudentList(self):
        return self.studentManger.getAllStudent()


