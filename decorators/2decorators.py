def swap_dec(fn): #fn=division(2,10)1
    def wrapper(n1,n2):#3 n1=2 n2=10

        if n1<n2:#2<10

            (n1,n2)=(n2,n1)#(10,2)

        return fn(n1,n2)#division(10,2)

    return wrapper#2

def round_dec(fn):
    def wrapper(n1,n2):
        n1=round(n1)
        n2=round(n2)
        return fn(n1,n2)
    return wrapper

    






@round_dec
@swap_dec

def add_num(num1,num2):
    return num1+num2
@round_dec
@swap_dec
def substraction(num1,num2):
    return num1-num2
@round_dec
@swap_dec
def division(num1,num2):
    return num1/num2   

# print(division(2,10)) 
print(add_num(2.5,3.6))

