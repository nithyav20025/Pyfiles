#List with diffrent category

fav_fruits=["Mango","Apple","Banana","Pineapple"]
fav_vegetables=["Carrot","Beans","Beetroot","Onion"]
fav_food=["Dosa","Biriyani","Pizza","Idly"]

print("Fruits:",fav_fruits)
print("Vegetables:",fav_vegetables)
print("Food:",fav_food)

#list methods

fav_fruits.append("Orange")
print("After append",fav_fruits)

fav_vegetables.insert(1,"Cabbage")
print("After insert",fav_vegetables)

fav_food.remove("Pizza")
print("After remove",fav_food)

fav_food.sort()
print("After sort",fav_food)

fav_fruits.pop()
print("After pop",fav_fruits)

fav_food.reverse()
print("After reverse",fav_food)

fav_fruits.clear()
print("After clear",fav_fruits)

print("count",fav_food.count('Idly'))

print("count",len('Carrot'))

#list slicing

print("Top 2 food", fav_food[0:2])

print("Last 2 fruits", fav_food[-2:])

#list iteration

for food in fav_food:
    print("Menu",food)