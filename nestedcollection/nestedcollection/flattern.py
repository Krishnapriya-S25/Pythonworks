arr=[
    [10,20],
    [20,30],
    [30,40],
    [40,50]


]
# # result=[]
# # for ls in arr:
# #     for num in ls:
# #         result.append()
# # print(result)
flat_list=[num for ls in arr for num in ls]
print(flat_list)

        