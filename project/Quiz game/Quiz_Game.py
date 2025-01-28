print("welcom to aditya's Quiz game (¬‿¬) :") # For welcoming the players
playing = input("Do you want to play game :- ") # in this we are taking the permission from the user 
if playing != "yes" :# hear we are chaking that the user want to play or not
    quit() #this statment will terminate the program if the condition is true

print("let's start playing (●'◡'●) :") # game is started hear
score = 0 # for calculating the score of the person we give the score varibal

# Qution no first

answer =input("what does the full from of nic card ?  ").lower()# we used the lower function to convert the whole code in lower case  (# we taken the input from the user as per the qustion)
if answer.lower() == "net working interface card":  # chaking the answer is correct or not (# .lower() function can also used hear tooo.....) 
    print("you are correct (¬_¬) ")  # if the answer is correct so it print correct
    score += 1 # hear we add the 1 to the score varibal if answer is correct
else:
    print("you are wrong (>_<) ")

# Qustion no second

answer =input("what does the full from of computer ?  ") # we taken the input from the user as per the qustion
if answer.lower() == "Common Operating Machine Purposely Used for Technological and Educational Research":  # chaking the answer is correct or not 
    print("you are correct (¬_¬) ")  # if the answer is correct so it print correct
    score += 1
else:
    print("you are wrong (>_<) ")

# Qution no third

answer =input("what does the full from of IOT ?  ") # we taken the input from the user as per the qustion
if answer.lower() == "Internet of Things":  # chaking the answer is correct or not 
    print("you are correct (¬_¬) ")  # if the answer is correct so it print correct
    score += 1
else:
    print("you are wrong (>_<) ")

# Qution no four

answer =input("what does the full from of SDLC ?  ") # we taken the input from the user as per the qustion
if answer.lower() == "Software Development Life Cycle ":  # chaking the answer is correct or not 
    print("you are correct (¬_¬) ")  # if the answer is correct so it print correct
    score += 1
else:
    print("you are wrong (>_<) ")

print("your score " +str(score) + " qustion correct")
print("your score " +str(4-score) + " qustion wrong")
print("your score " +str((score/4)*100) + "%")

