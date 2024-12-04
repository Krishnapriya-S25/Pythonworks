num=int(input("enter num"))
is_prime=True
#factors of a number=1,number
for i in range (2,num,1):
    if num%i==0:
        is_prime=False
        break



print(is_prime)