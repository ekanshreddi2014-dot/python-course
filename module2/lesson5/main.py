#while loop : this kind of loop only loops as long as the given conditions stays true and stops when the condition becomes false.it is also used when we dont know in advance how many times the loop will run.
#syntax:
#while (condition):
#statement
#example:
# lives = 3
# while lives > 0:
#     print("you are alive")
#     # lives = lives - 1
# print("game over")
#activity:
# WHAT YOU WILL BUILD

# You build a chore checklist countdown that asks about each chore one at a time using a while

# loop, retries any chore marked not done, then prints a final summary once every chore is

# complete.

# HOW IT WORKS

# Step 1: Set total_chores to 4, store it as original_count, and print how many chores are on today's

# list.

# Step 2: Set up a completed_count counter starting at 0 and a chore_num counter starting at 1.

# Step 3: Start a while loop that keeps running as long as chore_num is less than or equal to

# total_chores.

# Step 4: Inside the loop, work out the current chore's name from chore_num, then ask if it has

# been finished.

# Step 5: If the answer is yes, increase completed_count and chore_num by 1; otherwise, print a

# message and let the loop ask about the same chore again.

# Step 6: Once the while loop ends, print the completion message, then safely demonstrate an

# infinite loop's condition, using a break to stop it after 3 rounds.

# Step 7: Print the final chore checklist summary showing chores assigned, completed, and

# remaining.

original_count = 4
print("there are 4 chores to be done today")
print("chore to be done:" \
      "cleaning the dishes" \
      "cleaning your room" \
      "watering the plants" \
      "dusting then hall ")
completed_counter = 0
chore_num = 1
while chore_num <= original_count:
    chore_1 = input("did you complete dishes: ")
    chore_2 = input("did you clean your room: ")
    chore_3 = input("did you complete water the plants: ")
    chore_4 = input("did you dust the hall: ")
    print("answer in yes/no")
    if chore_1 == "yes":
        original_count = original_count - 1
        completed_count = completed_counter + 1
    if chore_2 == "yes":
            original_count = original_count - 1
            completed_count = completed_counter + 1
    if chore_3 == "yes":
            original_count = original_count - 1
            completed_count = completed_counter + 1
    if chore_4 == "yes":
            original_count = original_count - 1
            completed_count = completed_counter + 1
    print("you have ",original_count," chores to do")
print("chore checklist")
print("cleaning the dishes : ",chore_1)
print("cleaning your room : ",chore_2)    
print("watering the plants : ",chore_3)    
print("dusting the hall : ",chore_4)
if chore_1 == "yes" and chore_2 == "yes" and chore_3 == "yes" and chore_4 == "yes":
      print("congrats all your chores for today have been completed")       
