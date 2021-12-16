import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *

class TddTest(unittest.TestCase):
    def test_first_task(self):
        one_to_many = [(c.brand, c.price, d.name)
                       for d in disp_classes
                       for c in comps
                       if c.disp_cls_id == d.id]
        self.assertEqual(first_task(one_to_many), [('Asus', 'А-класс'), ('Acer', 'Б-класс')])

    def test_2(self):
        one_to_many = [(c.brand, c.price, d.name)
                       for d in disp_classes
                       for c in comps
                       if c.disp_cls_id == d.id]
        self.assertEqual(second_task(one_to_many), [('А-класс', 55390), ('В-класс', 78940), ('Б-класс', 97450)])

    def test_3(self):
        many_to_many_temp = [(d.name, dc.disp_cls_id, dc.comp_id)
                             for d in disp_classes
                             for dc in comps_disp_classs

                             if d.id == dc.disp_cls_id]
        many_to_many = [(c.brand, c.price, disp_class_name)
                        for disp_class_name, disp_cls_id, comp_id in many_to_many_temp
                        for c in comps if c.id == comp_id]
        self.assertEqual(third_task(many_to_many),
                         [('Acer', 'Б-класс'), ('Acer', 'Е-класс'), ('Asus', 'А-класс'), ('Asus', 'Д-класс'),
                          ('HP', 'А-класс'), ('HP', 'Е-класс'), ('Lenovo', 'В-класс'), ('Lenovo', 'Д-класс'),
                          ('ThinkPad', 'В-класс'), ('ThinkPad', 'Г-класс')])

if __name__=='__main__':
    unittest.main()