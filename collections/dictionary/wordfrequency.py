text="ABABBCCDDE"
character_count={ ch:text.count(ch) for ch in text}
print(character_count)
# for k,v in character_count.items():
#     if v==1:
#         print(k)
non_recursive_character=[k for k,v in character_count.items() if v==1]
print(non_recursive_character)

        


