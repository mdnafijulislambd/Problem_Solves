#  Check whether a person is eligible for voting.

age = int(input("Enter your age : "))

if age >= 18 and age <= 150:
    print("You are eligible for voting")
elif age > 150 or age < 0:
    print("Invalid input")
else:
    print("You are not eligible for voting")
