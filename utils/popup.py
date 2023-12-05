import tkinter as tk

# Create a window above everything else and show the provided text
def popup(title: str, text: str) -> None:
        win = tk.Toplevel()
        win.wm_title(title)

        content = tk.Label(
            master=win,
            text=text
        )
        content.pack()