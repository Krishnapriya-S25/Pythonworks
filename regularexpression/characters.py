from re import finditer

text="I have 3 cars,2 bike and 1 cycle"

pattern="[a-zA-Z0-9]"#or"\w"

#pattern="\d"->digits
#pattern="\D"->exclude digits
#pattern="\W"->special characters
#pattern="\s"->matches space
#pattern="\S"->excluded space



matcher=finditer(pattern,text)

for obj in matcher:
    print(obj.start(),obj.group())


