import random

def ManualGuess(x):
    random_no = random.randint(1, x)
    guess = 0
    while guess != random_no :
        guess = int(input(f"Enter a number between 1 and {x}: "))
        if(guess > random_no):
            print("The guess is too high.")
        elif(guess < random_no):
            print("The guess is too low")
    print(f"The guess entered is equal to {x} and yay Congrats")

# ManualGuess(10)
    
def ComputerGuess(x):
    high = x
    low = 1
    feedback = ''
    while feedback != 'c':
        if high != low:
            guess = random.randint(1, x)
        else:
            guess = low
        feedback = input(f"is {guess} too 'l' for low, 'h' for high or 'c' for correct: ").lower()
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
    print(f"The computer has made the correct guess at {guess}")

ComputerGuess(10)
