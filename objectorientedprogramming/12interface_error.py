class GrandParent:
    def m(self):
        print("Grand parent class m method")
class Parent:
    def m(self):
        print("parent class m method")
class Child(Parent,GrandParent):#(Grandparent,parent)=>o/p=grandparentclass method
    def m3(self):
        print("child class 3 method")
child_instance1=Child()
child_instance1.m3()
child_instance1.m()
