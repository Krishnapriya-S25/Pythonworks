num1=int(input("enter num")) #3
num2=int(input("enter num")) #4
max_num=max(num1,num2) #4
for i in range(max_num,(num1*num2)+1,max_num):
    if i%num1==0 and i%num2==0:
        print(i)
        break
        
