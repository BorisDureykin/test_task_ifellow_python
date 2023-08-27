import os
import sys

# Получаем путь к текущему файлу (test_task_1.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Добавляем путь к папке 'action' в системный путь Python
action_path = os.path.join(current_dir, '..', 'action')
sys.path.append(action_path)

from task_1 import task_1

def test_task_1_valid_input():
    result = task_1("5", "0")
    assert isinstance(result, str)
    assert "Заполнен массив:" in result
    assert "Минимальное значение:" in result
    assert "Максимальное значение:" in result
    assert "Среднее значение:" in result

def test_task_1_invalid_input():
    result = task_1("invalid", "0")
    assert isinstance(result, str)
    assert "Введите количество чисел в массиве!" in result

    result = task_1("-1", "0")
    assert isinstance(result, str)
    assert "Количество чисел должно быть больше нуля!" in result

def test_task_1_random_span():
    result = task_1("10", "0")
    assert isinstance(result, str)
    assert "Заполнен массив:" in result
    assert "Минимальное значение:" in result
    assert "Максимальное значение:" in result
    assert "Среднее значение:" in result

def test_task_1_small_span():
    result = task_1("10", "1")
    assert isinstance(result, str)
    assert "Заполнен массив:" in result
    assert "Минимальное значение:" in result
    assert "Максимальное значение:" in result
    assert "Среднее значение:" in result

def test_task_1_large_span():
    result = task_1("10", "2")
    assert isinstance(result, str)
    assert "Заполнен массив:" in result
    assert "Минимальное значение:" in result
    assert "Максимальное значение:" in result
    assert "Среднее значение:" in result
