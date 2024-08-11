import random #used the "random" library

print("If you got lucky 13 in the first try you are the luckiest person") #there is nothing to explain in this line a zbay, just a normal print 
input("Tap `Enter` to try your luck: ") #this is the input u fucking iliterate where you can tap `Enter` to get the fucking number
random_number = random.randint(1, 100) #I used a range between 1 to 100 to give you hope.
print("Your number is:", random_number) #here it gives you a random number

number = random_number #number is a fucking random number

#THIS LOOP IS ALREADY FUCKED SO NOTHING TO EXPLAIN
while True:
    if number == 13:
        print("You are the luckiest person on earth")
        break
print("Bad luck D:")
