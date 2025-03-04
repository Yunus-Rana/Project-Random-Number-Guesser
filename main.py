import random

number = random.randint(1,25)
attempts = 0

while True:
    n = int(input("Enter the number: "))
    if n < 1 or n > 25:
        print("Invalid number. Try again! ")
        continue
    attempts = attempts + 1   

    if number > n:
        print("Your number is lower than computer's number. ")
    elif number < n:
        print("Your number is higher than computer's number. ")
    else:
        print(f"You have won the game in {attempts} tries.")
        break