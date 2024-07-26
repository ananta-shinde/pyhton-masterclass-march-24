
class StudentManager :
    def __init__(self):
        self.list = []

    def addNewStudent(self,studref):
        self.list.append(studref)

    def getAllStudent(self):
        return self.list

    def getStudentByPRN(self,prn):
        for s in self.list:
            if(s.prn == prn):
                return s
            else:
                return False

    def updateStudentPRN(self,prn,studref):
        for s in self.list:
            if(s.prn == prn):
                s = studref

    def deleteStudentByPRN(self,prn):
        for s in self.list:
            if(s.prn == prn):
                self.list.remove(s)

    def getStudentCount(self):
        return len(self.list)