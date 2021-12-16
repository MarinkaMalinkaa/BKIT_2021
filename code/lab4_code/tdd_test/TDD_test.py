import unittest
import sys, os
from composite import *

sys.path.append(os.getcwd())

class TestPartCost(unittest.TestCase):
    def test_part_cost_is_working(self):
        ControlDivices = ComplexPart('Control divices')
        ControlDivices.add_product(Part('Mouse', 800))
        ControlDivices.add_product(Part('Keyboard', 1920))
        self.assertEqual(ControlDivices.cost(), 2720)

    def test_part_cost_receives_string_is_working(self):
        ControlDivices = ComplexPart('Control divices')
        ControlDivices.add_product(Part('Mouse', '800'))
        ControlDivices.add_product(Part('Keyboard', '1920'))
        self.assertIsInstance(ControlDivices.cost(), float)


if __name__ == '__main__':
    unittest.main()
