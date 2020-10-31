import random

def name_to_number(name):
    if(name=="rock"):
        return 0
    elif(name=="spock"):
        return 1
    elif(name=="paper"):
        return 2
    elif(name=="lizard"):
        return 3
    elif(name=="scissors"):
        return 4
    else:
        return "Error: Incorrect Choice"
    
def number_to_name(num):
    if(num==0):
        return "rock"
    elif(num==1):
        return "spock"
    elif(num==2):
        return "paper"
    elif(num==3):
        return "lizard"
    elif(num==4):
        return "scissors"
    else:
        return "Error: Incorrect Choice"
    

def rpsls(players_choice):
    print()
    print("Your choice is "+players_choice)
    player_number=name_to_number(players_choice)
    comp_choice=random.randrange(0,5)
    comp=number_to_name(comp_choice)
    print("Computer's choice is "+comp)
    difference = (comp_choice- player_number) % 5
    if (difference == 0):
        print("Player and computer tie!")
    elif (difference == 1) or (difference == 2):
        print("Computer wins!")
    else:
        print("Player wins!")

print("Please choose one of the options-")
print("rock  spock  paper  scissors  lizard")
players_choice= input("Your choice: ")
rpsls(players_choice)