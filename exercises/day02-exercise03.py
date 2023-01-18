# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
year_limit = 90
age_int = int(age)

month = (year_limit * 12) - (age_int * 12)
week = (year_limit * 52) - (age_int * 52)
day = (year_limit * 365) - (age_int * 365)

message = (f"You have {day} days, {week} weeks, and {month} months left.")

print(message)