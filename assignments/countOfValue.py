numList = [20,50,45,12,20,55,45,60,20]

num = int(input("enter a number to search"))
count = numList.count(num)
if(count>0):
    print(str(num) + " repeated for "+ str(count) +" times")
else:
    print("number not found in list")