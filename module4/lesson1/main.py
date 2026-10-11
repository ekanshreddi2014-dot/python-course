#data structure: it is a way of organizing and storing a collection of data so it can be managed and used efficiently.python gives several built data structures including lists , tuples , dictionaries and sets .each organizing data in its own way
#list:a list is an ordered collection of items enclosed in sqaure brackets.its items can be changed added or removed at any time.it can store multiple data types as its items.
#example:
# a = [1,2,3,4,5,"a","b","c",True,False,3.123]
# print(a)
# print(len(a))#len(): is used to tell you how many items a list contains.
# print(a[7])#indexing: retrieves one exact item from a listusing its position number . it starts from zero.
# #slicing: slicing means pulling out or retrieving a whole connected range of items from a list.
# #example:
# print(a[2:5])
# #iterating: iterating means using a loop to visit every single item in a list one at a time in a order.
# #example:
# for i in a:
#     print(i)
#.sort(): it arranges items in asscending order.
#solution:
# Lists
# Outline:
# Write a program to perform the following operations on a List: 1. Create an empty list 2. A list with elements 3. Use * operator 4. Reverse a list
# Project:
# Word Matching
# Outline:
# Write a Python program to count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings.
# # Project:
# # Play with Lists
# # Outline:
# # Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list.
# # Project:
#solution1:
a = []
print()
b = [1,2,3,4,5,6,7,8,9,10]
print(b)
c = [1,2,3,4,5]*3
print(c)
d = [2,4,6,8,10]
print(d[::-1])
#solution2:
