import random
from WordList import Words
import string
import time

#Getting a secret word from other file (WordList.py)
def ValidListWord(WordList):
    RandomWord = random.choice(WordList)
    #removing specific things from the list
    while "-" in RandomWord or " " in RandomWord or "Kwantlen" in RandomWord\
    or "Rai" in RandomWord or "Zimmerman" in RandomWord: 
        RandomWord = random.choice(WordList)
    return RandomWord.upper() 
#Logic of the actual hangman game
def HangMan():
    GuessWord = ValidListWord(Words)
    SetGuessWord = set(GuessWord)
    alphabet = set(string.ascii_uppercase)
    LettersUsed = set()
    Lives = 6
    while len(SetGuessWord) != 0 and Lives != 0:
        print (f"These are the letters you ahve used: {' '.join(sorted(LettersUsed))}")
        WordShown = [letter if letter in LettersUsed else "_" for letter in GuessWord]
        print(f"Secret word: {' '.join(WordShown)}")
        LetterChoice = input("Guess a letter in the secret word: ").upper()
        #Lagging the game for a second to create suspense. (Could have been inputed many places)
        time.sleep(1)
        if LetterChoice in alphabet - LettersUsed:
            LettersUsed.add(LetterChoice)
            if LetterChoice in SetGuessWord:
                SetGuessWord.remove(LetterChoice)
                print("WOW! you actually got something right for once.")
            else:
                #Changing the state of the guy hanging (from "HangPics" list)
                Lives = Lives - 1
                print("I thought you were good at this game. Who even guesses {LetterChoice} these days?")
                print(f"{LetterChoice} is not in the word. You have {Lives} lives left.")
        elif LetterChoice in LettersUsed:
            print("You guessed this letter already. ")
        else:
            print("Invalid input")
    #Either Lives or SetGuessWord have to be == 0 to get here
    if Lives == 0:
        print("How did you lose all your lives man? Disappointed.")
        print(f"It was sooo easy. The word was {GuessWord}")
    else:
        print(f"You got it! The word was {GuessWord}. Took you long enough.")

#logic to see if user wants to play multipule times or just dip
Play = input("Do you wanna play Hangman(h) or quit(q)? ").lower()
while Play != "q":
    if Play == "h":
        HangMan()
    else:
        print("Bruh. That wasnt even a choice.")
    Play = input("Play again?(h) or quit(q)? ").lower()
