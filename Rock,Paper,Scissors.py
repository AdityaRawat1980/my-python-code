import random
user_win = 0 
computer_win = 0 
options = ["rock","paper","scissors"]

while True :
    user_input =input("type any of them (Rock, Paper,Scissors, for Q to quuit the game) :- ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("please enter the right value") # hi my self adi
        continue

    rendom_number = random.randint(0,2)
    # hear rock = 0
    # hear paper = 1
    # hear scissors = 2
    computer_pick = options[rendom_number]
    print("comnputer picked :- ",computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("you did it (you won)")
        user_win += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("you did it ( you won )")
        user_win += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("you did it ( you won )")
        user_win += 1
    else:
        print("batter luck next time (you lost )")
        computer_win += 1

print("yours win :- ",user_win)
print("computers win ",computer_win)
print("Goodbye ! ")

