f=open("C:\\Users\\pc\\Desktop\\Pythonworks\\dataset\\fruits.txt","r")
fruits=[]
for line in f:
    fruits.append(line.rstrip("\n"))
print(fruits)

