import tkinter as tk
from tkinter import ttk

from action.task_1 import task_1
from tkinter_window.checks import validate_input


def window_tab_1(root, tab1):
    def arr_result_and_display():
        count_str = entry_var.get()
        span = radiobutton_var.get()
        result = task_1(count_str, span)
        result_text.pack()
        result_text.delete("1.0", tk.END)
        result_text.insert("1.0", result)

    validate_input_command_tab1 = root.register(lambda P: validate_input(P, allow_float=False))
    entry_var = tk.StringVar(value=5)
    radiobutton_var = tk.StringVar(value=1)
    text = """Сформировать и заполнить массив случайным числами
    и вывести максимальное, минимальное и среднее значение."""
    ttk.Label(tab1, text=text).pack()
    ttk.Label(tab1, text="Введите количество чисел в массиве:").pack()
    ttk.Entry(tab1, width=5, textvariable=entry_var, validate="key",
              validatecommand=(validate_input_command_tab1, '%P')).pack()
    ttk.Label(tab1, text="Укажите диапазон:").pack()
    ttk.Radiobutton(tab1, value=0, variable=radiobutton_var, text='от 0 до   1').pack()
    ttk.Radiobutton(tab1, value=1, variable=radiobutton_var, text='от 0 до  10').pack()
    ttk.Radiobutton(tab1, value=2, variable=radiobutton_var, text='от 0 до 100').pack()
    ttk.Button(tab1, text='Выполнить', width=20, command=arr_result_and_display).pack()

    result_text = tk.Text(tab1, height=15, width=58)
