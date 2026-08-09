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
print("recorded total is",recordedtotal)
correcttotal = (recordedtotal - wrongweeekcost + correctweekcost)
print("corrected grocery total",correcttotal)
correctedaverage = correctet / totalweeks
print("corrected weekly average: ",correctedaverage)
store_a_average = 70
store_b_average = 75
store_c_average = 80
print("store_a_average: ",store_a_average)
print("store_b_average: ",store_b_average)
print("store_c_average: ",store_c_average)
# Compare the corrected average with three values
if correctedaverage < store_a_average and correctedaverage < store_b_average and correctedaverage < store_c_average:
    print("Your corrected grocery average is lower than all three store averages.")
elif correctedaverage > store_a_average and correctedaverage > store_b_average and correctedaverage > store_c_average:
    print("Your corrected grocery average is higher than all three store averages.")
else:
    print("Your corrected grocery average is between the three store averages.")
