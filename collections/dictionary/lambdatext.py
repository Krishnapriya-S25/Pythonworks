text="this is a simple programming question to find word with maximum number of characters"
#split with words
words=text.split(" ")
def get_length(w):
    return len(w)
srt_words=sorted(words,key=get_length,reverse=True)
print(srt_words)
