start=int(input("enter num"))
end=int(input("enter num"))
if start<end:
    for num in range(start,end+1,1):
        print(num)
else:
    for num in range(start,end-1,-1):

        print(num)