import random

animals = ["cat", "walrus", "zebra", "panda"]
languages = ["warlpiri", "dutch", "swahili"]
countries = ["namibia", "russia", "tanzania", "laos"]

initial_word = "word"
chances = 10
guessed_letters = []
revealed_word = []

def force_yes_or_no(answer):
    '''
    Ensures that the user enters 'y' or 'n'. Returns T if user answers
    'yes' and F if user answer 'no'.
    '''
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        new_answer = input("Type 'y' for 'yes' and 'n' for 'no'.")
        return force_yes_or_no(new_answer)


def force_abc(answer):
    '''
    Checks if answer is 'a', 'b', or 'c'. If so, returns 
    answer. If not, requires user to provide a valid
    answer and then returns the new valid answer.
    '''
    if answer in ['a', 'b', 'c']:
        return answer 
    else:
        new_answer = input("Please enter 'a', 'b', or 'c'.")
        return force_abc(new_answer)


def force_alpha(answer):
    '''
    Checks if answer is a single alphabetic character. If so,
    returns answer. If not, requires user to provide a valid
    answer and then returns the new valid answer.
    '''
    if answer.isalpha():
        if len(answer) == 1:
            return answer
        else:
            new_answer = input("Please enter a single letter.")
            return force_alpha(new_answer)
    else:
        new_answer = input("Please enter valid letter.")
        return force_alpha(new_answer)


def force_new_letter(guess, guessed_letters):
    '''
    Forces user to enter a letter that has not already been guessed.
    Returns the letter (str).
    '''
    if guess not in guessed_letters:
        return guess
    else:
        print("Sorry, you've guessed that already.")
        new_guess = input("Please enter a new letter.")
        return force_new_letter(new_guess, guessed_letters)


def guess_letter(chances, hangman_word, revealed_word, guessed_letters):
    '''
    '''

    if chances == 0:
        print(hangman_word)
        print("You lose!")
        again = input("Would you like to play again?")
        yn = force_yes_or_no(again)
        if yn:
            play(yn, hangman_word)
        else:
            print("Okay, bye!")

    print(' '.join(revealed_word))
    if "_" not in revealed_word:
        print("You win!")
        again = input("Would you like to play again?")
        yn = force_yes_or_no(again)
        if yn:
            play(yn, hangman_word)
        else:
            print("Okay, bye!")


    else:
        print("You have {} lives left.".format(chances))
        if len(guessed_letters) > 0:
            print("Guessed letters: ", " ".join(guessed_letters))

        guess = input("Pick a letter...")
        guess = force_alpha(guess)
        guess = guess.lower()
        guess = force_new_letter(guess, guessed_letters)

        if guess in hangman_word:
            print("Good guess!")
            print("")
            print("")
            for i, l in enumerate(hangman_word):
                if guess == l:
                    revealed_word[i] = l

        else:
            print("Sorry, {} is not in the word.".format(guess))
            print("")
            print("")
            guessed_letters.append(guess)
            chances -= 1
        guess_letter(chances, hangman_word, revealed_word, guessed_letters)

def play(yn, hangman_word):
    initial_word = "word"
    chances = 7
    guessed_letters = []
    revealed_word = []

    if not play_game:
        print("Darn. Maybe another time!")
    else:
        print("Great!")
        print("Please pick a category:")
        category = input("(a) animals, (b) languages, (c) countries").lower()
        category = force_abc(category)
        if category == 'a':
            hangman_word = random.choice(animals)
        elif category == 'b':
            hangman_word = random.choice(languages)
        elif category == 'c':
            hangman_word = random.choice(countries)
        for l in hangman_word:
            revealed_word.append("_")
        chances = 7
        guess_letter(chances, hangman_word, revealed_word, guessed_letters)

initial_input = input("Would you like to play Hangman? ['y'/'n']")
play_game = force_yes_or_no(initial_input)
play(play_game, initial_word)