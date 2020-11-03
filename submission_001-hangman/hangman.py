#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    f = open(file_name, 'r')
    words = f.readlines()
    return words


def select_random_word(words):
    selection = random.choice(words)
    word = selection.rstrip("\n")
    l = random.randint(0, len(word) - 1)
    hint = word.replace(word[l], '_', 1)
    print("Guess the word: "+ hint)
    return word



def get_user_input():
    user_guess = input("\nGuess the missing letter: ")
    return user_guess


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

