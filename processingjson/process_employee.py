from json import load
f=open("C:\\Users\\pc\\Desktop\\Pythonworks\\dataset\\employee.json")
data=load(f)
for emp in data:
    print(emp)


