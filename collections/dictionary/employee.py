#create dictionary employee with keys id,name,salary,department,experience

employee={"id":100,"name":"krishna","salary":45000,"department":"it","experience":1}
print(employee["name"])
employee["name"]="ammu"
#add contact detils
employee["contact"]=123456
print(employee)

#if exp>5 update employee salary as current_salary+10000 else  current_salary+5000

if employee["experience"]>5:
    employee["salary"]+=10000
else:
    employee["salary"]+=5000
print(employee)


#add role as a SDE if exp>5 else add role as JDE

if employee["experience"]>5:
    employee["role"]="SDE"
else:
    employee["role"]="JDE"
print(employee)

