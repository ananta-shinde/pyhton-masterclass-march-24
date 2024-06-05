def addProduct():
    # creating an empty dictionary
    product = {}
    # accepting data and putting it into dictionary
    product["name"] = input("Enter Product Name :")
    product["price"] = input("Enter Product price :")
    product["category"] = input("Enter Product category :")
    product["pid"] = 1000
    # Adding dictionary to the list
    productsList.append(product)

def updateProductByID(pid,key,value):

    # go through list to find product and update it
    for p in productsList:
        if (p["pid"] == pid):
            p[key] = value


print("************ welcome admin *********************")
print("choose from following options :")

print("1. Add New Product  2.Update Product  3.Delete Product" )
print("4. Get All Products  5.Get Product by Id  6.Get Product by Category" )

productsList = [{ "pid":100,"name":"Redmi 12","price":12000},{ "pid":101,"name":"Iphone 12","price":15000}]
choice = input("Enter Number Corresponding to option you want to choose :")
if(choice == "1"):
    addProduct()
 # accept product Id
pid = int(input("Enter product ID"))

updateProductByID(101,"price",10000)

print(productsList)




