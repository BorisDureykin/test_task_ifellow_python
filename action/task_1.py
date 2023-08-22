import random


def task_1(count_str, span):
    try:
        count = int(count_str)
        span = int(span)
    except ValueError:
        result_text = "Введите количество чисел в массиве!!"
        return  result_text
    if count <= 0:
        result_text = "Количество чисел должно быть больше нуля!"
        return result_text

    arr = []
    c = min_arr = max_arr = avg_arr = 0
    for i in range(count):
        if span == 0:
            c = random.random()
        if span == 1:
            c = random.randint(0, 10)
        if span == 2:
            c = random.randint(0, 100)
        arr.append(c)

    min_arr = min(arr)
    max_arr = max(arr)
    avg_arr = sum(arr) / count
    result_text = f"Заполнен массив: {arr};\nМинимальное значение: {min_arr};\nМаксимальное значение: {max_arr};\nСреднее значение: {avg_arr};\n"
    return result_text
