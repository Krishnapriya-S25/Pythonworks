class GrandParent:
    def m1(self):
        print("Grand parent class m1 method")
class Parent:
    def m2(self):
        print("parent class m2 method")
class Child(Parent,GrandParent):
    def m3(self):
        print("child class 3 method")
child_instance1=Child()
child_instance1.m3()
child_instance1.m2()
child_instance1.m1()