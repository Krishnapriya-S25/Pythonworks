class Bankaccount:
    customer_name:str
    m_pin:int
    customer_type:str

    def __init__(self,customer_name,customer_type,m_pin):
        self.customer_name=customer_name
        self.__m_pin=m_pin
        self.customer_type=customer_type
    def __str__(self):
        return self.customer_name   
b_instance=Bankaccount("hari",2345,"savings")
print(b_instance)
print(b_instance.m_pin)



