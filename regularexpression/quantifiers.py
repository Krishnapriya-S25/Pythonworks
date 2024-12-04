from re import finditer

text="ababababaaaabba"

# pattern="a{2}"

pattern="a{1,3}" #"a(minimum,maximum)"

#pattern=*->any number including 0





matcher=finditer(pattern,text)

for obj in matcher:
    print(obj.start(),obj.group())