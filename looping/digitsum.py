num=int(input("enter num"))#234 
total=0#0 
while num!=0:#234!=0
    digit=num%10 #234%10
    total=total+digit#0+4
    num=num//10 #234//10=23

print(total)