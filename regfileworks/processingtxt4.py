
from re import findall

f=open("C:\\Users\\pc\\Desktop\\Pythonworks\\regfileworks\\text.txt")

content=f.read()
    
pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

dates=findall(pattern,content)

for d in dates:
    print(d)





