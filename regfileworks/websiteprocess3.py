
# from re import finditer
from re import findall

f=open("C:\\Users\\pc\\Desktop\\Pythonworks\\regfileworks\\website.txt")


# for line in f:
#     word=line.rstrip("\n")

#     pattern="(http|https)://[\w./]+"

#     matcher=finditer(pattern,word)

#     for obj in matcher:
#         print(obj.group())


content=f.read()

pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:
    print(url)

