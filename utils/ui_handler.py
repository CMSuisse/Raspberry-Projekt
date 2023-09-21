chimport tkinter as tk


class UI:
    def __init__(self, resolution: list, fullscreen: bool) -> None:
        # All the labels and buttons will be stored in dicts to edit and delete them
        # based on a tag name
        self.labels = {}
        self.buttons = {}

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
            borderwidth=1
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
            self.quit_button.place(relx=0.99, rely=0.01, anchor="ne")

    # Adds a simple label to a screen with width and heigth fitting the text
    def add_label(
        self, tag: str, text: str, foreground: str, background: str, 
        relx: float, rely: float, anchor: str):

        label = tk.Label(
            master=self.main_frame,
            text=text,
            fg=foreground,
            bg=background
        )
        label.place(relx=relx, rely=rely, anchor=anchor)
        self.labels[tag] = label