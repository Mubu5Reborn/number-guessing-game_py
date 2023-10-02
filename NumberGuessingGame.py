import random
#guess = int(input("Please guess a number:"))
def num_guess():#prompt as parameter
    guess_attempt = input("Please guess again: ")
    try:
        int(guess_attempt)
    except ValueError:
            print("Error: A number was not detected")
            return(num_guess())
    return int(guess_attempt)
guess = num_guess()
seed = 15
number = random.randint(2,seed)
guess_counter = 1

while(guess != number):
    if (guess < number):
        print("The number is higher")
        guess = num_guess()
        guess_counter+=1
    elif (guess > number):
        print("The number is lower")
        guess = num_guess()
        guess_counter+=1
    else:
        break

print ("Congrats you guessed the number within " + str(guess_counter) + " guesses!")
