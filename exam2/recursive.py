
def most_frequent(text):
    words=text.split(" ")
    word=max(words,key=lambda w:words.count(w))
    return word
text=input(" hello world!hello everyone.Welcome to the world :").casefold()
freq_word=most_frequent(text)
print(freq_word)

     


    
