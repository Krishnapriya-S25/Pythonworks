lst1=["apple","orange","mango","potato"]
lst2=[100,200,]
#  lst={  lst1[i] : lst2[i] for i in range (len(lst2)) }
# print(lst)
result={}
for i in range(0,len(lst2)):
    list1_one_index=lst1[i]
    list_two_index=lst2[i]
result[list1_one_index]=list_two_index
balance=lst1[len(lst2):]
for index ,element in enumerate(balance):
    result[element]=index+1
print(result)
