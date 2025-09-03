import random 

random_number = random.randrange(1,11)
print(random_number)

while True:
        guess = (input("Guess the number: "))
        if guess.isdigit():
            guess = int(guess)
        else:
            print(" Please type a number next time")
            continue

        if guess > random_number:
            print("You are on the upper bound")
        elif guess < random_number:
            print("You are on the lower bound")
        else:
            print("Your guess is correct!") 
            break

                

