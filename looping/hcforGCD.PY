
# num1=int(input("enter num"))
# for i  in range(1,num1+1,1):
#     if num1%i==0:
#       print(i)
num1=int(input("enter num")) #12
num2=int(input("enter num")) #24
min_num=min(num1,num2) #12
gcd=1
for i in range(1,min_num+1,):
    if num1%i==0 and num2%i==0:
        print(i)
        gcd=i
print(f"gcd={gcd}")

