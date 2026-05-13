# Find the largest among three numbers.

num1 = float(input("Enter the 1st num : "))
num2 = float(input("Enter the 2nd num : "))
num3 = float(input("Enter the 3rd num : "))

if (num1 >= num2)  and (num1 >= num3):
    print(f"largest num is {num1}")
elif (num2 >= num1)  and (num2 >= num3):
    print(f"largest num is {num2}")
else:
    print(f"largest num is {num3}")