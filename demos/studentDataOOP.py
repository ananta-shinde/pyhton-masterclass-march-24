class Student:
    #properties


    #Actions
    def __init__(self,rollno,name,branch):
        self.rollNo = rollno
        self.name = name
        self.branch = branch

    def showDetails(self):
        print("Rollno:"+str(self.rollNo) +" Name:" +self.name +" Brnach :"+self.branch)


class StudentManager:

    def __init__(self):
        self.list = []
    #actions
    def addStudent(self,stud):
        self.list.append(stud)

    def findStudentByRollNo(self,rollNo):
        studRef= None

        for s in self.list:
            if(s.rollNo == rollNo ):
               studRef = s

        return studRef
    def deleteStudent(self,rollNo):
        studRef = self.findStudentByRollNo(rollNo)
        self.list.remove(studRef)

    def printStudentList(self):
        for s in self.list:
            s.showDetails()



s1 = Student(100,"Ananta","MECH")
s2 = Student(101,"Suraj","MECH")

studMng = StudentManager()
studMng.addStudent(s1)
studMng.addStudent(s2)
studMng.deleteStudent(100)
studMng.printStudentList()
