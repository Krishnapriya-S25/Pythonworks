num1=int(input("enter  num1 "))

num2=int(input("enter num2 "))

try:
    result=num1/num2
    print(result)
except:
    num2=int(input("enter num2 "))
    result=num1/num2
    print(result)
finally: 
   print("file write")
   print("db commit")
