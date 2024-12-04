text="this is a test to remove duplicates words this test is  simple"
#split text wrt space
words=text.split(" ")
print(set(words))

text1="this is a test to remove duplicates words this test is  simple"
text2="this simple test remove duplicates words"
print(set(text1).issubset(set(text2)))    
 
