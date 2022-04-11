import random
from re import A
from WordList import Words
import string
import time

#List with all the Hangman Pictures
HANGMAN_PICS = ['''
 +---+                  
     |
     |
     |
    ===''', '''
 +---+
 O   |
     |
     |
    ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
+---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''']
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
#twist of time
    t = time.time()
    GuessWord = ValidListWord(Words)
    SetGuessWord = set(GuessWord)
    alphabet = set(string.ascii_uppercase)
    LettersUsed = set()
    Lives = 0
    LetterChoice = ""
    Player = 1
#When input is wrong
    BadList = [f"I thought you were good at this game. Who even guesses {LetterChoice} these days?", f"You're actually bad.", "COME ON MAN. What are you thinking.", "Nice try I guess",]
#when input is right
    GoodList = ["WOW! you actually got something right for once.", f"Yay! {LetterChoice} is actually in the word", f"Good Job! {LetterChoice} is there."]
    while len(SetGuessWord) != 0 and Lives != 6 and GuessWord != LetterChoice:
        print(HANGMAN_PICS[Lives])
        print (f"These are the letters you have used: {' '.join(sorted(LettersUsed))}")
        WordShown = [letter if letter in LettersUsed else "_" for letter in GuessWord]
        print(f"Secret word: {' '.join(WordShown)}")
        if Play == "2h":
            print (f"It is Player {Player} turn. ")
            if Player == 1:
                Player = Player + 1
            else:
                Player = Player - 1
        LetterChoice = input("Guess a letter in the secret word: ").upper()
#Lagging the game for a second to create suspense. (Could have been inputed many places)
        time.sleep(1)
        if LetterChoice in alphabet - LettersUsed:
            LettersUsed.add(LetterChoice)
            if LetterChoice in SetGuessWord:
                SetGuessWord.remove(LetterChoice)
                print(random.choice(GoodList))
            else:
#Changing the state of the guy hanging (from "HangPics" list)
                Lives = Lives + 1
                print(random.choice(BadList))
                print(f"{LetterChoice} is not in the word. You have {6 - Lives} lives left.")
        elif LetterChoice in LettersUsed:
            print("You guessed this letter already. ")
        elif len(LetterChoice) == len(GuessWord):
            if LetterChoice == GuessWord:
                print(random.choice(GoodList))
            else:
                Lives = Lives + 1
                print(random.choice(BadList))
        else:
            print("Invalid input")
#Either Lives or SetGuessWord have to be == 0 to get here
    print(HANGMAN_PICS[Lives])
    if Lives == 6:
        if Play == "2h":
            print(f"Oh you lost all your collective lives! that means player {Player} automatically wins.")
        print("How did you lose all your lives man? Disappointed.")
        print(f"It was sooo easy. The word was {GuessWord}")
#finished time tiwst
        Elapsed = time.time() - t
        Elapsed = int(Elapsed)
        print(f"it took you {Elapsed} seconds to lose.")
    else:
        print(f"You got it! The word was {GuessWord}.")
        if Play == "2h":
            if Player == 1:
                Player = Player + 1
            else:
                Player = Player - 1
            print(f"Easy w's for Player {Player}. Congradulations")
        Elapsed = time.time() - t
        Elapsed = int(Elapsed)
        print(f"it took you {Elapsed} seconds to get the word.")

#logic to see if user wants to play multipule times or just dip
Play = input("Do you wanna play Hangman(h), two player Hangman?(2h) or quit(q)? ").lower()
while Play != "q":
    if Play == "h" or Play == "2h":
        HangMan()
    else:
        print("Bruh. That wasnt even a choice.")
    Play = input("Play again?(h), (2h) or quit(q)? ").lower()
