#nested loops : nested loops are loops which are in one-another.
#nested while loops: a while loop which is in another while or for loop.
#example:
# i = 1
# while i <= 5:
#     j = 1
#     while j <= 10:
#         print(j,end=" ")
#         j = j + 1
#     print()
#     i = i + 1
#nested for loops: a for loop which is in another for or while loop.
#example:
# for i in range(1,5):
#     for j in range(1,11):
#         print(j,end=" ")
#     print()
#activity:
# ATM Cash Dispenser
# Outline:
# This one activity keeps you working with both nested loop types end to end - a daily ATM session that serves several customers, then a denomination report printed once the day is done.
# WHAT YOU WILL BUILD

# You build a program that serves customers one at a time at an ATM, breaking each withdrawal

# into notes, then prints a daily denomination report once the session ends.

# HOW IT WORKS

# Step 1: Set up six counter variables (one per note value) plus counters for customers served and

# total dispensed, all starting at 0.

# Step 2: Start an outer while loop that keeps serving customers until the flag variable serving

# becomes False.

# Step 3: Ask for the customer's name and withdrawal amount; if the amount is invalid, print a

# message and continue back to the top of the loop.

# Step 4: Inside that same repeat, run an inner while loop that checks each of the six note values

# one at a time and works out how many of each note to dispense.

# Step 5: Update the matching counter variable for whichever note value was just dispensed, then

# ask if there is a next customer, setting serving to False if not.

# Step 6: Once the outer while loop ends, start an outer for loop stepping through each of the six

# note values to print the daily denomination report.

# Step 7: Inside that same repeat, run an inner for loop that prints one symbol for every note of that

# # value dispensed across the whole day.
#solution:
a = 1
b = 10
c = 50
d = 100
e = 500
f = 1000
a3 = 0
b3 = 0
c3 = 0
d3 = 0
e3 = 0
f3 = 0
customers_served = 0
total_dispensed = 0
flag = True
while flag == True:
    customer_name = input("what's your name ? : ")
    withdrawel_amount = int(input(f"How much do you want to withdraw, {customer_name}? "))
    if withdrawel_amount <= 0:
       print("invalid amount please try again")
       continue
    a1 = withdrawel_amount // f
    a2 = withdrawel_amount % f
    b1 = a2 // e
    b2 = a2 % e
    c1 = b2 // d
    c2 = b2 % d
    d1 = c2 // c
    d2 = c2 % c
    e1 = d2 // b
    e2 = d2 % b
    f1 = e2 // a
    f2 = e2 % a
    if f2 == 0:
        print(f"\n--- Dispensed for {customer_name} ---\n"
      f"1000 rupee notes: {a1}\n"
      f"500 rupee notes: {b1}\n"
      f"100 rupee notes: {c1}\n"
      f"50 rupee notes: {d1}\n"
      f"10 rupee notes: {e1}\n"
      f"1 rupee notes: {f1}")
    a3 = a3 + a1
    b3 = b3 + b1
    c3 = c3 + c1
    d3 = d3 + d1
    e3 = e3 + e1
    f3 = f3 + f1   
    question = input("if there a customer behind you ? (yes / no)")
    if question == "yes":
        flag = True
    else:
        flag = False
    if flag == False:
        continue
print("dispensing report for the day : ")
print("1000 rupee notes dispensed : ",a3,)
print("500 rupee notes dispensed : ",b3,)
print("100 rupee notes dispensed : ",c3,)
print("50 rupee notes dispensed : ",d3,)
print("10 rupee notes dispensed : ",e3,)
print("1 rupee notes dispensed : ",f3)
print("=== daily visual dnomination report ===")
print("\n===== DAILY DENOMINATION REPORT =====")
print("1000 rupee notes: ",end="")  
for i in range(a3):                  
    print("*",end="")              
print()                              
print("500 rupee notes: ", end="")
for j in range(b3):
    print("*", end="")
print()
print("100 rupee notes: ", end="")
for k in range(c3):
    print("*", end="")
print()
print("50 rupee notes: ", end="")
for l in range(d3):
    print("*", end="")
print("10 rupee notes: ", end="")
for m in range(e3):
    print("*", end="")
print()
print("1 rupee notes: ", end="")
for n in range(f3):
    print("*", end="")
print()
