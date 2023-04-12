# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    correct = 0
    for letter in secret_word:
        if letter not in letters_guessed:
            break
        else:
            correct += 1
    if correct == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    new_word = ''
    for letter in secret_word:
        if letter not in letters_guessed:
            new_word += '_ '
        else:
            new_word += letter
    return new_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    remaining = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            remaining += letter
    return remaining
def hangman(secret_word):
    counter = 0
    n = 6
    alphabet = string.ascii_lowercase
    warnings = 3
    guessed_characters = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    victory = False
    while not victory and n > 0:
        counter += 1
        if counter == 1:
            print('Welcome to the game Hangman!')
            print(f'I am thinking of a word that is {len(secret_word)} letters long.')
        print('-------------')
        print(f'You have {n} guesses left.')
        print('Available letters:', get_available_letters(guessed_characters))
        guess = input('Please guess a letter: ').lower()
        if guess in alphabet and len(guess) == 1:
            if guess in secret_word and guess not in guessed_characters:
                guessed_characters.append(guess)
                print('Good guess: ', get_guessed_word(secret_word, guessed_characters))
        elif guess in alphabet and guess not in secret_word and guess not in guessed_characters:
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, guessed_characters))
            guessed_characters.append(guess)
            if guess in vowels:
                n -= 2
            else:
                n -= 1
        else:
            if warnings > 1 and guess not in alphabet:
                warnings -= 1
                print(f'Oops! That is not a valid letter. You have {warnings} warnings left: ',
                  get_guessed_word(secret_word, guessed_characters))
            elif warnings > 1 and guess not in guessed_characters:
                print(f'Oops! That is not a valid letter. You have no warnings left so you lose one guess: ',
                  get_guessed_word(secret_word, guessed_characters))
                n -= 1
            elif warnings > 1 and guess in guessed_characters:
                print(f"Oops! You've already guessed that letter.. You have {warnings} warnings left: ",
                  get_guessed_word(secret_word, guessed_characters))
            else:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: ",
                  get_guessed_word(secret_word, guessed_characters))
                n -= 1
        victory = is_word_guessed(secret_word, guessed_characters)
    if victory:
        print('-------------')
        unique_char = len(set(secret_word))
        score = n * unique_char
        print('Congratulations, you won! \n Your total score for this game is: ', score)
    else:
        print('-------------')
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    my_word_list = list(my_word)
    other_word_list = list(other_word)
    for char in my_word_list[:]:
        if char == ' ' :
            my_word_list.remove(char)
    match = True
    if len(my_word_list) != len(other_word_list):
        match = False
    else:
        for char_index in range(len(my_word_list)):
            if my_word_list[char_index] != '_':
                if my_word_list[char_index] != other_word_list[char_index]:
                    match = False
            else:
                if other_word_list[char_index] in my_word_list:
                    match = False
    return match

def show_possible_matches(my_word):
    matches = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            matches.append(other_word)
    if len(matches) == 0:
        print('No matches found.')
    return ' '.join(matches)
print(show_possible_matches('a_ _ le'))

def hangman_with_hints(secret_word):
    counter = 0
    n = 6
    alphabet = string.ascii_lowercase
    warnings = 3
    guessed_characters = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    victory = False
    while not victory and n > 0:
        counter += 1
        if counter == 1:
            print('Welcome to the game Hangman!')
            print(f'I am thinking of a word that is {len(secret_word)} letters long.')
        print('-------------')
        print(f'You have {n} guesses left.')
        print('Available letters:', get_available_letters(guessed_characters))
        guess = input('Please guess a letter: ').lower()
        if guess == '*':
            print("Possible matches are:")
            print(show_possible_matches(get_guessed_word(secret_word, guessed_characters)))
        elif guess in alphabet and len(guess) == 1:
            if guess in secret_word and guess not in guessed_characters:
                guessed_characters.append(guess)
                print('Good guess: ', get_guessed_word(secret_word, guessed_characters))
            elif guess in alphabet and guess not in secret_word and guess not in guessed_characters:
                print('Oops! That letter is not in my word:', get_guessed_word(secret_word, guessed_characters))
                guessed_characters.append(guess)
                if guess in vowels:
                    n -= 2
                else:
                    n -= 1
        else:
            if warnings > 1 and guess not in alphabet:
                warnings -= 1
                print(f'Oops! That is not a valid letter. You have {warnings} warnings left: ',
                      get_guessed_word(secret_word, guessed_characters))
            elif warnings >1 and guess not in guessed_characters:
                print(f'Oops! That is not a valid letter. You have no warnings left so you lose one guess: ',
                          get_guessed_word(secret_word, guessed_characters))
                n -= 1
            elif warnings >1 and guess in guessed_characters:
                print(f"Oops! You've already guessed that letter.. You have {warnings} warnings left: ",
                          get_guessed_word(secret_word, guessed_characters))
            else:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: ",
                get_guessed_word(secret_word, guessed_characters))
                n -= 1
        victory = is_word_guessed(secret_word, guessed_characters)
    if victory:
        print('-------------')
        unique_char = len(set(secret_word))
        score = n * unique_char
        print('Congratulations, you won! \n Your total score for this game is: ', score)
    else:
        print('-------------')
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
