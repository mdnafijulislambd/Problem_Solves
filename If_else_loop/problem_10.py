# Create a simple login system. Username: admin Password: 1234

username = input("Enter your username : ")
password = input("Enter your password : ")

current_use = "admin"
current_pass = "1234"


if username == current_use and password == current_pass: 
   print("Valid User")
else:
   print("Invalid User")