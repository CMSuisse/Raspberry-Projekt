import tkinter as tk
from tkinter import ttk


class UI():
    def __init__(self, resolution: list, fullscreen: bool, bg_color: str) -> None:
        self.bg_color = bg_color
        # In this dictionary the frames that contain more complex UI elements are stored
        self.frames = {}
        # Initialize the window
        self.window = tk.Tk()
        # Tkinter resolution has to be set with a string of format 000x000
        self.window.geometry("{}x{}".format(resolution[0], resolution[1]))
        self.window.attributes("-fullscreen", fullscreen)

        # Define a frame with the size of the window
        # Frame instances are easier to work with than Tk instances
        self.main_frame = tk.Frame(
            master=self.window,
            width=resolution[0],
            height=resolution[1],
            borderwidth=1,
            bg=bg_color
        )
        self.main_frame.pack()

        # Also define a quit button if fullscreen is on
        # The top bar containing a quit button disappears when
        # fullscreen is true
        if fullscreen:
            self.quit_button = tk.Button(
                master=self.main_frame,
                text="x",
                bg="red",
                command=self.window.destroy
            )
            self.quit_button.place(relx=0.99, rely=0.075, anchor="se")

    # Adds a simple label to the screen  
    def add_label(
        self, text:str, font: str, font_size: int, foreground: str, background:str,
        relx: float, rely: float, width: int, height: int, anchor: str, master=None
    ) -> None:

        if master==None:
            master=self.main_frame
        
        label = tk.Label(
            master=master,
            text=text,
            font=(font, font_size),
            fg=foreground,
            bg=background,
            width=width,
            height=height
        )
        label.place(relx=relx, rely=rely, anchor=anchor)

    def add_button(
        self, text: str, font: str, font_size: int, foreground: str, background: str,
        relx: float, rely: float, width: int, height: int, anchor: str, master=None
    ) -> None:

        if master==None:
            master=self.main_frame
        
        button = tk.Button(
            master=master,
            text=text,
            font=(font, font_size),
            fg=foreground,
            bg=background,
            width=width,
            height=height
        )
        button.place(relx=relx, rely=rely, anchor=anchor)

    def add_frame(
        self, tag: str, border: bool,
        relx: float, rely: float, width: int, height: int, anchor: str
    ) -> None:
        
        # The frames are only used as a container for UI elements and therefore shouldn't stand out
        frame = tk.Frame(
            master=self.main_frame,
            width=width,
            height=height,
            bg=self.bg_color,
            highlightbackground="black",
            highlightthickness=1 if border else 0
        )
        frame.place(relx=relx, rely=rely, anchor=anchor)
        # Add the frame to the dictionary to access it via its tag
        self.frames[tag] = frame

    def add_dropdown(
        self, options_list: list,
        relx: float, rely: float, width: int, height: int, anchor: str, master=None
    ) -> None:

        if master==None:
            master=self.main_frame

        # Define the default value of the dropdown
        variable = tk.StringVar(master)

        entry = ttk.Combobox(
            master,
            width=width,
            height=height,
            textvariable=variable
        )
        entry["values"] = options_list
        entry.place(relx=relx, rely=rely, anchor=anchor)