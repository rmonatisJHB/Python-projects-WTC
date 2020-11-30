import unittest
import robot
import sys
from io import StringIO
class Test_Functions(unittest.TestCase):

    def test_history(self):
        original = sys.stdout
        new_string = StringIO()
        sys.stdout = new_string
        robot.history =  []
        self.assertEqual(robot.add_to_history('forward 10'), ['forward 10'])
        self.assertEqual(robot.add_to_history('help'), ['forward 10','help'])
        sys.stdout = original


    def test_normal_replay(self):
        original = sys.stdout
        new_string = StringIO()
        sys.stdout = new_string
        robot_name = 'HAL'
        robot.history = ['forward 10', 'right', 'forward 10']
        arguments = '3'
        output = (True, ' > HAL replayed 3 commands.')
        self.assertEqual(robot. do_replay(robot_name,arguments), output)
        sys.stdout = original

    
    def test_replay_specific(self):
        original = sys.stdout
        new_string = StringIO()
        sys.stdout = new_string
        robot_name = 'HAL'
        robot.history = ['forward 10', 'right', 'forward 10','right', 'back 5']
        robot.command_name = 'replay'
        arguments= '2'
        output = (True, ' > HAL replayed 2 commands.')
        self.assertEqual(robot.do_replay(robot_name,arguments), output)
        sys.stdout = original

    
    def test_replay_limited(self):
        original = sys.stdout
        new_string = StringIO()
        sys.stdout = new_string
        robot_name = 'HAL'
        robot.history = ['forward 10', 'right', 'forward 10','right', 'back 5', 'back 5']
        robot.command_name = 'replay'
        arguments = '5-2'
        output = (True, ' > HAL replayed 3 commands.')
        self.assertEqual(robot.do_replay(robot_name,arguments), output)
        sys.stdout = original

    
    def test_replay_silent(self):
        original = sys.stdout
        new_string = StringIO()
        sys.stdout = new_string
        robot_name = 'HAL'
        robot.history = ['forward 10', 'right', 'forward 10','right', 'back 5', 'back 5']
        robot.command_name = 'replay'
        arguments = 'silent'
        output = (True, ' > HAL replayed 6 commands silently.')
        self.assertEqual(robot.do_replay(robot_name,arguments), output)
        sys.stdout = original

    
    def test_replay_silent_specific(self):
        original = sys.stdout
        new_string = StringIO()
        sys.stdout = new_string
        robot_name = 'HAL'
        robot.history = ['forward 10', 'right', 'forward 10','right', 'back 5', 'back 5']
        command_name = 'replay'
        arguments = '4 silent'
        output = (True, ' > HAL replayed 4 commands silently.')
        self.assertEqual(robot.do_replay(robot_name,arguments), output)
        sys.stdout = original

    
    def test_replay_reversed(self):
        original = sys.stdout
        new_string = StringIO()
        sys.stdout = new_string
        robot_name = 'HAL'
        robot.history = ['forward 10', 'right', 'forward 10','right', 'back 5', 'back 5']
        command_name = 'replay'
        arguments = 'reversed'
        output = (True, ' > HAL replayed 6 commands in reverse.')
        self.assertEqual(robot.do_replay(robot_name,arguments), output)
        sys.stdout = original

    
    def test_reversed_specific(self):
        original = sys.stdout
        new_string = StringIO()
        sys.stdout = new_string
        robot_name = 'HAL'
        robot.history = ['forward 10', 'right', 'forward 10','right', 'back 5', 'back 5']
        command_name = 'replay'
        arguments= '5 reversed'
        output = (True, ' > HAL replayed 5 commands in reverse.')
        self.assertEqual(robot.do_replay(robot_name,arguments), output)
        sys.stdout = original

    
    def test_reversed_silent(self):
        original = sys.stdout
        new_string = StringIO()
        sys.stdout = new_string
        robot_name = 'HAL'
        robot.history = ['forward 10', 'right', 'forward 10','right', 'back 5', 'back 5']
        command_name = 'replay'
        arguments= 'silent reversed'
        output = (True, ' > HAL replayed 6 commands in reverse silently.')
        self.assertEqual(robot.do_replay(robot_name,arguments), output)
        sys.stdout = original