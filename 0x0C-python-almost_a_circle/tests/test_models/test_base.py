#!/usr/bin/python3
""" Unittest for base.py """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ testcase is created by subclassing unittest.TestCase """
    def setUp(self):
        """ Prepare the test fixture - Assign private class attribute """
        Base._Base__nb_objects = 0

    def test_create_instance_id_int(self):
        """ Testing id property with int type """
        tbase = Base(10)
        self.assertEqual(tbase.id, 10)

    def test_create_instance_id_int_neg(self):
        """ testing id property with negative int type """
        tbase = Base(-10)
        self.assertEqual(tbase.id, -10)

    def test_create_instance_id_float(self):
        """testing id property with float type """
        tbase = Base(2.15)
        self.assertEqual(tbase.id, 2.15)

    def test_create_instance_id_empty(self):
        """ testing id property withouth attribute """
        tbase = Base()
        self.assertEqual(tbase.id, 1)

    def test_create_instance_id_None(self):
        """ testing id property with None type """
        tbase = Base(None)
        self.assertEqual(tbase.id, 1)

    def test_create_instance_id_moreargs(self):
        """ testing id property with more than one argument """
        with self.assertRaises(TypeError):
            tbase = Base(6, 3)

    def test_check_private_attribute(self):
        """ checking private attribute __nb_objects """
        tbase = Base()
        with self.assertRaises(AttributeError):
            tbase.__nb_objects

if __name__ == '__main__':
    unittest.main()
