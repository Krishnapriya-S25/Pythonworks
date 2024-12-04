arr=[100,200,300,400,500,600,700,800,900]
# Odd_elements=[]
# for i in range(0,len(arr)):
#     if i%2!=0:
#         Odd_elements.append(arr[i])
# #odd elements insert
# for i in range(1,len(arr),2):
#     elements=Odd_elements.pop()
#     arr[i]=elements
# print(arr)

left=1

right=len(arr)-1
if right%2==0:
    right=right-1
while(left<right):
    arr[left],arr[right]=arr[right],arr[left]
    left=left+2
    right=right-2
print(arr)




    


    
    
