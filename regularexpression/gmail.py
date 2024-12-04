#validate gmailid
#lowercase
#starts witj an alpha
#numbersoptional
#@gmail.com
#before at 6 to 64 character


from re import fullmatch

email=input("enter email")


pattern="[a-z]+[a-z0-9]{5,63}@gmail.com"


matcher=fullmatch(pattern,email)

if matcher==None:
    print("invalid")

else:
    print("valid")





