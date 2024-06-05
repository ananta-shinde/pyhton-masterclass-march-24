productList = [];

for x in range(5):
    product = {};
    product["name"] = input("enter product name")
    product["price"] = input("enter product price")
    product["discount"] = input("enter product discount")
    productList.append(product);

print(productList);



