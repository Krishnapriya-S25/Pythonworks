products=[
    {"id":1,"title":"s23ultra","brand":"samsung","price":78000},
    {"id":2,"title":"a17","brand":"samsung","price":18000},
    {"id":3,"title":"m50","brand":"samsung","price":16000},
    {"id":4,"title":"pocom3","brand":"poco","price":15000},
    {"id":7,"title":"vivov50","brand":"vivo","price":25000},
    {"id":5,"title":"oppof19pro","brand":"oppo","price":27000},
    {"id":6,"title":"iphone16pro","brand":"apple","price":150000},
    {"id":6,"title":"iphone16proplus","brand":"apple","price":150000},
    {"id":8,"title":"nokia105","brand":"nokia","price":900}

]

# total number of mobiles

total=len(products)
print(total)

# print mobile titles
mobile_title= [m.get("title") for m in products ]
print(mobile_title)

#print samsung mobiles
samsung=[m.get("title") for m in products if m.get("brand")=="samsung"]
print(len(samsung))
print(samsung)

#costly product
print(max(products,key=lambda d:d.get("price")))

#costlyproducts
costly_product=max(products,key=lambda d:d.get("price"))
max_price=costly_product.get("price")
costly_products=[m.get("title") for m in products if m.get("price")==max_price]
print(costly_products)

#brandcount
all_brand=[m.get("brand") for m in products]
print(all_brand)
brand_count={b:all_brand.count(b) for b in all_brand}
print(brand_count)

#costly producs
costly_products=max(products,key=lambda d:d.get("price"))
max_price=costly_product.get("price")
costly_product=[m.get("title")for m in products if m.get("price")==max_price]

