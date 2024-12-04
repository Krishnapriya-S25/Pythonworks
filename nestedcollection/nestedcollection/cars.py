
 
cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dcd"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torque"]},
]
#count of vehicles
print(f"total vehicles:{len(cars)}")

#print available colors of baleno
baleno=[c.get("colors")for c in cars if c.get("name")=="baleno"]
print(baleno[0])

#print all brands
brands=set(c.get("brand")for c in cars)
print(brands)

# all_brands=[c.get("brand") for c in cars]
# # print(set(all_brands)) 

# print car name available inamt  transmission
transmission=[c.get("name") for c in cars if "amt" in c.get("transmissions")]
print(transmission)

#cars available in blue color
blue_color=[c.get("name") for c in cars if "blue" in c.get("colors")]
print(blue_color)

#all transmission types
transmission={t for c in cars for t in c.get("transmissions")}
print(transmission)

#all colors
all_color={cl for c in cars for cl in c.get("colors")}
print(all_color)

#most popular color
color=[cl for c in cars for cl in c.get("colors")]
color_count={cl:color.count(cl) for cl in color}
print(max(color_count))

#costly car
costly_car=max(cars,key=lambda d:d.get("price"))
print(costly_car.get("name"))

#min cost
min_cost=min(cars,key=lambda d:d.get("price"))
print(min_cost.get("name"))

#sort car wrt price
sorted=sorted(cars,key=lambda d:d.get("price"),reverse=True)

sorted_car_title={c.get("name"):[c.get("price"),c.get("brand") ] for c in sorted}
print(sorted_car_title)














