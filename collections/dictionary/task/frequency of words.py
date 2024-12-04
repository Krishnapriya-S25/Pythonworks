text="this is a test to remove duplicates words this test is  simple"
#split text wrt space
duplicates={}
words=text.split(" ")
print(words)
word_count={  w:words.count(w) for w in words}
print(word_count)


