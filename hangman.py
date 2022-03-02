#author CJP and JRI 2/10/2022

#we are importing random
import random

#added a function that prompts the user to play again
def play_game():

    play = input("Do you want to play hangman? Enter either yes or no: ")

    #if and else used to convert the users imput to the game

    if play == 'yes':

        game()
        
    else:
        print("Fine. Goodbye! ")

#another function used to pick a random word out of the word list

def choose_word():

#the word list
    words = ["random", "list", "meat", "corn", "cornbread",
    "trail","grass","green","snail","stump","mushroom",
    "yellow","blue","weather","centipede","basketball","vile",
    "flourish","meatstick","crayon", "flouride", "beefs", "beast",
    "hippopotomus", "telescope", "racecar", "freedom", "computer",
    "taxes", "aardvarks", "iodized", "transcontinental", "responsibility"
    , "beetroot", "independent", "democracy", "amendment", "polysaccharide",
    "ponder", "spoon", "meatloaf", "meatballs", "gruel", "meatiest", "meatless"
    "meathead","slippy","sloth","cumbersome", "gargantuan", "fluctuate",
    "radish", "marketability", "tree", "laboratory", "thyroparathyroidectomized",
    "anger", "beer","fraction", "retire", "vacuum", "bark", "loser", "useless", 
    "battlefield"]
    
    return random.choice(words).lower()

# this is the primary game function
def game():

#all of the possible imputs
    alphabet = ('abcdefghijklmnopqrstuvwxyz')

#word is set equal to the choose_word function so that that the random word is set in the game
    word = choose_word()

    letters_guessed = []

#added a counter to keep track of the amount of failed attemps

    attempts = 7

    guessed = False

    print()

#this print statement tells the user how many letters are in the word
   
    print('The word has', len(word), 'letters')

#if the user goes over 7 failed guesses they lose
    
    while guessed == False and attempts > 0:

#this tells the user how many tries they have  
     
        print('You have ' + str(attempts) + ' attempts')
        
#this allows the user to guess the full word as well as a single letter
        guess = input('Guess a letter in the word or enter the full word. ').lower()

#this statement is when the user only guesses one letter
        if len(guess) == 1:
            
#if the letter is not in the alphabet than the game will tell the user that they must enter a real number            
            if guess not in alphabet:
                
                print('Please enter a real letter ')

#this statement tells the user if they have already guessed a letter using an elif 
           
            elif guess in letters_guessed:
                
                print("You have already guessed that letter. Please try again ")
            
#used an elif statement to trigger a print statement telling the user that the guess is incorrect if the user's guess is not in the word
            elif guess not in word:
                
                print("incorrect guess. Try again ")
                
# this appends all previous guesses to a list of letters that the user have already guessed
                letters_guessed.append(guess)

# we used a counter to count the number of incorrect guesses   
                attempts -= 1
            
#now an elif is used to print a statment telling the user that the letter the user guessed is in the word
            elif guess in word: 
                
                print("That guess is corrrect! ")
                
                letters_guessed.append(guess)

#if the entry is invald or does not meet the requirments than it will print the following

            else:
                
                print("Invalid input! ")
        
# elif for when the length of the actual word equals the users guess
        elif len(guess) == len(word):

# if statement inside of the elif to further devide what will happen if the users guess is or is not the word            
#if the guess is the word that the following print statement will print for the user            
            if guess == word:
                
                print("You have guessed the word! ")
                
                guessed = True
#but an else is used to add another incorrect guess by a counter and to print that the users guess is not the word            
            else:
                
                print("That is not the word! ")
                
                attempts -= 1
# this else is used to explain that if the guess is not equal to the length of the word then the code above will not be used and a incorrect guess will be added to the counter        
        else:
            
            print("That was not the corrrect length of the word ")
            
            attempts -= 1

# empty string to be used later for print statement        
        status = ''

# if/else used for a false guess of the word        
        if guessed == False:
            
            for letter in word:

# puts letter in right location               
                if letter in letters_guessed:
                    status += letter
                
                else:
                    status += '_'
            
            print(status)
        
#once all of the letters of the correct word are guessed the if is used to tell the user they have won the game        
        if status == word:
            
            print('Great job! You guessed the word correctly! ')
            
            guessed = True

#once you run out of guesses you are a loser of the game        
        elif attempts == 0:
            
            print("You have ran out of attempts.")
            print("You are a loser!")
    
    play_game()

#game function
game()
