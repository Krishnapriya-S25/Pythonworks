#Student Averge Score

Student_Marks = {
    "Kichu" : 100,
    "Rahul" : 100,
    "Vava"  : 100,
    "Kukku" :100
}
total_student = 0
total_score = 0
for v in Student_Marks.values():
    total_score += v
    total_student += 1
averge = total_score / total_student
print("Average Score : ",averge)