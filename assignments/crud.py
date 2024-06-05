
studentList =[ {
    "id":100,
    "name":"Ananta",
    "contact":"45645666654",
    "branch":"CSE"
    },
    {
    "id":105,
    "name":"Anil",
    "contact":"5454454545",
    "branch":"CSE"
    },
    {
        "id": 101,
        "name": "Suraj",
        "contact": "5454454545",
        "branch": "Mech"
    },
    {
    "id":102,
    "name":"John",
    "contact":"87878787887",
    "branch":"CSE"
    },
    {
        "id":103,
        "name":"Rahul",
        "contact":"878787878787",
        "branch":"Civil"
    },
]

def getAllStudents(slist):
    return slist;

def getStudentsByBranch(slist,brnachName):
    newlist = []
    for student in slist:
        if(student["branch"] == brnachName):
            newlist.append(student)
    return newlist;

def getStudentById(sList,id):
    searchedStudent = {}
    for student in studentList:
        if(student["id"] == id):
            searchedStudent =student
    return searchedStudent;


result = getStudentById(studentList,105);
print(result)