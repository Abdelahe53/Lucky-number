import random  # Import the "random" library

print("If you get lucky 13 on the first try, you are the luckiest person!")  # Print a message

lucky_num = 13

while True:
    random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    print("Your number is:", random_number)  # Display the random number

    if random_number == lucky_num:
        print("You're lucky ma boi!")
        break
    else:
        input("99% of gamblers quit before they win big, try again...")
