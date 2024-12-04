#create a fn that accept any number and return secondlargest

def second_largest(*args):
    sorted_number=sorted(args,reverse=True)
    return sorted_number[1]
print(second_largest(10,2,70,40))
print(second_largest(30,40,6))