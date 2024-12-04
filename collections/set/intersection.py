st1={10,20,30,40,50}
st2={10,20,60,70,80}
intersection_set=st1.intersection(st2)
print(intersection_set)
#union of set
union_set=st1.union(st2)
print(union_set)

#difference
difference_set=st1.difference(st2)
print(difference_set)

#remove
st1.remove(50)
print(st1)

#issubset
st1={1,2,3}
st2={1,2,3,4,5}
print(st1.issubset(st2))

#superset
st1={1,2,3}
st2={1,2,3,4,5}
print(st2.issuperset(st1))

#symmetricdiff
st1={1,2,3}
st2={1,2,3,4,5}


syymmetric_difference=st1.symmetric_difference(st2)
print(syymmetric_difference)#(AUB)-(A^B)

#update
st1={1,2,3}
st2={1,2,3,4,5} 
st1.update(st2)
print(st1)

