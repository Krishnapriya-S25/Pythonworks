text="Hello world! This is a test for finding the longest word"
word=text.split(" ")
for w in word:
    longest_word=max(word,key=lambda w:len(w))
print(longest_word)
