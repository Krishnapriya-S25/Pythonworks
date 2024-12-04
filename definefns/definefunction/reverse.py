# create a fn smart_sub with three parameter num1,num2,reverse
# reverse take boolean value
# if reverse==True then  return num2-num1 elsenum1-num2
def smart_sub(num1,num2,reverse):
    return num2-num1 if reverse==True else num1-num2
print(smart_sub(5,8,True))