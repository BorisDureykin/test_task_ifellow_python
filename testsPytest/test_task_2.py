
from task_2 import task_2


def test_task_2_empty_string():
    result = task_2("")
    assert "Строка пуста" in result

def test_task_2_no_repeating_symbols():
    result = task_2("abcdef")
    assert "Повторяющихся символов нет" in result

def test_task_2_repeating_symbols():
    result = task_2("aabbcdd")
    assert "Проверяем текст: aabbcdd" in result
    assert "Повторяющиеся символы: a, b, d" in result

def test_task_2_special_characters():
    result = task_2("!@#$%^&*()")
    assert "Повторяющихся символов нет" in result

def test_task_2_mixed_characters():
    result = task_2("aabbcc!@#")
    assert "Проверяем текст: aabbcc!@#" in result
    assert "Повторяющиеся символы: a, b, c" in result
