import os
import tkinter as tk 
import time 

root = tk.Tk()

root.geometry("1024x1024")
root.title ("TESTING")
text = tk.Label(root,text="Hej Vill du starta ett test?")
def test_01():
    tex_start = tk.Label(root,text="start")
    tex_start.pack()

text.pack()
test_01()

root.mainloop()