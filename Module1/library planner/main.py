print("=== Library Visit Planner ===")
a = input("What day is it today? ")
b = input("What is today's weather like? (sunny/rainy/cloudy): ")
c = input("Does a book need to be returned? (yes/no): ")
dd = a.strip().lower()
ss = b.strip().lower()
aa = c.strip().lower()
if dd in ("saturday", "sunday"):
    print("It's a weekend.")
elif dd in ("monday", "tuesday", "wednesday", "thursday", "friday"):
    print("It's a regular school day.")
else:
    print("Please be more specific with the day.")
if ss == "sunny" and aa == "yes":
    print("Since the conditions are perfect, you should go return the book!")
if ss == "rainy" or ss == "cloudy":
    print("Take an umbrella!")
if not (aa == "yes"):
    print("No book needs to be returned today.")
if ss == "rainy" and aa == "yes":
    print("Best plan  : Visit the library carefully and return your book on time.")
elif ss == "sunny" and aa == "yes" and not (dd in ("saturday", "sunday")):
    print("Best plan  : Stop by the library after school and return your book.")
elif dd in ("saturday", "sunday") and ss == "sunny":
    print("Best plan  : Perfect day for a longer reading session at the library!")
else:
    print("Best plan  : Check your schedule and plan a simple library visit.")
print()
print("Library return planning complete!")
