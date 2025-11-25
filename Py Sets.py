n= ["Vicky","Nithu","Sree","Vignesh"]
print(n[3])

grocery=["Milk","Curd","Bread","Milk","Bread"]

edit_list=set(grocery)
print(edit_list)

grocery1= {"Milk","Curd","Bread"}
grocery2= {"Cheese","Carrot","Bread"}

print(grocery1.union(grocery2))
print(grocery1.intersection(grocery2))
print(grocery1.difference(grocery2))
print(grocery1.symmetric_difference(grocery2))

grocery1.add("Butter")
print(grocery1)

grocery2.remove("Cheese")
print(grocery2)
