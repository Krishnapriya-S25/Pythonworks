class Shipping:
    def calculate_shipping_cost(self,weight):
        print(weight*5)
class ExpressShipping(Shipping):
    def calculate_shipping_cost(self,weight):
        print(weight*20)
class StandardShipping(Shipping):
    def calculate_shipping_cost(self,weight):
        print(weight*10)
ship=Shipping()
ship.calculate_shipping_cost(10)

exp_shipping=ExpressShipping()

exp_shipping.calculate_shipping_cost(10)