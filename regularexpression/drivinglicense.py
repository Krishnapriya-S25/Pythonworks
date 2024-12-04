from re import fullmatch

input=input("enter license number")


pattern="(kL)+[0-9]{2}\s[0-9]{4}[0-9]{7}"


matcher=fullmatch(pattern,input)


if matcher==None:
    print("invalid")

else:
    print("valid")








