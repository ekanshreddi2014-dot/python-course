a = int(input("todays temperature: "))
b = input("is it raining: ")
c = int(input("how many minutes did you study today: "))
d = int(input("how much free time did you have today in minutes: "))
if a > 40:
  aa = "play indoors"
  print("it is too hot today , you should stick to indoor games")
else:
  aa = "play outdoors"
  print("you can play outside")
if b == "yes":
  ab = "don't play outside as its raining"
  print("you shouldnt play outside")
else:
  ab = "you can play as it's not raining"
if c > 90:
  ac = "need brake"
  print("you can take rest")
else:
  ac = "dont need brake"
  print("you need to study")
if d > 120:
  ad = "hobby time"
  print("you have enough free time to enjoy your hobby time ")
else:
  ad = "planning time"
  print("you dont have enough free time use some time for planning")
print("  ")
print("daily activity check completed")
print("here is the final summary")
print("todays temeperature is ",a,",so you should ",aa)
print(ab)
print("today you studied for ",c,",so you ",ac)
print("your free time today is ",d,",so you need ",ad)
