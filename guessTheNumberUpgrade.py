# Phillip Vo
import random

# -------------------------------------------------------------------
# this is the generateNumber function
# it has one parameter:
#   'topLimit' which is the top limit for the random number generator
# the function returns the random number generated to its caller
def generateNumber( topLimit ):
    
    # TO DO: ####################################################
    # Write code in this function that calculates and           #
    # returns a random number between 1 and the user's topLimit #
    #############################################################
    return random.randint(1, topLimit)
    
    
	
# end of generateNumber function -------------------------------------


# -------------------------------------------------------------------
# this is the askUserToGuess function
# it has two parameters:
#   the 'times' parameter is the number of guesses allowed
#   the 'secretNumber' parameter is the secret, random number
# the function returns one of two values:
#   return True if the user guessed the answer correctly
#   return False if the user did not guess the answer correctly
def askUserToGuess( times, secretNumber ):

    # this loop cycles through all the user guesses
    for guessesTaken in range(1, times+1):
        print('Take your guess #' + str(guessesTaken) + ': ')
        guess = int(input())

        if evaluateAnswer( guess, secretNumber ) == True:
            return True
        
    return False
# end of askUserToGuess function ----------------------------------


# -------------------------------------------------------------------
# this is the evaluateAnswer function
# it has two parameters:
#   the 'userGuess' parameter is the answer entered by the user
#   the 'userSecretNumber' parameter is the randomly generated number
def evaluateAnswer( userGuess, userSecretNumber ):
    
    # TO DO: ####################################################
    # Write code in this function that compares userGuess and   #
    # userSecretNumber. The code should:                        #
    # 1. If the user guess is smaller than the secret number,   #
    #    tell the user their guess is too low, and return False #
    # 2. If the user guess is greater than the secret number,   #
    #    tell the user their guess is too high, and return False#
    # 3. If the user guess and secret number are the same,      #
    #    return True, no message prints to the screen           #
    #############################################################
    if userGuess < userSecretNumber:
        print('Your guess is too low')
    elif userGuess > userSecretNumber:
        print('Your guess is too high')
    else:
        return True
		
# end of evaluateAnswer function -------------------------------------


# -------------------------------------------------------------------
# this is the playGame function
# it has one parameter:
#   'showAnswer' is a Boolean value, if that Boolean value is:
#       True, we'll show the right answer on the screen
#       False, we won't show the right answer on the screen
def playGame( showAnswer ):
    
    # TO DO: ####################################################
    # Write code in this function that                          #
    # 1. Greets the user                                        #
    # 2. Asks the user to choose the upper limit of the random  #
    #    number generator. Store the user's response in a       #
    #    variable you define                                    #
    # 3. Asks the user to choose a total number of guesses.     #
    #    Store the user's response in a local                   #
    #    variable called 'totalGuesses'                         #
    # 4. Generates a random number using the generateNumber     #
    #    function. Ensure the random number is between 1 and    #
    #    the user's choice for the upper limit. Store this      #
    #    number in the local variable 'theNumber'               #
    # 5. Tell the user to guess a number between 1 and the      #
    #    upper limits, and tell the user how many guesses they  #
    #    have in total                                          #
    #############################################################
    print('Welcome to the game that will determine if you live or die, muahahahah!')
    print('What is the largest number you would like to guess?')
    print('Enter only integers, fool:')
    upperLimit = int(input())
    print('And how many times would you like to guess?')
    print('Enter only integers, imbecile:')
    totalGuesses = int(input())
    theNumber = generateNumber(upperLimit)
    print('I am thinking of a number between 1 and ' + str(upperLimit))
    print('You have ' + str(totalGuesses) + ' tries to guess it right or else!')
    
    # you don't need to change anything below this comment ##############
    # ///////////////////////////////////////////////////////////////////
    # this if statement allows us to show the hidden number to the user
    if( showAnswer == True ):
        print('--shhh, the real number is ' + str(theNumber) + '.')
        
    #this gives a sucess/fail message if the user guessed correctly in the allotted attempts
    if askUserToGuess(totalGuesses,theNumber) == True:
        print('Good job! You guessed my number!')
    else:
        print('Nope. The number I was thinking of was ' + str(theNumber))
# end of playGame function -----------------------------------------
