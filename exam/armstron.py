num=int(input("enter num")) #153
digit_count=len(str(num))
total=0
orginal=num

while num!=0:
    digit=num%10
    exponent=digit**digit_count
    total=total+exponent
    num=num//10 
print("armstrong" if orginal==total else "noarmstrong")


