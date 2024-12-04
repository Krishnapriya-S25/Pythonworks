student_data={
    "hari":[45,40,35],
    # key:values
    "vipin":[34,40,45],
    "vinay":[45,40,35],
    "bijoy":[33,38,35],
    "anvin":[32,30,40]
}
index=4

for i,element in enumerate(student_data):
    if i==index:

        mark=student_data.get(element)
        avg=sum(mark)/len(mark)
        print(avg)
    

avg={k:sum(v)/len(v)  for k,v in student_data.items()}
print(avg)

    

