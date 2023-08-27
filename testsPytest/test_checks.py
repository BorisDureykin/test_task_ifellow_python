import os
import sys
import unittest


current_dir = os.path.dirname(os.path.abspath(__file__))
action_path = os.path.join(current_dir, '..', 'tkinter_window')
sys.path.append(action_path)
from checks import validate_input, validate_time_input


class TestValidationFunctions(unittest.TestCase):
    def test_validate_input_integer(self):
        valid_values = ["123", "0", "456"]
        invalid_values = ["12.34", "abc", "-1", "12a"]

        for value in valid_values:
            self.assertTrue(validate_input(value, allow_float=False))

        for value in invalid_values:
            self.assertFalse(validate_input(value, allow_float=False))

    def test_validate_input_float(self):
        valid_values = ["123.45", "0.0", "456.78"]
        invalid_values = ["abc", "-1.2.3", "12a", "12,0"]

        for value in valid_values:
            self.assertTrue(validate_input(value, allow_float=True))

        for value in invalid_values:
            self.assertFalse(validate_input(value, allow_float=True))

    def test_validate_time_input_hours(self):
        valid_values = ["0", "1", "12", "23"]
        invalid_values = ["-1", "24", "abc", "12a"]

        for value in valid_values:
            self.assertTrue(validate_time_input(value, check_hours=True))

        for value in invalid_values:
            self.assertFalse(validate_time_input(value, check_hours=True))

    def test_validate_time_input_minutes(self):
        valid_values = ["0", "1", "59"]
        invalid_values = ["-1", "60", "abc", "12a"]

        for value in valid_values:
            self.assertTrue(validate_time_input(value, check_hours=False))

        for value in invalid_values:
            self.assertFalse(validate_time_input(value, check_hours=False))

