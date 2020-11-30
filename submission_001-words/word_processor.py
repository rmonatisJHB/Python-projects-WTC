
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    """Converts a text into a string and lowers the case"""
    delimiters = ',',';','.','?',' '
    text = split(delimiters,text)
    new_text = list(map(lambda word:word.lower(),text))
    filtered_text = list(filter(lambda words:len(words)>0,new_text))
    return filtered_text
   


def words_longer_than(length, filtered_text):
    """Finds words in a list that are equal to or longer than the length specified"""

    long_words = list(filter(lambda words:len(words)>= length, filtered_text ))
    return long_words


def words_lengths_map(filtered_text):
    """Finds words of the same length and returns their count in a dictionary"""
    
    lengths = [len(word) for word in filtered_text if len(word)>1]
    result = {x:lengths.count(x) for x in lengths}
    return result
    


def letters_count_map(text):
    new_text = text.lower()
    letters_list= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = {letter : new_text.count(letter) for letter in letters_list}
    return result

def most_used_character(text):
    from functools import reduce
    letters = letters_count_map(text)
    if text == "":
        return None 
    else:
        popular_char = reduce(lambda x,y: x if letters[x] > letters[y] else y,letters)
        return popular_char

if __name__ == "__main__":
    text = 'These are indeed interesting, an obvious understatement, times. What say you?'
    length = 4
    filtered_text = convert_to_word_list(text)
    words_longer_than(length, filtered_text)
    lengths = words_lengths_map(filtered_text)
    letters = letters_count_map(text)
    popular_char = most_used_character(text)