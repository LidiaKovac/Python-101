
import random
machine = random.randint(1, 3)
def choose(): 
    user_chosen = input("Press 1 for scissors, 2 for paper and 3 for rock. \n")
    user = int(user_chosen)
    if user == 1: 
        print(" User has chosen: Scissors")
    elif user == 2: 
        print(" User has chosen: Paper")
    elif user == 3: 
        print(" User has chosen: Rock")
    else: 
        print("Please choose a number between 1 and 3")

    if machine == 1: 
        print(" Computer has chosen: Scissors")
    elif machine == 2: 
        print(" Computer has chosen: Paper")
    elif machine == 3:
        print(" Computer has chosen: Rock")
    
    if (user == machine): 
        print("Draw!")
        choose()
    elif user == 1 and machine == 2: 
        print("User wins! ")
    elif user == 2 and machine == 3:
        print ("User wins! ")
    elif user == 3 and machine == 1:
        print ("User wins! ")
    else: 
        print("Computer wins! ")

choose()

