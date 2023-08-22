import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Button

from tkinter_window.window_task_1 import window_tab_1
from tkinter_window.window_task_2 import window_tab_2
from tkinter_window.window_task_3 import window_tab_3
from tkinter_window.window_task_4 import window_tab_4

def main_window():
    root = tk.Tk()
    root.title("test_task_ifellow_python")
    tabControl = ttk.Notebook(root,  height = 300, width = 480)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='Задача 1')
    tabControl.add(tab2, text='Задача 2')
    tabControl.add(tab3, text='Задача 3')
    tabControl.add(tab4, text='Задача 4')
    tabControl.pack(expand=1, fill="both")

    window_tab_1(root,tab1)

    window_tab_2(tab2)

    window_tab_3(root,tab3)

    window_tab_4(root, tab4)

    btn = Button(root, text='Выход', width=20,
                  command=root.quit)
    btn.pack()
    root.mainloop()
