class Mobile:

    name:str

    price:int

    brand:str

    def __init__(self,name,price,brand):
        self.name=name

        self.price=price

        self.brand=brand

    def display(self):
        print(self.name,self.price,self.brand)

Mobile_instance1=Mobile("oneplusnord",45000,"oneplus")

Mobile_instance1.display()