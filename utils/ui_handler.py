import tkinter as tk


class UI():
    def __init__(self, resolution: list, fullscreen: bool, bg_color: str) -> None:
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
        relx: float, rely: float, width: int, height: int, anchor: str) -> None:
        
        label = tk.Label(
            master=self.main_frame,
            text=text,
            font=(font, font_size),
            fg=foreground,
            bg=background,
            width=width,
            height=height
        )
        label.place(relx=relx, rely=rely, anchor=anchor)

    def add_button(
        self
    ) -> None:
        pass