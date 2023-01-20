# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

combined_string = name1 + name2
lower_case_sring = combined_string.lower()

true = (lower_case_sring.count("t") +
        lower_case_sring.count("r") +
        lower_case_sring.count("u") +
        lower_case_sring.count("e"))

love = (lower_case_sring.count("l") +
        lower_case_sring.count("o") +
        lower_case_sring.count("v") +
        lower_case_sring.count("e"))

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(
        f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score > 40) and (love_score < 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
