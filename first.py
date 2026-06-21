# quiz game starts here 

perm = input("Do you want to play the game? ").lower()
score = 0


if perm == "yes":
    name = input("Type your name to continue: ")
    print(f"Hi, {name}\n")
    quiz_1 = input("What does CNN stand for?: ").lower()
    quiz_2 = input("What does RNN stand for?: ").lower()
    quiz_3 = input("What does LSTM stand for?: ").lower()

    if quiz_1 == "convolutional neural network":
        print("You're correct!")
        score +=1
    if quiz_2 == "recurrent neural network":
        print("You are correct!")
        score +=1
    if quiz_3 == "long short term memory":
        print("You are correct!")
        score +=1
else:
    quit()


print(f"You got {score} correct.")