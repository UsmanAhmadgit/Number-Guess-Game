import random

n = random.randint(1, 100)
a = -1
guesses = 1
while a != n:
    a = int(input("Guess the number(Between 1 and 100): "))
    if a < n:
        print("Higher number please")
        guesses += 1
    elif a > n:
        print("Lower number please")
        guesses += 1
print(f"You have guessed the number {n} in {guesses} attempts")
