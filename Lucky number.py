import random

print("If you got lucky 13 in the first try you are the luckiest person")
input("Tap `Enter` to try your luck: ")
random_number = random.randint(1, 100)
print("Your number is:", random_number)

number = random_number

while True:
    if number == 13:
        print("You are the luckiest person on earth")
        break
print("Bad luck D:")