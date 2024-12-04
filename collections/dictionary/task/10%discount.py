# 10% discount to items 

items_list ={"Samsung" : 15000,
             "Apple" : 60000,
             "Realme ": 20000}

discount = {k: v * 0.9 for k,v in items_list.items()}
print(discount)