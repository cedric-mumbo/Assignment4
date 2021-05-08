# A typical example of a nested if statement
number = int(input("Enter number"))
if number % 2 == 0:
    if number % 3 == 0:
        print("Divisible by 3 and 2")
    else:
        print("Divisible by 2 not Divisible by 3")
    if number % 3 == 0:
        print("Divisible by 3 not by 2")
    else:
        print("not divisible by 2 not divisible by 3")

