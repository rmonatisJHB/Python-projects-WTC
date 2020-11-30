import unittest
from world import obstacles


class Test_Functions(unittest.TestCase):

    def test_get_obstacles(self):
        self.assertEqual(type(obstacles.obs_list), list)

    def test_is_position_blocked(self):
       obstacles.obs_list = [[(17, 22)], [(80, 24)], [(39, -79)]] 
       x = 19
       y = 24
       self.assertTrue(obstacles.is_position_blocked(x,y))
    
    def test_is_path_blocked(self):
        obstacles.obs_list = [[(17, 22)], [(80, 24)], [(39, -79)]]
        x1 = 19
        x2 = 19
        y1 = 16
        y2 = 30
        blocked = True
        self.assertEqual(obstacles.is_path_blocked(x1,y1,x2,y2),blocked)