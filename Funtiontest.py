# color_code_system/test_color_converter.py

import unittest
from .color_converter import get_color_from_pair_number, get_pair_number_from_color, color_pair_to_string
from .color_constants import MAJOR_COLORS, MINOR_COLORS

class TestColorConverter(unittest.TestCase):
    def test_number_to_pair(self):
        self.assertEqual(get_color_from_pair_number(4), ('White', 'Brown'))
        self.assertEqual(get_color_from_pair_number(5), ('White', 'Slate'))
        self.assertEqual(get_color_from_pair_number(10), ('Red', 'Slate')) # Nuevo test
        self.assertEqual(get_color_from_pair_number(1), ('White', 'Blue')) # Nuevo test

    def test_pair_to_number(self):
        self.assertEqual(get_pair_number_from_color('Black', 'Orange'), 12)
        self.assertEqual(get_pair_number_from_color('Violet', 'Slate'), 25)
        self.assertEqual(get_pair_number_from_color('Red', 'Orange'), 7)
        self.assertEqual(get_pair_number_from_color('White', 'Blue'), 1) # Nuevo test

    def test_invalid_pair_number_to_color(self):
        with self.assertRaises(ValueError):
            get_color_from_pair_number(0)
        with self.assertRaises(ValueError):
            get_color_from_pair_number(-1)
        with self.assertRaises(TypeError): # Para caso no int
            get_color_from_pair_number(4.5)
        with self.assertRaises(IndexError):
            
            get_color_from_pair_number(len(MAJOR_COLORS) * len(MINOR_COLORS) + 1)

    def test_invalid_color_to_pair_number(self):
        with self.assertRaises(ValueError):
            get_pair_number_from_color('InvalidColor', 'Blue')
        with self.assertRaises(ValueError):
            get_pair_number_from_color('White', 'InvalidColor')

    def test_color_pair_to_string(self):
        self.assertEqual(color_pair_to_string('White', 'Brown'), 'White Brown')
        self.assertEqual(color_pair_to_string('Red', 'Green'), 'Red Green')

if __name__ == '__main__':
    unittest.main() # Esto corre todos los tests en esta clase
