
def validateinput(contact,uid):
    error = {}
    if(len(contact) != 10):
        error["contact"] = "Invalid input"
    if(len(uid) != 12):
        error["uid"] = "Invalid input"
    return error;

name = input("Enter your name")
phone = input("Enter your mobile number")
uid = input("Enter your aadhaar no")

print(validateinput(phone,uid))