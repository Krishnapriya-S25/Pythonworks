f=open("C:\\Users\\pc\\Desktop\\Pythonworks\\dataset\\words1.txt","r")
f_pallindrome=open("C:\\Users\\pc\Desktop\\Pythonworks\\dataset\\pallindrome.txt","w")

for words in f:
    words=words.rstrip("\n")

    reversed_word=words[::-1]

    if reversed_word==words:

        f_pallindrome.write(words+"\n")
f.close()


f_pallindrome.close()
        
    