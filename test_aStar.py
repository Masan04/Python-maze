import unittest
from pyamaze import maze
from aStar import getNextCell, h
from aStar import aStar

class TestHFunction(unittest.TestCase):

    def test_h(self):
        self.assertEqual(h((0, 0), (3, 4)), 7)
        self.assertEqual(h((1, 1), (1, 1)), 0)
        self.assertEqual(h((5, 3), (1, 2)), 5)

class TestGetNextCell(unittest.TestCase):

    def test_east_direction(self):
        currCell = (3, 5)
        expected_child_cell = (3, 6)
        self.assertEqual(getNextCell('E', currCell), expected_child_cell)

    def test_west_direction(self):
        currCell = (3, 5)
        expected_child_cell = (3, 4)
        self.assertEqual(getNextCell('W', currCell), expected_child_cell)

    def test_north_direction(self):
        currCell = (3, 5)
        expected_child_cell = (2, 5)
        self.assertEqual(getNextCell('N', currCell), expected_child_cell)

    def test_south_direction(self):
        currCell = (3, 5)
        expected_child_cell = (4, 5)
        self.assertEqual(getNextCell('S', currCell), expected_child_cell)

class TestAStar(unittest.TestCase):

    def test_maze_not_initialized_throws_error(self):
        def call_aStar_without_maze():
            aStar(None,(10, 15))
       
        with self.assertRaises(ValueError) as error_context:
            call_aStar_without_maze()
        expected_error_message = "Maze object cannot be None."
        self.assertEqual(str(error_context.exception), expected_error_message)



    def test_aStar(self):
        m=maze(4,4)
        m.CreateMaze(loadMaze='aStardemo.csv')
        start = (4,4)

        search_path, a_path, fwd_path = aStar(m, start)

        self.assertEqual(search_path[0], start)
        self.assertEqual(search_path[-1], m._goal)
        self.assertEqual(m._goal, (1,1))
        self.assertNotEqual(m._goal, (2,3))
       

if __name__ == '__main__':
    unittest.main()