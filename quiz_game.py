print("Welcome to my Computer Science trivia question game!")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's start playing!")

# count 
count = 0 
quiz_1 = input("Who is known as the father of computer science?: ")
if quiz_1.lower() == "alan turning":
    print("Correct!")
    count +=1
else :
    print("Incorrect!")  

quiz_2 = input("What does \"HTTP\" stand for?: ")
if quiz_2.lower() == "hypertext transfer protocol":
    print("Correct!")
    count +=1
else :
    print("Incorrect!")  

quiz_3 = input("What does \"URL\" stand for?: ")
if quiz_3.lower() == "uniform resource locator":
    print("Correct!")
    count +=1
else :
    print("Incorrect!")  

quiz_4 = input("What does \"IP\" in IP address stand for?: ")
if quiz_4.lower() == "internet protocol":
    print("Correct!")
    count +=1
else :
    print("Incorrect!")  


print(f"The count is {count}")     

print(f"Your percentage is {count/4*100}%")  
