#dictionary: it is a colllection of data stored in key - value pairs , wrapped inside curly brackets with a colon seperating every key from its matching value.
#example:
student = {"name":"six-seven","age":20}
print(student["name"])
print(student.get("age"))
student["age"]=12
print(student["age"])
student["city"]="vishakapatnam"
print(student)
student.pop("age")
print(student)
# student.clear()
# print(student)
print(len(student))
for key,i in student.items():
    print(key, ":",i)
#activity:
# Get rid of the duplicates
# Outline:
# First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest.
# Project:
# https://codingal.s3.ap-south-1.amazonaws.com/media/blackops/lesson-plan-assets/All_About_Dictionary_bpc-f68f.zip
# Check the frequency
# Outline:
# Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.
# Project:
# https://codingal.s3.ap-south-1.amazonaws.com/media/blackops/lesson-plan-assets/All_About_Dictionary_bpc-f68f.zip
# Get the country code
# Outline:
# Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.
# Project:
# https://codingal.s3.ap-south-1.amazonaws.com/media/blackops/lesson-plan-assets/All_About_Dictionary_bpc-f68f.zip