print("===librry visit planner===")
a = input("what day it it today?")
b = input("whatis today's wheather like today?(sunny/rainy)")
c = input("does a book need to be returned?")
dd = a.strip().lower().capitalize()
ss = b.strip().lower().capitalize()
aa = c.strip().lower().capitalize()
if dd == "Saturday"or dd == "Sunday":
    print("its a weekend")
elif dd ==  "Monday"or dd == "Tuesday"or dd == "Wednesday"or dd == "Thursday"or dd == "Friday":
    print("its a regular school day")
else:
    print("please be more specific")
if (ss == "sunny")and(aa == "yes"):
    print("since the conditions are perfect you should go return the book")
else:
    print("you should stay at home today")
if ss == "rainy" or ss == "cloudy":
    print("take an umbrella")
if not(aa == "yes"):
    print("no book needs to be returned today")
if ss == ""

    
    
