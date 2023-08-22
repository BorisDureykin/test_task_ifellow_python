
def task_2(input_str):
    if not input_str:
        result_text = "Строка пуста"
    else:
        x = []
        for i in input_str:
            if i not in x and input_str.count(i) > 1:
                x.append(i)
        if not x:
            result_text = "Повторяющихся символов нет"
        else:
            symbols = ", ".join(x)
            result_text = f"Проверяем текст: {input_str}\nПовторяющиеся символы: {symbols}"

    return result_text
