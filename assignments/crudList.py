data = [];

for x in range(3):
    ip = input("enter value to add into list : ")
    data.append(ip)
print("list is saved.....")

choice = int(input("chose from options : 1. delete a value, 2. know count"))


if(choice == 1):
    ip = input("enter value to delete")
    data.remove(ip)
    print("deletion successfull")
    print(data)
elif(choice == 2):
    ip = input("enter value to search")
    print(ip + " repeated for " + str(data.count(ip)) + " times")
else:
    print("invalid choice......")