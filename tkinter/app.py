from tkinter import *
import tkinter.ttk as ttk

s = ttk.Style()

print(s.theme_names())
print(s.theme_use())

themes = ('clam', 'alt', 'default', 'classic')

s.theme_use("clam")


