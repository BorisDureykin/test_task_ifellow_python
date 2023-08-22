import tkinter as tk
from tkinter import ttk

from action.task_2 import task_2


def window_tab_2(tab2):
    def str_and_display_symbols(input_str, label):
        result_text = task_2(input_str)
        label.config(text=result_text)
        result_label.pack()
        ok_button.pack()

    def hide_result():
        result_label.pack_forget()
        ok_button.pack_forget()
        entry_var.set("")

    entry_var = tk.StringVar(value='Hello')
    text = """Написать программу, которая должна найти и вывести
     повторяющийся символ в введенном тексте"""
    ttk.Label(tab2, text=text).pack()
    ttk.Label(tab2, text="Введите текст:").pack()
    entry = ttk.Entry(tab2, width=30, textvariable=entry_var)
    entry.pack()
    find_button = ttk.Button(tab2, text="""Найти повторяющиеся
                символы""", width=23, command=lambda: str_and_display_symbols(entry_var.get(), result_label))
    find_button.pack()
    ok_button = ttk.Button(tab2, text="Ok", width=23, command=hide_result)

    result_label = ttk.Label(tab2, text="", justify="center")
    