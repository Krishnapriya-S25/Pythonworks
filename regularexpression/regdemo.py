# text="ababababab"
#is this patttern available or not
from re import finditer

text="ababababab"

matcher=finditer("ab",text)# objectstart,group)

for m in matcher:
    print(m.start(),m.group())


