text="this is a simple programming question to find word with maximum number of characters"
#split with words
words=text.split(" ")
def get_count(w):
    return words.count(w)
frequent_word=max(words,key=get_count)
print(frequent_word)