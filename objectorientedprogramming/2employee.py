class Employee:

    name:str
    age:int
    salary:int
    department:str

    def set_employee(self,name,age,salary,department):
        self.name=name
        self.age=age
        self.salary=salary
        self.department=department


    def display(self):
        print(self.name,self.age,self.salary,self.department)
    
employee_instance=Employee()
employee_instance.set_employee("krishna",23,250000,"it")
employee_instance.display()

  