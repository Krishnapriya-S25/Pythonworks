num=int(input("enter num")) 

total=0

for i in range(1,num):

    if num%i==0:

      total=total+i
      
print("perfect" if total==num else "notperfect")


