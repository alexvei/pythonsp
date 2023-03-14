import datetime
import os
import tkinter as tk
from tkinter import ttk




def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)


def window():
    global clock_label
    body = tk.Tk()
    body.geometry("300x96")
    body.resizable(False, False)
    body.title('Digital Clock')
    frm = ttk.Frame(body, padding=10)
    frm.grid()
    clock_label = ttk.Label(frm, text="", font=("Hack NF", 32))
    clock_label.grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=body.destroy).grid(column=1, row=0)
    update_time() # call the update_time function to start updating the clock
    body.mainloop()


if __name__ == "__main__":
    window()
