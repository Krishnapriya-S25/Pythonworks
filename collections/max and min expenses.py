expenses=[10000,11000,12000,13000]
max_exp=0
for exp in expenses:
    if exp>max_exp:
        max_exp=exp
print(max_exp)

min_exp=expenses[0]
for exp in expenses:
    if exp<min_exp:
        min_exp=exp
print(min_exp)
count=len(expenses)
total=0
for exp in expenses:
    total=total+exp
    avg_exp=total/count
print(avg_exp)




    
