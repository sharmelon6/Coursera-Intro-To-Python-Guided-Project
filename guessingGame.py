import random

def computerGuess(lowval, highval, randnum, count=0):
    if highval >=lowval:
        guess = lowval + (highval - lowval) // 2
        
        # if guess ins in the middle, it is found!
        if guess == randnum:
            return count
        
        # if the guess is greater than the number, it must be found in lower half of the set of numbers between lowval and guess
        elif guess > randnum:
            return computerGuess(lowval, guess-1, randnum, count)
        
        # if the guess is less than the number, it must be found in upper half of the set of numbers between guess and highval
        else:
            return computerGuess(guess+1, highval, randnum, count)

    else:
        # Number not found
        return -1
    # end of function

# generate a random number between 1 and 100
randnum = random.randint(1,101)

# initializing the guess variable and counter
count = 0
guess = -99

while (guess != randnum):
    # get the user's guess
    guess = int(input("Enter your guess between 1 and 100: "))

    # comparing the guess to the random number and giving feedback
    if guess < randnum:
        print("higher")
    elif guess > randnum:
        print("lower")
    else:
        print("you guessed it!")
        break
    count +=1

# End of while loop and output guess count
print("It took you " + str(count) + " steps to guess the number.")
print("The computer took " + str(computerGuess(0,100, randnum)) + " steps!")