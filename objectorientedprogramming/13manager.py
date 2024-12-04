class Person:
    name:str
    age:str
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person_info(self):
        print(self.name,self.age)


class Employee:
    employee_id:int
    salary:int
    def __init__(self,employee_id,salary):

       self.employee_id=employee_id
       self.salary=salary
    def display_employee_info(self):
        print(self.employee_id,self.salary)

class Manager(Person,Employee):
    department:str

    def __init__(self,name,age,employee_id,salary,department):
        Person.__init__(self,name,age)
        Employee.__init__(self,employee_id,salary)
        self.department=department
    def display_manager_info(self):
        print(self.department)
        self.display_employee_info()
        self.display_person_info()





manager_instance=Manager("AG",34,100,25000,"HR")
manager_instance.display_manager_info()


