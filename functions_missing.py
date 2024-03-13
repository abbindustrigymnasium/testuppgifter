import random

print("The guessing game - round one!")
numberToGuess=random.randint(1,10)
print("I'm thinking of a number between 1 and 10")

guess=int(input("Guess which number I'm thinking of: "))
if guess==numberToGuess:
    print("You win!")
elif abs(guess-numberToGuess)<5:
    print("You are close, try again!")
    guess=int(input("Guess which number I'm thinking of: "))
    if guess==numberToGuess:
        print("You win!")
    elif abs(guess-numberToGuess)<5:
        print("Wrong again! One more try!")
        guess=int(input("Guess which number I'm thinking of: "))
        if guess==numberToGuess:
            print("You win!")
        else:
            print("Wrong again! That was your last chance...Game over!")
    else:
        print("Wrong again, and you did worse! Game over!")
else:
    print("You are so far off. Game over!")

print("The number was: ", numberToGuess)

print("The guessing game - round two!")
if guess==numberToGuess:
    a=100
else:
    a=5
numberToGuess=random.randint(1,a)
print("I'm thinking of a number between 1 and ", a)

guess=int(input("Guess which number I'm thinking of: "))
if guess==numberToGuess:
    print("You win!")
elif abs(guess-numberToGuess)<a/10:
    print("You are close, try again!")
    guess=int(input("Guess which number I'm thinking of: "))
    if guess==numberToGuess:
        print("You win!")
    elif abs(guess-numberToGuess)<a/10:
        print("Wrong again! One more try!")
        guess=int(input("Guess which number I'm thinking of: "))
        if guess==numberToGuess:
            print("You win!")
        else:
            print("Wrong again! That was your last chance...Game over!")
    else:
        print("Wrong again, and you did worse! Game over!")
else:
    print("You are so far off. Game over!")

print("The number was: ", numberToGuess)