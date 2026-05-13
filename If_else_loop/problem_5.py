# Print the multiplication table of a number.

num = int(input("Enter the number for multiplication : "))

for i in range(1, 11):
    multi = (num * i)
    print(f"{i} * {num} = {multi}")