#set:set is a collection item where every item is unique and unordered .
#example:
import array as arr
# fruits = {"apple","banana","avacado","bluebereis","avacado"}
# print(fruits)
# fruits.add("strawberry")
# print(fruits)
# fruits.update(["orange","walnut","coconut"])
# print(fruits)
# a = {1,3,5,7,8,9}
# b = {2,4,6,8,9}
# print(a.intersection(b))
# print(a & b)
#array:array is a collection of items
#that are all the exact same data type stored one fter anothe rin a fixed order
#example:
a = arr.array("i",[1,2,3,5])
print(a)
a.append(4)
print(a)
a.insert(0,5)
print(a)
print(len(a))
print(a.count(5))
a.reverse()
print(a)
