import random 

random_number = random.randrange(1,11)
print(random_number)

guess_num = 0
while True:
        guess_num += 1
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
print("You got it in", guess_num, "guesses")
                

