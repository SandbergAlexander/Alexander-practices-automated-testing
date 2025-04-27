import os
import tkinter as tk 
import time 
import TEST_RUNER as  testing

root = tk.Tk()
root.geometry("1024x1024")
root.title ("TESTING")
text = tk.Label(root,text="Hej Vill du starta ett test?",font=2)
def test():
    tex_start = tk.Label(root,text="start",font=22)
   # tex_start.pack()
    testing.testR()
  

text.pack()
button = tk.Button(root,text="start",command=test)
button.pack()
root.mainloop()
