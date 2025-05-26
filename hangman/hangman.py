import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 6

    while len(word_letters) > 0 and lives >0:

        #letters used
        print(f'You have {lives} lives left and You have used these characters:', ' '.join(used_letters))


        #what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 #taking away a life if wrong
                print('Letter is not in word.')
        elif user_letter in used_letters:
            print('You have already guessed this letter.')
        else:
            print('Invalid Character. Please try again.')

    if lives == 0:
        print(f'Sorry. You Died. The word was {word}')
    else:
        print (f'\nCongratulations! You have guessed the word {word}')


hangman()
# user_input = input('Type a character: ')
# print(user_input)

