text="ABAABBC"
#most recursive character 
#non recursive character
def get_count(ch):
    return text.count(ch)
frequent_ch=(max(text,key=get_count))
print(frequent_ch)
min_recursive_character=(min(text,key=get_count))
print(min_recursive_character)




