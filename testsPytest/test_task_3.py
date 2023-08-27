import os
import sys

import pytest

current_dir = os.path.dirname(os.path.abspath(__file__))

action_path = os.path.join(current_dir, '..', 'action')
sys.path.append(action_path)

from task_3 import BaseConverter

def test_convert_to_kelvin():
    converter = BaseConverter(celsius=25, conversion_type=0)
    result = converter.convert(conversion_type=0)
    assert result == 298.15

def test_convert_to_fahrenheit():
    converter = BaseConverter(celsius=25, conversion_type=1)
    result = converter.convert(conversion_type=1)
    assert result == 77.0

def test_invalid_conversion_type():
    converter = BaseConverter(celsius=25, conversion_type=2)
    with pytest.raises(ValueError, match="Недопустимый тип конвертации"):
        converter.convert(conversion_type=2)
