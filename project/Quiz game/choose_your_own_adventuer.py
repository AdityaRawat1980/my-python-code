name = input("type your name :- ")
print("welcome", name ," to this advanture !")
answer = input("you are on a dirt road , it come to an end and you can go left or right or which way you like to go ? ")
if answer == "left":
    answer = input("you come to an river , you can walk it or swim accross ? type walk to walk or swim to swim")
    if answer == "swim" :
        print("you swim acrross and were eaten by alligator.")
    elif answer == "walk":
        print("you walked for many miles, run out of water and you lost the game")
    else:
        print("you choise a wrong way.......... you lose......")
elif answer == "right":
    answer = input("you come to a bridge , it looks wobbly , do you want to cross it or head back (cross/back) ? ")
    if answer == "back":
        print("you are back to main road. and you lose")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger. Do you talk with him (yes/No) ?  ")
        if answer == "yes":
            print("you talk to the stranger and they give you gold .....you won")
        elif answer == "No":
            print("you ingnor the stranger and they are offended and you lose....")
        else:
            print("not a valid option......you lose......")
else :
    print("you choise a wrong way.......... you lose......")

print("thank you for trying ", name)