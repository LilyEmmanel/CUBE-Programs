#DICE ROLLING PROGRAM FEATURES

#1. Option to choose between die types (d6-d20)
#2. Roll multiple dice (ask the user!)
#3. Random number generator
#4. POSSIBLE IDEA: add "wight" to the dice so they only roll certain numbers

#MISSING FEATURES
#1. A way to roll one die multiple times
#2. A way to total up the dice rolls (min/max too)



import random

myRolls =[]


def diceEngine():
    #use a while loop to run until the user quits
    while True:
        dieType = input("How many sides would you like the die to have")
        numberOfRolls = input("How many times would you like me to roll?")

        #creat a for loop that runs the number specified in numberOfRolls
        for x in range(0, int(numberOfRolls)):
            myRolls.append(random.randint(1, int(dieType)))
        
        print("Here are all of your dice rolls: {}".format(myRolls))
        print("The sum of all of our dice rolls was: {}".format(sum(myRolls)))
        print("The highest roll was: {}".format(max(myRolls)))
        print("The lowest roll was: {}".format(min(myRolls)))

        #use a variable to determine whether or not to trigger a break statement
        rollAgain = input("Roll again? y / n  ")
        if rollAgain == "n":
            break
        #use a variable to determine whether or not to clear the myRolls list
        clearRolls = input("Clear previous rolls? y / n  ")
        if clearRolls == "y":
            myRolls.clear()

if __name__ == "__main__":
    diceEngine()
    
        
