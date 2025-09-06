import random

random_number = random.randint(0,1)

def next_stage():
    fourth_path = input("Do you choose golden or stone? (Type 'golden' or 'stone') ").lower() 
    if fourth_path == 'golden':
        print("Game over! You lost!")
    else:
        print("You are in the chamber now! Let's go in. You see the artifact glowing on a pedestal.")
        fifth_path = input("Do you grab it immediately or look first? (Type 'grab' or 'look') ").lower()
        if fifth_path == 'grab':
            print("Game over! you lost")
        else:
            print("You can take the artifact safely!, You must escape before the temple collapses!")
            final_path = input("Do you run or sneak? (Type 'run' or 'sneak') ").lower()
            if final_path =='run':
                if random_number == 1:
                    print("Oh that was a glorious escape! You win the game!")
                else:
                    print("You lost!")
            else:
                    print("You lost!")    

print("The lost temple!")
print("""You wake up at the edge of a dense jungle. Rumors say a Lost Temple inside hides a powerful artifact. 
But the jungle is full of danger.
Your mission: find the artifact and escape alive.""")

#First Choice



second_path = True

while second_path:
    first_path = input("Do you want to take the left path (river) or right path (jungle)? (Type 'left' or 'right')" ).lower()
    #River Path
    if first_path == 'left':
        print("You reach a raging river with a broken bridge")
        second_path = input("You have a choice to make now\nType bridge to cross the bridge or Type next to find another way! ").lower()
        if second_path == 'bridge':
            if random_number == 1:
                    print("You are inside the temple now!")
                    next_stage()
            else:
                print("You failed off from the bridge, Game over!")
        else:
            print("Let's find another way to go around!, You are closer to the temple now!") 
            next_stage()   
    elif first_path == 'right':
        print("Let's enter the Jungle!, You hear growling — a tiger appears!")
        second_path = input("Do you fight, climb, or run? (Type 'fight', 'climb', 'run')" ).lower()  
        if second_path == 'fight':
            if random_number == 1:
                print("You win! The game is over")
            else:
                print("Game over you lost!")    
        elif second_path == 'climb':
            print("You are safe to continue!, let's walk to the temple!") 
            next_stage()   
        elif second_path =='run':
            print("Go back to the beginning!")    

                   
