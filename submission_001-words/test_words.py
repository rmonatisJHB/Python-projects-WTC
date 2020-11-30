import unittest
import word_processor
import sys

class Test_Functions(unittest.TestCase):

    def test_convert_to_word_list(self):
        """Check if the output is a list and that it is separated 
        by specific delimitors and is in lowercase"""

        text = 'These are indeed interesting, an obvious understatement, times. What say you?'
        result = ['these','are','indeed','interesting','an','obvious','understatement','times','what','say','you']
        self.assertEqual(word_processor.convert_to_word_list(text), result)
    
    def test_words_longer_than(self):
        """ returns words longer or equal to the specified length"""

        filtered_text = ['these','are','indeed','interesting','an','obvious','understatement','times','what','say','you']
        length = 6
        result = ['indeed','interesting','obvious','understatement']
        self.assertEqual(word_processor.words_longer_than(length,filtered_text),result)
    
    def test_words_lengths_map(self):
        """Finds words of the same length and returns their count in a dictionary"""

        filtered_text = ['these','are','indeed','interesting','an','obvious','understatement','times','what','say','you']
        output = {2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1}
        self.assertEqual(word_processor.words_lengths_map(filtered_text),output)
    

    def test_letters_count_map(self):
        """ Counts the number of occurrences of each letter"""

        text = 'These are indeed interesting, an obvious understatement, times. What say you?'
        results = {'a':5, 'b': 1, 'c':0, 'd': 3, 'e': 11, 'f': 0, 
        'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 
        'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 
        'w': 1, 'x': 0, 'y': 2, 'z': 0}
        self.assertEqual(word_processor.letters_count_map(text),results)

    def test_most_used_character(self):
        """Returns the most used letter in the text"""

        text = 'These are indeed interesting, an obvious understatement, times. What say you?'
        self.assertEqual(word_processor.most_used_character(text), 'e')
        self.assertEqual(word_processor.most_used_character(''), None)
        

        