import unittest
import mastermind
import io
from io import StringIO
from unittest.mock import patch
import sys

class TestFunctions(unittest.TestCase):


    def test_create_code(self):
        for x in range(1, 101):
            code = mastermind.create_code()
            """Check if the code generated is a list"""
            self.assertEqual(list, type(code))
            """Check the length of the code"""
            self.assertEqual(4, len(code))
            """Check if the range of numbers does not exceed the number 8"""
            for i in range(0,4):
                self.assertTrue(code[i],range(1,9))

    def test_check_correctness(self):
        """ This function checks if the correct digits are in place 
        and the number of turns are sufficient the test should be true"""
        sys.stdout = StringIO()
        output = sys.stdout.getvalue()
        self.assertTrue(mastermind.check_correctness(8,4))
        self.assertFalse(mastermind.check_correctness(7,3))
        

    @patch("sys.stdin", StringIO("123\n12345\n1234\n"))   
    def test_get_user_input(self):
        sys.stdout  = StringIO()
        output = sys.stdout.getvalue()
        result = mastermind.get_user_input()
        self.assertEqual(result, "1234")
        self.assertEqual(len(result), 4)
        self.assertIsInstance(result, str)
        


    @patch("sys.stdin", StringIO("5624"))
    def test_take_turn(self):
        sys.stdout = StringIO()
        output = sys.stdout.getvalue()
        code =[1,6,2,3]
        answer = ["5","6","2","4"]
        result = mastermind.take_turn(code,answer)
        self.assertEqual(result, (2,0))


if __name__ == '__main__':
    unittest.main()