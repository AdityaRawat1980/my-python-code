import random # it is built in module in python
top_of_range =input("type any n'th number for genrat the rendom number : ")
if top_of_range.isdigit() : # isdigit function is only work on string values only
    top_of_range= int(top_of_range) # hear we perform type cast function
    if top_of_range <= 0: 
        print("please type a number larger than 0 ")
        quit()
else:
    print("please type a number not a string")
    quit()

# rendom_number = random.randrange(top_of_range) #in this it genrat the rendom numbers between tn 1 to 10 or print the n-1 values in the termanil
random_number = random.randint(0,top_of_range)  # it also include the last value too into the genration of rendom number
guesses = 0 # we are making a varibal for chacking how much time does user guse for geting right answer
while True:
    guesses+=1 # it will add one value to guesses when the loop star again and again , {so by that we track the no of time the user guesses the value}
    user_guess = input("make a guess : ")
    if user_guess.isdigit() : # isdigit function is only work on string values only
        user_guess = int(user_guess) # hear we perform type cast function 
    else:
        print("please type a number not a string")
        continue # this will continue the loop if no is stringg value 

    if user_guess is random_number :
        print("you got it (*^_^*) :")
        break # this will auto quit the program if the condition is becom true
    else: # you also use elif statment for this
        print("you got wrong ( *︾▽︾) :")
        if user_guess > random_number :
            print("you are above the number !! ")
        else:
            print("you are below the number !! ")

print("you guesses the number",guesses,"time to get correct one!!")

# for quit the program from terminal you just use(ctrl + c)

