#starting with kL
#2digit
#alphabets min 1max2
#4digit

from re import fullmatch

vehicle_number=input("enter number ")

pattern="(KL)+[0-9]{2}[A-Z]{1,2}[0-9]{4}" #(KL|kl) o(KL ORkl)

matcher=fullmatch(pattern,vehicle_number)


if matcher==None:
    print("invalid")

else:
    print("valid")

#passport
#adhar
#drivinglicense