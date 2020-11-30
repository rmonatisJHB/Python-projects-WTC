import unittest
import robot
import io
from io import StringIO
import sys

class Test_Functions(unittest.TestCase):

    def test_history(self):
        
        robot.history =  []
        self.assertEqual(robot.command_history('forward 10'), ['forward 10'])
        self.assertEqual(robot.command_history('help'), ['forward 10'])   

    def test_normal_replay(self):
        robot_name = 'HAL'
        history = ['forward 10', 'right', 'forward 10']
        command_name = 'replay'
        arg1 = ''
        arg2 = ''
        output = (True, ' > HAL replayed 3 commands.')
        self.assertEqual(robot. do_replay(robot_name,history,command_name, arg1, arg2), output)
    
    def test_replay_specific(self):
        robot_name = 'HAL'
        history = ['forward 10', 'right', 'forward 10','right', 'back 5']
        command_name = 'replay'
        arg1 = '2'
        arg2 = ''
        output = (True, ' > HAL replayed 2 commands.')
        self.assertEqual(robot.do_replay(robot_name,history,command_name, arg1, arg2), output)
    
    def test_replay_limited(self):
        robot_name = 'HAL'
        history = ['forward 10', 'right', 'forward 10','right', 'back 5', 'back 5']
        command_name = 'replay'
        arg1 = '5-2'
        arg2 = ''
        output = (True, ' > HAL replayed 3 commands.')
        self.assertEqual(robot.do_replay(robot_name,history,command_name, arg1, arg2), output)
    
    def test_replay_silent(self):
        robot_name = 'HAL'
        history = ['forward 10', 'right', 'forward 10','right', 'back 5', 'back 5']
        command_name = 'replay'
        arg1 = 'silent'
        arg2 = ''
        output = (True, ' > HAL replayed 6 commands silently.')
        self.assertEqual(robot.do_replay(robot_name,history,command_name, arg1, arg2), output)
    
    def test_replay_silent_specific(self):
        robot_name = 'HAL'
        history = ['forward 10', 'right', 'forward 10','right', 'back 5', 'back 5']
        command_name = 'replay'
        arg1 = '4'
        arg2 = 'silent'
        output = (True, ' > HAL replayed 4 commands silently.')
        self.assertEqual(robot.do_replay(robot_name,history,command_name, arg1, arg2), output)
    
    def test_replay_reversed(self):
        robot_name = 'HAL'
        history = ['forward 10', 'right', 'forward 10','right', 'back 5', 'back 5']
        command_name = 'replay'
        arg1 = 'reversed'
        arg2 = ''
        output = (True, ' > HAL replayed 6 commands in reverse.')
        self.assertEqual(robot.do_replay(robot_name,history,command_name, arg1, arg2), output)
    
    def test_reversed_specific(self):
        robot_name = 'HAL'
        history = ['forward 10', 'right', 'forward 10','right', 'back 5', 'back 5']
        command_name = 'replay'
        arg1 = 'reversed'
        arg2 = '5'
        output = (True, ' > HAL replayed 5 commands in reverse.')
        self.assertEqual(robot.do_replay(robot_name,history,command_name, arg1, arg2), output)
    
    def test_reversed_silent(self):
        robot_name = 'HAL'
        history = ['forward 10', 'right', 'forward 10','right', 'back 5', 'back 5']
        command_name = 'replay'
        arg1 = 'reversed'
        arg2 = 'silent'
        output = (True, ' > HAL replayed 6 commands in reverse silently.')
        self.assertEqual(robot.do_replay(robot_name,history,command_name, arg1, arg2), output)