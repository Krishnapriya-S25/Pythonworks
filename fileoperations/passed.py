f1=open("C:\\Users\\pc\\Desktop\\Pythonworks\\dataset\\all_students.txt","r")
f2=open("C:\\Users\\pc\\Desktop\\Pythonworks\\dataset\\failed.txt ","r")
all_students_set=set()
failed_students=set()
for line in f1:
    line=line.rstrip("\n")
    all_students_set.add(line)
for line in f2:
    line=line.lstrip("\n")
    failed_students.add(line)
passed_students=all_students_set.difference(failed_students)
print(passed_students)
 
