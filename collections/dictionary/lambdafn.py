#lambda function
#lambda function for adding 2 numbers
add=lambda n1,n2:n1+n2
print(add(10,20))

#lambda function for substracting 2 num
sub=lambda n1,n2:n1-n2
print(sub(10,2))

#lambda function for cube of num
cube=lambda n:n**3
print(cube(3))

max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2
print(max_two("hai","morning"))


min_two=lambda str1,str2:str1 if len(str1)<len(str2) else str2
print(min_two("hai","morning"))


# def smart_sub(num1,num2):
#     return num1-num2 if num1>num2 else num2-num1


smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1
print(smart_sub(10,20))





