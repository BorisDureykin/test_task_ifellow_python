import tkinter as tk
from tkinter import ttk


from action.task_4 import task_4
from tkinter_window.checks import validate_time_input


def window_tab_4(root, tab4):
    def calculate_and_display_angle(hours, minutes, label):
        if not hours or not minutes:
            angle_result = "Недопустимое время"
        else:
            try:
                angle_result = task_4(int(hours), int(minutes))
            except ValueError:
                angle_result = "Недопустимое время"
        label.config(text=angle_result)

    validate_time_input_command_hours = root.register(lambda P: validate_time_input(P, check_hours=True))
    validate_time_input_command_minutes = root.register(lambda P: validate_time_input(P, check_hours=False))
    hour_var = tk.StringVar(value=0)
    minute_var = tk.StringVar(value=0)

    text = """Напишите метод, который будет вычислять угол между часовой и минутной стрелками часов.
    На вход функции подаётся время в виде двух переменных: "hours" и "minutes".
    Расчет угла производить относительно реального поведения стрелок часов."""
    ttk.Label(tab4, text=text).pack()
    ttk.Label(tab4, text="Введите время").pack()
    ttk.Label(tab4, text="Часы:").pack()
    ttk.Entry(tab4, width=5, textvariable=hour_var, validate="key",
              validatecommand=(validate_time_input_command_hours, '%P')).pack()

    ttk.Label(tab4, text="Минуты:").pack()
    ttk.Entry(tab4, width=5, textvariable=minute_var, validate="key",
              validatecommand=(validate_time_input_command_minutes, '%P')).pack()
    result_button = ttk.Button(tab4, text='Рассчитать угол', width=20,
                               command=lambda: calculate_and_display_angle(hour_var.get(), minute_var.get(), result_label))
    result_button.pack()
    result_label = ttk.Label(tab4, text="", justify="center")
    result_label.pack()
