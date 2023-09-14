# Screen resolution 800x480p

import tkinter

window = tkinter.Tk()

test = tkinter.Label(
    text="Hello World",
    fg="white",
    bg="black",
    width=800,
    height=480
)

test.pack()
window.mainloop()