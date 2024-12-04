from re import fullmatch

user_input=input("enter variable name ")

#rule->starts with  alphabets,any number of alpha,digits,_

pattern="[a-zA-Z][a-zA-Z0-9]*"


matcher=fullmatch(pattern,user_input) #NONE

if matcher==None:
    print("invalid")
else:
    print("valid")

