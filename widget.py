import tkinter as tk
from tkinter import Tk, Text, Button, messagebox, Frame, Label
import pyperclip
import re

"""
창에 복붙하면 개행문자 처리해서 클립보드에 복사해주는것 구현
"""

root = Tk()
# root.wm
root.geometry('600x400')
root.title('Copy & Paste text from *.pdf file.')
root.resizable(True,True)

def click():
    text = input_lines.get('1.0','end')
    text = text.replace('\n\n','alkdjfnkdsjfnaljen')
    text = text.replace('-\n','')
    text = text.replace('\n',' ')
    text = text.replace('. ','.\n')
    text = text.replace('alkdjfnkdsjfnaljen','\n\n')
    print(text)
    pyperclip.copy(text)
    messagebox.Message("Converted & Copied.")
    
input_lines = Text(root)
input_lines.pack(side=tk.LEFT)

button = Button(input_lines, text="convert" ,width=10, command=click)
# button.config(text='convert')
# button.config(width=10)
# button.config(command=click)
button.pack(side=tk.BOTTOM)

frame_output = Text(root)
frame_output.pack(side=tk.RIGHT)

root.mainloop()