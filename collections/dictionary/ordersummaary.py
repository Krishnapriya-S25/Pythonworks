orders=["tea","coffe","tea","gheeroast","plainroast","porotta","tea"]
orders_summary={}

for item in orders:

    if item in orders_summary:

        orders_summary[item]+=1
    else:
        orders_summary[item]=1
        
print(orders_summary)
