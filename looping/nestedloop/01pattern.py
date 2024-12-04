for row in range(1,6):
    for col in range(1,row+1):
        prev=0
        current=1
        print(current)
        for i in range(1,8):
            next=prev+current
            print(next)
            prev=current
            current=next
            print(next,end="\t")
print()




    
# for row in range(1,6):
#     for col in range(1,row+1):
#         print(row,end="\t")

        
#     print()