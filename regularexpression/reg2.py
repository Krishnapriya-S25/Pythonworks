#lowercase alphabets
from re import finditer

text="I have 3 cars,2 bike and 1 cycle"

pattern="[a-zA-Z]"#chk for all Alphabets
#for chk lowercase->"[a-z]"

# pattern="[0-9]"->for chk digits

#alphanumeric->
#pattern-> "[a-zA-Z0-9]"for  chk all 

#pattern->"[^ak]" exclude a,k

#all lower case alphabets exclude a,k
#pattern=>"[^a,kA-Z0-9,\-]""


matcher=finditer(pattern,text)
 
for obj in matcher:


    print(obj.start(),obj.group())











