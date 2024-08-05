
class Student:

    def __init__(self,prn,name,city):
        self.__prn = prn
        self.name = name
        self.city = city

    def __printStudentInfo(self):
        print("PRN :"+str(self.__prn)+" Name :"+ self.name+" City:"+self.city)

    def printStudentData(self):
        self.__printStudentInfo()

    def getPRN(self):
        print(self.__prn);



class MetechStudent(Student):

    def __init__(self,prn,name,city):
        Student.__init__(self,prn,name,city)



s1 = Student(120215,"Ananta","Pune")
s1.printStudentData()
s1.getPRN()
s2 = MetechStudent(545454,"Suraj","Mumbai")
s2.printStudentData()