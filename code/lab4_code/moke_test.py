import unittest
import sys, os
from unittest.mock import patch, Mock

import composite

sys.path.append(os.getcwd())
from composite import *


class TestComposite(unittest.TestCase):
    @patch.object(composite.Comp, 'cost')
    def test_comp_cost(self, mock_cost):
        mock_cost.return_value = "100"
        Equipment = Comp ('HP')
        self.assertEqual(Equipment.cost(), "100")