text="this is a simple question return word with maximum number of character"

words=text.split(" ")

word_count={w:len(w) for w in words}

print(max(words,key=lambda w:len(w) ))





    
    
 