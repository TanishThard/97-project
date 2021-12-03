import random
print ("Number guessing game")
print ("Guess a number between 1 and 9")
number=random.randint(1,9)
chances=0
while chances < 5:
    guess=int(input("enter your guess"))
    if guess== number:
        print("Congratulation you won !!!")
        break

    elif guess<number:
        print("your guess is too low:guess a number higher than",guess)

    else:
        print("your number is too high: guess a number lower than",guess) 
       
if not chances<5:
        print ("You Lose !! The number is",number)   


