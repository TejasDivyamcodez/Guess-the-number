import random

random_number = 0

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {x}:\t"))
        if guess < random_number:
            print("Sorry. Guess again .You are too low!")
        elif guess > random_number:
            print("Sorry. Guess again . You are too high!")
    print(f"Yoo! You have guessed the number {random_number} correctly!! ✋ ")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} . Too high:(h) or Too low:(l) or Correct(c):\t')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess +1
    print(f"Yaa hoo ! AI have guessed your number {guess} correctly!! 🥳")

computer_guess(1000)

guess(10)

if __name__ == '__main__':
    guess
    computer_guess
