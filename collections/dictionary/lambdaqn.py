words=["hello","hai","morning","test","apple"]
# def get_length(word):
#     return len(word)
 
get_length=lambda word:len(word)
print(max(words,key=get_length))