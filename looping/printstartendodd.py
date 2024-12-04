start=int(input("enter num"))
end=int(input("enter num"))

if start>end:
    start,end=end,start
i=start
while i<=end:
    if i%2!=0:
        print(i)
    i=i+1
