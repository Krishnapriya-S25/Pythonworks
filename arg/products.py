def products(*args):
    result=1
    for num in args:
        result=result*num
    return result
print(products(10,20))