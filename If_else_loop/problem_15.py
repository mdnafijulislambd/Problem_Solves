# Create a grade calculator using if-elif-else.

mark = int(input("Enter your mark : "))

if mark < 0:
    print("Invalid Input")
elif mark >= 80 :
    print("Your Grade A+")
elif mark >= 70 :
    print("Your Grade A")
elif mark >= 60 :
    print("Your Grade B")
elif mark >= 50 :
    print("Your Grade C")
elif mark >= 40 :
    print("Your Grade D")
else:
    print("Your Grade F")