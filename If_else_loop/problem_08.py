# Print the following pattern:
# *
# **
# ***
# ****
# *****

num = int(input("Enter the number : "))

for i in range(1, num+1):
    star = ("*"*i)
    print(star)