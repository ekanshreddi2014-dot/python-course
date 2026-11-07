#list comprehension:it s a short method to make a new list from an old one and we can also 
#add conditions.(what to do for item in list)
#example:
a = [1,2,3,4]
square = [n*n for n in a]
print(square)
#dictionary comprehension:dictionary comprehension is also a short method to make a new dictionary 
#by paring upkeys with their matching values.
#example:
items = ["pencil","eraser"]
stock = [12,0]
inventory = {item:stock for item in items }
print(inventory)