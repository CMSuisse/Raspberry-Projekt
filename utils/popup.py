import tkinter as tk

def popup(title: str, text: str) -> None:
        win = tk.Toplevel()
        win.wm_title(title)

        error = tk.Label(
            master=win,
            text=text
        )
        error.pack()