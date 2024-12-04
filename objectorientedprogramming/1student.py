class Student:
    
    name:str
    roll:int
    age:int
    course:str

#intialization attributes of students class 
    def set_student(self,name,roll,age,course):
         self.name=name
         self.roll=roll
         self.age=age
         self.course=course
    def display(self):
        print(self.name,self.roll,self.age,self.course)
#reference_name=className()
student_instance1=Student()

student_instance1.set_student("vyshnav",12,23,"django")

student_instance1.display()

