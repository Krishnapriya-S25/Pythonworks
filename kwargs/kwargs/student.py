# def student_info(*args,**kwargs):
#     if kwargs.get("operation")=="avg":
#         count=0
#         sum=0
#         for i in args:
#             count=count+1
#             sum=sum+i
#         return sum/count
#     if kwargs.get("operation")=="total":
#         return sum(args)
# print(student_info(45,43,44,operation="total"))
def student_info(*args,**kwargs):
    if kwargs.get("operation")=="total":
        return sum(args)
    if kwargs.get("operation")=="avg":
        return sum(args)/len(args)
print(student_info(45,43,44,operation="total"))

            
    

    