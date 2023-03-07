import random
def BattleGame(computer , you):
    if(computer == you):
        return None
    elif(computer == 'r'):
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif(computer == 'p'):
        if you == 's':
            return True
        elif you == 'r':
            return False    
    elif(computer == 's'):
        if you == 'r':
            return True
        elif you == 'p':
            return False


Random_Num = random.randint(1,3)
print("Computer turn: Rock('r') , Paper('p') , Scissor('s'): ")
if(Random_Num == 1):
    computer = 'r'
elif(Random_Num == 2):
    computer = 'p'
else:
    computer = 's'

you = input("Your turn : Rock('r') , Paper('p') , Scissor('s') : ")
result = BattleGame(computer , you)

print(f"Computer chose {computer}")
print(f"You chose {you}")

if result == None:
    print("The game is a tie!!")
elif result:
    print("You Win :)")
else:
    print("You Lose :(")
    