
from task_4 import task_4

def test_valid_time_1():
    result = task_4(3, 15)
    assert "Угол между стрелками:" in result
    assert "градусов" in result

def test_valid_time_2():
    result = task_4(9, 45)
    assert "Угол между стрелками:" in result
    assert "градусов" in result

def test_valid_time_3():
    result = task_4(12, 0)
    assert "Угол между стрелками:" in result
    assert "градусов" in result

def test_invalid_hour():
    result = task_4(25, 30)
    assert result == "Недопустимое время"

def test_invalid_minute():
    result = task_4(10, 61)
    assert result == "Недопустимое время"

def test_invalid_hour_and_minute():
    result = task_4(25, 70)
    assert result == "Недопустимое время"
