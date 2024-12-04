f=open("C:\\Users\\pc\\Desktop\\Pythonworks\\dataset\\years.txt","r")
f_century=open("C:\\Users\\pc\\Desktop\\Pythonworks\\dataset\\century.txt","w")
f_leap=open("C:\\Users\\pc\\Desktop\\Pythonworks\\dataset\\leapyear.txt","w")

def is_century(year):

   return True if year%100==0 else False

def is_leap_year(year):

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        return True

    else:

        return False

for year in f:
    
    year=int(year)

    if is_century(year):

       f_century.write(str(year)+"\n")

    if is_leap_year(year):
        f_leap.write(str(year)+"\n")
f.close()
f_century.close()
f_leap.close()