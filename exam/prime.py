num=int(input("enter num"))
is_prime=True
i=0
#factors of number=1,number
for  i  in range(2,num):
    if num%i==0:
        is_prime=False
print(is_prime)



