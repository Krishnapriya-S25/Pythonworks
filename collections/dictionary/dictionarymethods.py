employee={"id":123,"name":"govind","department":"it","age":23,"salary":45000}
print(employee["salary"])
#get(key)
print(employee.get("name"))
#invalid key return none

#pop(key) remove a keY value pair
employee.pop("salary")
print(employee)

#keys()  return all keys
for k in employee.keys():
    print(k)

#values() return all values:
for v in employee.values():
    print(v)

#fetch keys and values:
for k,v in employee.items():
    print(k,v)




