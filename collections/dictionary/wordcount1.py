text="ABBACB"
#print character count
character_count={}
for ch in text:

    if ch in character_count:

        character_count[ch]+=1
    else:
        character_count[ch]=1
print(character_count)

if character_count[ch]>1:
    print(ch,"first recursive")
