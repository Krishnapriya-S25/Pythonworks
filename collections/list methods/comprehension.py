arr=[2,3,4,5,6]
# square=[]
# for num in arr:
#     result=num**2
#     square.append(result)
# print(square)
 
 #list comprehension=[return loop condition]
square=[ num**2 for num in arr]
print(square)

add_ten=[ num+10 for num in arr ]
print(add_ten)

even_num=[num for num in arr if num%2==0]
print(_num)

odd_num=[  num for num in arr if num%2!=0]
print(odd_num)






