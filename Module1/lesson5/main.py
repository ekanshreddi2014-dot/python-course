print("hello farmer.Can you give me the details")
a = int(input("harvest of field 1 in kg:"))
b = int(input("harvest of field 2 in kg:"))
c = int(input("harvest of field 3 in kg:"))
d = int(input("harvest of field 4 in kg:"))
e = int(input("harvest of field 5 in kg:"))
f = int(input("bonus crop and seed reserves:"))
g = int(input("last year's yield:"))
total = a + b + c + d + e + f + g
average = total/5
bags = total//25
leftover = total % 25
print("total crop: ",total)
print("average yield among all the fields: ",average)
print("number of bags the seeds can be packed into: ",bags)
print("leftover after packing in kg: ",leftover)
print("bonus crops in kg: ",f)
if total < g:
  print("last year's yeild was better")
elif total > g:
  print("this year's yeild is better")
else:
  print("both the years yeild is same")


