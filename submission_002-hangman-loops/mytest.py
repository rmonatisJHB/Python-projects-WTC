import random

word = 'mine'
def select_random_word(word):
    import random
    random_index = random.randint(0, len(word)-1)
    letter = word[random_index]
    print(letter)

def select_random_letter_from(word):
    import random
    random_index = random.randint(0, len(word) - 1)
    letter = word[random_index]
    print('Guess the word: ' + word[:random_index] + "_" + word[random_index+1:])
    return letter, random_index
