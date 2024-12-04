#abs value
value = {"A" : -1, "B" : -5, "C" : 7, "D" : -8}
abslte = {k : abs(v) for k,v in value.items()}
print(abslte)