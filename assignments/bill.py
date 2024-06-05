
product = {
    "id":100,
    "name":"Redmi 12",
    "price": 40000
}

def getGST(price):
    return price*(18/100)

def printBill(product,qty):
    subtotal = product["price"]*qty
    gst = getGST(subtotal)
    print("Name:" +product["name"])
    print("Quantity :" + str(qty))
    print("GST:"+ str(gst))
    print("Total :"+ str(subtotal+gst))

printBill(product,2)



