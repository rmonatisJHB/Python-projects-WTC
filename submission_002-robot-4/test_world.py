import unittest
from world.text import world


class Test_Function(unittest.TestCase):

    def test_is_position_allowed(self):
        new_x = 105
        new_y = 201
        self.assertEqual(world.is_position_allowed(new_x,new_y),False)
    

    def test_update_position(self):
        steps = 300
        robot_name = 'HAL'
        self.assertEqual(world.update_position(steps,robot_name),False)
    
    def test_do_forward(self):
        steps = 10
        robot_name = 'HAL'
        output = True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
        self.assertEqual(world.do_forward(robot_name,steps), output)
    
    def test_do_back(self):
        steps = 20
        robot_name = 'HAL'
        output = True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
        self.assertEqual(world.do_back(robot_name,steps),output) 