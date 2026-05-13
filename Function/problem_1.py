def fact(n):
    A = 1
    if n < 0:
        return("Invalid input ")
    else:
        for i in range(1, n+1):
            A *= i 
        return(A)

num = int(input("Enter a num : "))
print(f"The factorial is {fact(num)}")

