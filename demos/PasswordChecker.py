
password = input("Enter your password : ")
if(len(password)>=10 and password.__contains__("@")):
    print("password is valid")
else:
    print("password is invalid")

