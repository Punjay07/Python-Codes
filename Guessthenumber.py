import random

randnum = random.randint(-101,101)
#print(randnum)

def compguess(low, high, randnum, countc=0):
    if high>= low:
        guess = low+(high-low) //2
        if guess==randnum:#if guess is in the middle, it is found.
            return countc
        elif guess>randnum:#if guess is higher than randnum, it must be in lower half of the set of numbers
            countc=countc+1
            return compguess(low, guess-1, randnum, countc)
        else:#if guess is lower than randnum, it must be in upper half of the set of numbers
            countc=countc+1
            return compguess(guess+1, high, randnum, countc)
    else:#number not found
        return -1

count=0
guess=None

while (guess != randnum):
    guess=(int)(input("Enter you guess b/w -100 t0 100: "))
    if guess < randnum:
            print("Your guess is lower")
            count=count+1
    elif guess > randnum:
            print("Your guess is higher")
            count=count+1
    else:
            print("Congratulations, you guessed it. You have potential to become a Seer!")
            count=count+1
            break

print("However you took",count,"steps to guess the number")
print("Computer took " + str(compguess(-100,100,randnum)) + " step")
