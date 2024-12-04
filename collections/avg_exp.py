expenses=[10000,11000,12000,13000]
count=len(expenses)
total=0
for exp in expenses:
    total=total+exp
    avg_exp=total/count
print(avg_exp) 
