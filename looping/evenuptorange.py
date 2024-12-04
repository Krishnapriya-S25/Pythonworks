begin=int(input("enter num"))
end=int(input("enter num"))
reverse=True if begin>end else False
i=begin
while (i<=end if reverse==False else i>=end):
    if i%2==0:
        print(i)
    if reverse==0:
        i=i+1
    else:
        i=i-1


