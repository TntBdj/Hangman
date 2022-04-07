import random
from WordList import WordList
import string

def ValidListWord(WordList):
    RandomWord = random.choice(WordList)
    #removing specific things from the list
    while "-" in WordList or " " in WordList: 
        RandomWord = random.choice(WordList)
    return RandomWord.upper() 

def HangMan():
    GuessWord = ValidListWord(WordList)
    SetGuessWord = set(GuessWord)
    alphabet = set(string.ascii_uppercase)
    LettersUsed = set()

    while len(SetGuessWord) != 0:

        print (f"You already used these letters: {' '.join(sorted(LettersUsed))}")
        WordShown = [letter if letter in LettersUsed else "_" for letter in GuessWord]
        print(f"You have: {' '.join(WordShown)}")
        LetterChoice = input("Guess a letter in the secret word: ").upper()
        if LetterChoice in alphabet - LettersUsed:
            LettersUsed.add(LetterChoice)
            if LetterChoice in SetGuessWord:
                SetGuessWord.remove(LetterChoice)
                print (SetGuessWord)
        elif LetterChoice in LettersUsed:
            print ("You guessed this letter already. ")
        else:
            print("Invalid input")
#when the length of SetGuessWord == 0
HangMan()