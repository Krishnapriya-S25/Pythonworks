#create a dictionary product with keyid title price brand
product={"id":101,"title":"smartphone","price":25000,"brand":"vivo"}
print(product["id"])

#update product price
product["price"]=45000
print(product)

#update brand
product["brand"]="samsung"
print(product)

#add
product["use_by_date"]="12/5/24"
print(product)

#chk key is exist or not

if "price" in product:
    print("exist")
else:
    print("notexist")

#add offer as 10 if offer exist else add offer as a 20

if "offer" in product:
    product["offer"]=10
else:
    product["offer"]=20
print(product)


