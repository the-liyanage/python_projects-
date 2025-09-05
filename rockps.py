#has to be two players -> computer and user
#take two inputs
#compare the inputs 
#tell who won 

import random


print("Hello, Welcome to the Rock paper scissor game")
while True:
    you_want = input("Do you want to play the game?\nType y for yes and n for no: ").lower()
    if you_want =='n':
        break
    #taking computer input y

    computer_input_choices =['rock', 'paper', 'scissors']
    computer_input = random.choice(computer_input_choices)
    print(computer_input)
     
    #taking user input
    user_input = input("type rock, scissors or paper:  ").lower()
    print(user_input, computer_input)         
    
    #comparing
    if computer_input == user_input:
        print(" It is a draw!")
    elif (computer_input =='rock' and user_input == 'scissors') or \
         (computer_input == 'scissors' and user_input =='paper') or \
         (computer_input == 'paper' and user_input == 'rock'):
         print("computer wins!") 
    else:
        print('you win!')


