
orderlist = [
    {
        "id":100,
        "products":[
            { "id":500,"name":"Laptop","price":50000},
            { "id":450,"name":"Mobile","price":40000},
            {"id": 450, "name": "Laptop", "price": 55000},
            {"id": 450, "name": "Laptop", "price": 60000},
            {"id": 450, "name": "Mobile", "price": 15000},
        ]
    },
{
        "id":120,
        "products":[
            { "id":500,"name":"Laptop","price":50000},
            { "id":450,"name":"Mobile","price":40000},
        ]
    }
]

# to get list of all products in first order
orderlist[0]["products"]

# to get list of all products in second order
orderlist[1]["products"]

total = 0;

for product in orderlist[1]["products"]:
    total = total + product["price"]

print(total)



