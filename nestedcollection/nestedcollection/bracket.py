user_input=input("enter brackets")
symbol_dictionary={"{":"}","(":")","[":"]"}
symbal_stack=[]
top=-1
is_valid=True
for symbol in user_input:
    if symbol in symbol_dictionary:#symbol is opening
        top=top+1
        symbal_stack.append(symbol)
    elif top==-1:
        is_valid=False
    elif symbol==symbol_dictionary.get(symbal_stack[top]):#symbol==value of symbol in top of the stack

        top=top-1
        symbal_stack.pop()
    else:
        is_valid=False

if len(symbal_stack)==0:#stack is empty or top=-1

    print("valid")
else:
    print("invalid")


    


        



    
    
    


