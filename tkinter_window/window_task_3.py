import tkinter as tk
from tkinter import ttk

from action.task_3 import BaseConverter
from tkinter_window.checks import validate_input


def window_tab_3(root, tab3):
    def convert_and_display():
        celsius = entry_var.get()
        if not celsius:
            result_label.config(text="Введите значение в градусах С")
            return
        celsius = float(celsius)
        conversion_type = conversion_choices.index(conversion_combobox.get())
        converter = BaseConverter(celsius, conversion_type)
        result = converter.convert(converter.conversion_type)
        units = conversion_combobox.get()
        result_label.config(text=f"Результат: {result:.2f} {units}")

    validate_input_command_tab3 = root.register(lambda P: validate_input(P, allow_float=True))
    entry_var = tk.StringVar(value=0)
    text = """Напишите класс BaseConverter для конвертации из градусов по Цельсию в
                         Кельвины, Фаренгейты, и так далее.
    У метода должен быть метод convert, который и делает конвертацию.
    При запуске кода должна быть возможность ввести градусы Цельсия
                и выбора конвертации в Кельвины или Фаренгейты"""

    ttk.Label(tab3, text=text).pack()
    ttk.Label(tab3, text="Введите значение в градусах С:").pack()
    ttk.Entry(tab3, width=5, textvariable=entry_var, validate="key",
              validatecommand=(validate_input_command_tab3, '%P')).pack()
    ttk.Label(tab3, text="Выберите единицу измерения:").pack()
    conversion_choices = ["Кельвины", "Фаренгейты"]
    conversion_combobox = ttk.Combobox(tab3, values=conversion_choices, state="readonly")
    conversion_combobox.pack()
    conversion_combobox.set(conversion_choices[0])
    ttk.Button(tab3, text='Конвертировать', width=20,
               command=convert_and_display).pack()
    result_label = ttk.Label(tab3, text="", justify="center")
    result_label.pack()
