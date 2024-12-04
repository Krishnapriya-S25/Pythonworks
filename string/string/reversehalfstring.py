text="hellopython"
x=text.index("o")
reversed_string=text[x-1::-1]
balance=text[x:]
result=reversed_string+balance
print(result)