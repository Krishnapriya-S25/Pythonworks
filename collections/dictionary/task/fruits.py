

fruits = ["Apple", "Orange" , "Pineapple"]
price = [80,90,60]

details ={fruits[i]:price[i] for i in range(len(fruits))}

print(details)