words=["hai","hello","hai","hello","hai"]


#create a emppty dictionary
words_count={}
#iteration of w in words
for w in words:
    if w in words_count:  #chk w in words_count
        
        words_count[w]+=1 #add=+1
    else:
        words_count[w]=1 


        
print(words_count)