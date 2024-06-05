
def calculateTicketFair(cityNo):
    if(cityNo == 1):
        return 280*10;
    if(cityNo == 2):
        return 250*10
    if(cityNo == 3):
        return 350*10

print("----------------------welcome to Tripo -----------------------")
print("choose destination from following : ")
print(" 1. Latur  2.Pune   3.Mumbai")
citychoice =int( input("Enter number before your city name"))
ticketfair = calculateTicketFair(citychoice)

print("enter your details :")
name = input("Full name :")
age = input("Your Age :")

print("--------------------------------------")
print("Passanger Name :" + name)
print("Passanger Age : " + age)
print("Ticket Amount : " + str(ticketfair))
