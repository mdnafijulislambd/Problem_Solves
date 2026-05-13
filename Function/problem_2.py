def is_vowels(n):
    count = 0
    for i in n:
        if i in "AEIOUaeiou":
            count += 1
    return count
Srt=input("Enter a String: ")
print(is_vowels(Srt))