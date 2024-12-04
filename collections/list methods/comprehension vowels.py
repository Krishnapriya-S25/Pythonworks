#words starting with vowels

text=["apple","iphone","orange","potato"]
words=[w for w in text if w[0] in ['a','e','i','o','u'] ]
print(words)  
# consonant
words=[w for w in text if w[0]  not in ['a','e','i','o','u'] ]
print(words)