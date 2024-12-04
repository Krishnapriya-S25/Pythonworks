nums=[2,1,-1]

cl_to_zero=nums[0]

for num in nums[1:]:
    if abs(num)<abs(cl_to_zero) or (abs(num))==abs(cl_to_zero) and num>cl_to_zero:
        cl_to_zero=num
print(cl_to_zero)
