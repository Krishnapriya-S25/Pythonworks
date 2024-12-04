str1="ace"
str2="abcde"
ptr=0
is_subsequence=True
for char in str1:
    while ptr<len(str2) and str2[ptr]!=char:
        ptr+=1
        if ptr==len(str2):
            is_subsequence=False
            break
        ptr+=1
print(is_subsequence)
        



