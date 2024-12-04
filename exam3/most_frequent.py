text="this is a simple python program that print most recursive word.this is simple"

words=text.split(" ")

# freq_chara=max(words,key=lambda w:words.count(w))

# print(freq_chara)

def get_count(w):
    return words.count(w)


freq=max(words,key=get_count)
print(freq)









     

