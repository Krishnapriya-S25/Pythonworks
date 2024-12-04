#starting with an alphabet p-t
#in second place mustbe a number that is divisible by 3
#followed by anynumber of alpha,numbers,@



from re import fullmatch

user_input=input("enter variable")

pattern="[p-tP-T][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("invalid")
else:
    print("valid")