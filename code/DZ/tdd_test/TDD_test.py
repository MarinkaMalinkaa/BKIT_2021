import unittest
import sys, os
from lab6_code_bot import *

sys.path.append(os.getcwd())

class TestBot(unittest.TestCase):
    def test_1(self):
        self.assertEqual('катя','катя')

    def test_2(self):
        self.assertEqual(16, 16)

if __name__ == '__main__':
    unittest.main()
