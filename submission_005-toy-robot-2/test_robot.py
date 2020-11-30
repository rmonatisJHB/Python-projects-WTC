import unittest
import robot
import io
from io import StringIO
from unittest.mock import patch
import sys

class Test_Functions(unittest.TestCase):

    def test_turn_left(self):
        """Test turn left function"""

        self.assertEqual(robot.turn_left("south"), "east")
        self.assertEqual(robot.turn_left("north"), "west")
    
    def test_turn_right(self):
        """Test turn right function"""

        self.assertEqual(robot.turn_right("east"), "south")
        self.assertEqual(robot.turn_right("west"), "north")

    def test_move_forward(self):
        """Test the move forward function"""

        direction = "south"
        position = [0,0]
        command = ["forward","10"]
        self.assertEqual(robot.move_forward(direction,position,command),[0,-10])
    
    def test_move_back(self):
        """Test the move back function"""

        direction = "east"
        position = [0,0]
        command = ["back", "15"]
        self.assertEqual(robot.move_back(direction,position,command),[-15,0])
    
    def test_sprint(self):
        """Test the sprint command"""

        sys.stdout = StringIO()
        output = sys.stdout.getvalue()
        command = 4
        robot_name = "Gal"
        self.assertEqual(robot.sprint(command,robot_name),10)

    def test_handle_command(self):
        """Test is the handle command function"""

        command = "help"
        robot_name = "HAL"
        direction = "north"
        position = [0,0]
        self.assertEqual(robot.handle_command(command,robot_name,direction,position), "north")
    
    def test_check_area(self):
        """Test the function and if the boundaries exceeded returns to previous
        position"""

        sys.stdout = StringIO()
        output = sys.stdout.getvalue()
        direction = "west"
        position = [50,20]
        command = ["forward","200"]
        robot_name = "HAL"
        self.assertEqual(robot.check_area(direction,command,robot_name,position),[50,20])
