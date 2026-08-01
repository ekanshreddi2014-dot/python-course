team_1 = int(input("points of team 1: "))
team_2 = int(input("points of team 2: "))
team_3 = int(input("points of team 3: "))
team_4 = int(input("points of team 4: "))
team_5 = int(input("points of team 5: "))
total = team_1 + team_2 + team_3 + team_4 + team_5
average = total/5
print("total points of all the teams: ",total)
print("average of all the teams: ",average)
aa = int(input("bonus points: "))
bb = int(input("negative points(in case missed tasks.): "))
total += aa
total -= bb
print("new score after bonus and negative markings: ")
a = int(input("stars per point: "))
b = total*a
print("no. of stars: ",b)
c = b//25
d = b%25
print("boxes packed: ",c)
print("leftover: ",d)
x = int(input("last week's scores: "))
if total < x:
  print("last week's scores were better")
elif total > x:
  print("this week's scores were better")
else:
  print("the scores were the same")
