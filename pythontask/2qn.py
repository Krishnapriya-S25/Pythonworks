word1="pqrs"
word2="abc"
str=""
if len(word1)<len(word2):
    for i in range(len(word1)):
        if i<len(word2):
            str=str+word1[i]+word1[i]
        else:
            str=str+word1[i]
else:
    for i in range(len(word2)):
        if i<len(word1):
            str=str+word2[i]+word1[i]
        else:
            str=str+word2[i]
print(str)
    
