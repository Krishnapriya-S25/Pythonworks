def next_fibinocci_number(number):
    number=number+1
    prev=0
    current=1
    for i in range(1,number+1):
        next=prev+current
        prev=current
        current=next
        if next==number:
            number=number+1
print(number)
    
    


