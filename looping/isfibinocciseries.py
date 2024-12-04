# 0 1 1 2 3 5 8 13
# p c n
#   p c n
num=int(input("enter num"))
previous=0
current=1
is_fibannocci=False
for i in range(1,num+1):
    next=previous+current
    previous=current
    current=next
    if next==num:
        is_fibannocc=True
        break
print(is_fibannocci)

