
shape = input("Enter shape name")

if(shape == "square"):
    width = float(input("enter width of Square"))
    print("Area of Square is : "+ str(width*width))
if (shape == "rectangle"):
    width = float(input("enter width of Rectangle"))
    breadth = float(input("enter breadth of Rectangle"))
    print("Area of Rectangle is : "+ str(width*breadth))
else:
    print("Invalid shape")