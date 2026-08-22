print("homework tracker")
total_homework = 4
original_count = total_homework
print("you have ",original_count," homeworks left")
completed_tasks = 0
task_num = 1
while task_num <= total_home3work:
    if task_num == 1:
        next_task = "maths"
    elif task_num == 2:
        next_task = "english"
    elif task_num == 3:
        next_task = "science"
    else:
        next_task = "maths"
    a = input("did you complete",next_task,"? (yes / no)")
    b = a.lower()
    if b == "yes":
        completed_tasks = completed_tasks + 1
        total_homework = total_homework - 1
        print("goodjob!complete the other ")
    else:
        print("okay do it first then come and check it")
    print("homework tasks remaining ",total_homework - completed_tasks)
    print()
print("congarts you can do other things now")
# PART 8: A different look at how an infinite loop operates safely
print("Simulating a video game loop that has no natural exit...")
game_over = False
loop_guard = 0

while game_over == False:
    print("Game frame rendering... Processing background logic endlessly!")
    loop_guard += 1
    
    if loop_guard == 3:
        print("[SAFETY CONTROLLER]: Intercepted infinite loop to prevent a crash.")
        break
print("\n================ PROGRESS OVERVIEW ================")
print("Total Tasks Assigned Initialized:", original_count)
print("Successfully Finished Items:", completed_tasks)
print("Pending Assignments Left:", total_homework - completed_tasks)
print("===================================================")

    