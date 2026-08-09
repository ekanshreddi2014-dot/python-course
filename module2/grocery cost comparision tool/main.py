rice = int(input("cost of rice: "))
milk = int(input("cost of rice: "))
fruit = int(input("cost of rice: "))
number_of_baskets = int(input("cost of rice: "))
family_members = int(input("cost of rice: "))
basket_cost_per_person = (rice + milk + fruit) * number_of_baskets / family_members
print("grocery cost per person",basket_cost_per_person)
a = int(input("enter total number of grocery items"))
b = int(input("enter total number of family members"))
if a % b == 0:
    print(a,"items can equally be divided among",b,"people")
else:
     print(a,"items cannot equally be divided among",b,"people")
recordedaverage = 65
wrongweeekcost = 50
correctweekcost = 80
totalweeks = 4
recordedtotal = recordedaverage * totalweeks