#method_overloading=>same method name and diff  number of parameters
class Operation:

    def add(self,num1,num2):
        print(num1+num2)
    def add(self,num1,num2,num3):
        print(num1+num2+num3)
obj=Operation()
obj.add(10,20,30)
#this concept will not work in python