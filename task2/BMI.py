weight=int(input("enter weight in kg"))
height_in_cm=int(input("enter height in cm"))
gender=input("enter gender")
height_in_m=height_in_cm/100
BMI=(weight/(height_in_m)**2)
BMI=round(BMI)
print(BMI)
 

if BMI<19:
    print("underweight")
elif BMI>=19 and BMI<25:
    print("normalweight")
elif BMI>=25 and BMI<30:
    print("overweight")
elif BMI>=30:
    print("obese")