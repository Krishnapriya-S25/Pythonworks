from re import fullmatch

adhar_number=input("enter adharnumber ")

pattern="[0-9]{4}\s[0-9]{4}\s[0-9]{4}"

matcher=fullmatch(pattern,adhar_number)

if matcher==None:
    print("invalid")

else:
    print("valid")
