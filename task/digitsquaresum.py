num=int(input("enter num")) #145
total=0
while num!=0: #145!=0
    digit=num%10 #145%10=5
    square=digit**2 #5**2
    total=total+square #0+5**2
    num=num//10 #145//10=14

    
print(total)
    