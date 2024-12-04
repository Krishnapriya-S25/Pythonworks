def is_perfectnum(num):
    total=0
    for i in range(1,num):
        if num%i==0:
            total=total+i
    print("perfectnumber"if total==num else"notperfect")
is_perfectnum(6)