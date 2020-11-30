import super_algos
import unittest
import itertools
from itertools import product

class TestFunctions(unittest.TestCase):


    def test_find_min(self):

        my_list = [3,5,6,5,9,13,8,28]
        self.assertEqual(min(my_list), super_algos.find_min(my_list))
        self.assertIsInstance(my_list[0], int)
        self.assertEqual(super_algos.find_min([1,'a', 2]), -1)
        self.assertEqual(super_algos.find_min([]), -1)

    def test_sum_all(self):
        my_list = [3,5,6,5,9]
        self.assertEqual(sum(my_list), super_algos.sum_all(my_list))
        self.assertIsInstance(my_list[0], int)
        self.assertEqual(super_algos.sum_all([1,'a', 2]), -1)
        self.assertEqual(super_algos.sum_all([]), -1)



    def test_find_possible_strings(self): 
        my_chars = ['r','o']
        p = product(my_chars, repeat = 3)
        for i in p:
            return i
        self.assertEqual(super_algos.find_possible_strings(my_chars, 3), i)
        self.assertEqual(super_algos.find_possible_strings(['q','b',1],3), [])
        self.assertEqual(super_algos.find_possible_strings([],[]))
    
