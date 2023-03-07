import random
randNUM = random.randint(1,100)
print(randNUM)
UserGuess = None
Guesses = 0
while(UserGuess!=randNUM):
    UserGuess = int(input("Enter your number between 1 to 100: "))
    Guesses +=1
    if(UserGuess==randNUM):
        print("You guessed it right")
    else:
        if(UserGuess<randNUM):
            print("You guessed it wrong! Try bigger number")
        elif(UserGuess>randNUM):
            print("You guessed it wrong! Try smaller number")

print(f"You guessed the number in {Guesses} guesses")

with open("HighScore.txt","r") as f:
    HighScore = int(f.read())
if(Guesses<HighScore):
    print("You have just broken the high score!")
    with open("HighScore.txt","w") as f:
        f.write(str(Guesses))
