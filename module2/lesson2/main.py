#operator precedence:
#PEMDAS:Parentheses,Exponent,Multiplication, Divide, Add & Subtract
#activity1:
# sum=12+25+50+20+15 #122- wrong sum 122/5 122-(20-40) 122-(-20) 122+20=142
# sum1=12+25+50+40+15 #142 -correct sum 142/5


mean1 = 38
wrong_number = 36
correct_number = 56
total_number = 40
wrong_sum =mean1*total_number
correct_sum= wrong_sum-(wrong_number-correct_number)
correct_mean=correct_sum/total_number
print(correct_mean)


# Activity 1:
# WHAT YOU WILL BUILD
# You calculate one expression using PEMDAS, then test a condition that mixes and and or
# together, to see Python's precedence rules in action for both.
# HOW IT WORKS
# Step 1: Store v = 4, w = 5, x = 8, y = 2, then calculate z = (v + w) * x / y, following PEMDAS -
# parentheses first, then multiply, then divide.
# Step 2: Print the value of z with a message - it comes out to 36.0.
# Step 3: Store name = "Alex" and age = 0.
# Step 4: Check name == "Alex" or name == "John" and age >= 2 - since and is checked before or,
# this becomes True the moment name equals "Alex" alone, and print "Hello! Welcome."

# Activity 2: Divisible Number

# WHAT YOU WILL BUILD
# You take two numbers as input and use the modulus operator to check whether the first divides
# evenly into the second.

# HOW IT WORKS
# Step 1: Ask the user to enter a numerator and store it in numn.
# Step 2: Ask the user to enter a denominator and store it in numd.
# Step 3: Check numn % numd == 0 - if the remainder is exactly 0, print that numn is divisible by
# numd.
# Step 4: Otherwise, print that numn is not divisible by numd.

# Activity 3: Mean Value

# WHAT YOU WILL BUILD
# You correct a wrongly-calculated mean by rebuilding the original sum, swapping in the correct
# number, and recalculating.
# HOW IT WORKS
# Step 1: Store mean1 = 38, wrong_number = 36, correct_number = 56, and total_number = 40.
# Step 2: Rebuild the original sum using sum = mean1 * total_number, and print it - this comes out
# to 1520.
# Step 3: Correct the sum using num2 = sum - ((wrong_number) - (correct_number)), and print it -
# this comes out to 1540.
# Step 4: Calculate the corrected mean using mean2 = num2 / total_number, and print it - this
# comes out to 38.5.

# Activity 4: Average speed

# WHAT YOU WILL BUILD
# You take three speeds as input, calculate their average, then use a chain of elif conditions to
# describe exactly which of the three the average beats.

# HOW IT WORKS
# Step 1: Take three values as input and store them in a, b, and c.
# Step 2: Calculate avg = (a + b + c) /3, and print it.
# Step 3: Check avg against a, b, and c using a chain of elif conditions joined with and, from all
# three at once down to just one at a time.
# Step 4: If avg isn't strictly greater than any of the three, print "invalid input".
#Activity1:
v = 4
w = 5
x = 8
y = 2
z = (v + w) * x / y
print(z," - it comes out to 36")
name = "alex"
age = 0
if name == "alex" or name == "john" and age >= 0:
    print("hello, welcome!")
#Activity2:
a = int(input("num 1: "))
b = int(input("num 2: "))
c = a % b
if c == "0":
    print("num 1 can divide num 2")
else:
    print("num 1 cannot divide num 2")
#Activity4:
d = int(input("speed 1: "))
e = int(input("speed 2: "))
f = int(input("speed 3: "))
g = (d + e + f)/3
if d > g:
    print("speed1 beats average")
elif e > g:
    print("speed2 beats average")
elif f > g:
    print("speed3 beats average")

