# rginal=num
# digit_count=len( str(num))
# total=0
# while(num!=0):
#     digit=num%10
#     exponent=digit**digit_count
#     total=total+exponent
#     num=num//10

# print("armstrong" if orginal==total else "no armstrong")
def arm_strong(num):
    
    digit_count=len(str(num))
    orginal=num
    
    total=0
    while(num!=0):
        digit=num%10
        exponent=digit**digit_count
        total=total+exponent
        num=num//10
print("armstrong" if total==num else "no armstrong" )
arm_strong(143)
