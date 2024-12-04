f=open("C:\\Users\\pc\\Desktop\\Pythonworks\\regfileworks\\socialpost.txt")

from re import finditer



for line in f:
    words=line.rstrip("\n")    
    pattern="#[a-zA-Z0-9]+"

    matcher=finditer(pattern,words)

    for obj in matcher:
        print(obj.group())

 

