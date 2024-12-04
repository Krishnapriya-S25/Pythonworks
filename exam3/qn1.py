text="on june 5th,2024,we will celebrate @ our annual event: 'Tech Innovations 2024!'"
word_count={}

for w in text:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)


