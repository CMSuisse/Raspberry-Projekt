import random
import string

import tkinter as tk
from tkinter import ttk
from utils import api_handler
import picamera
from time import sleep

from utils import consts

class UI_Handler():
    def __init__(self, resolution: list, fullscreen: bool, bg_color: str, dropdown_font: tuple):
        self.bg_color = bg_color
        # In this dictionary the frames that contain more complex UI elements are stored
        self.frames = {}
        # In this dictionary the string variables that the program uses are stored
        self.variables = {}
        # Initialize the window
        self.window = tk.Tk()
        # Tkinter resolution has to be set with a string of format 000x000
        self.window.geometry("{}x{}".format(resolution[0], resolution[1]))
        self.window.attributes("-fullscreen", fullscreen)
        # Set the font size of the comboboxes dropdown
        self.window.option_add("*TCombobox*Listbox.font", dropdown_font)

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
        relx: float, rely: float, width: int, height: int, anchor: str, callback_function, master=None
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
        button.bind("<Button-1>", callback_function)

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

    # Adds a dropdown menu to a specific label
    def add_dropdown(
        self, options_list: list, default_index: int, var_name: str, font: tuple,
        relx: float, rely: float, width: int, height: int, anchor: str, master=None
    ) -> None:

        if master==None:
            master=self.main_frame

        # Define the default value of the dropdown
        variable = tk.StringVar(master)
        self.variables[var_name] = variable

        entry = ttk.Combobox(
            master,
            width=width,
            height=height,
            textvariable=variable,
            font=font
        )
        entry["state"] = "readonly"
        entry["values"] = options_list
        entry.current(default_index)
        entry.place(relx=relx, rely=rely, anchor=anchor)
    
    def add_slider(
        self, tag: str, start_value: int, end_value: int, is_horizontal: bool, fg_color: str, bg_color: str,
        font: list, relx: float, rely: float, length: int, width: int, anchor: str, master=None
    ) -> None:
        
        if master==None:
            master=self.main_frame

        slider_value = tk.IntVar()
        self.variables[tag] = slider_value
        
        # The highlightbackground attribute is responsible for creating a white border when not set to self.bg_color
        slider = tk.Scale(
            master=master,
            variable=slider_value,
            from_=start_value,
            to=end_value,
            orient=tk.HORIZONTAL if is_horizontal else None,
            fg=fg_color,
            bg=bg_color,
            highlightbackground=self.bg_color,
            length=length,
            width=width,
            font=font
        )
        slider.place(relx=relx, rely=rely, anchor=anchor)

    def add_checkbox(
        self, text: str, font: str, font_size: int, var_name: str, fg_color: str, bg_color: str,
        relx: float, rely: float, width: int, height: int, anchor: str, master=None
    ) -> None:
        
        if master==None:
            master=self.main_frame

        variable = tk.IntVar(master)
        self.variables[var_name] = variable

        checkbox = tk.Checkbutton(
            master=master,
            text=text,
            font=(font, font_size),
            command=None,
            variable=variable,
            fg=fg_color,
            bg=bg_color,
            width=width,
            height=height
        )
        checkbox.place(relx=relx, rely=rely, anchor=anchor)
    
    def popup(self, title: str, text: str) -> None:
        win = tk.Toplevel()
        win.wm_title(title)

        error = tk.Label(
            master=win,
            text=text
        )
        error.pack()
    
    def capture_image(self, API_instance: api_handler.API_Handler) -> None:
        try:
            # Gather the values of the dropdowns and sliders
            resolution = consts.RESOLUTION_SETTINGS[self.variables["resolution"].get()]
            output = self.variables["output"].get()
            preview_length = self.variables["preview_length"].get()
            upload_image = self.variables["upload_image"].get()

            # Add a (probably) unique identifier to allow several images to be saved
            photo_id = "".join(random.choice(string.ascii_letters) for _ in range(10))
            image_path = "/home/pi/projects/Raspberry-Projekt/captures/image_{}.{}".format(
                photo_id, output)

            # Create a camera instance and capture the image
            camera = picamera.PiCamera()
            camera.resolution = resolution
            camera.start_preview()
            sleep(preview_length)
            camera.capture(image_path, format=output)

        except Exception as e:
            # Handle errors with popup here
            self.popup("Error", "An error occured. Please try again. Error: {}".format(e))
        
        else:
            self.popup("Success", 
            "Your image was captured and saved under {}".format(image_path)
            )

        finally:
            camera.close()
            # If the user selected it, upload the image to Flickr
            # Inform the user of the success or failure of his requested action
            if upload_image == 1:
                try:
                    API_instance.upload_capture(image_path)
                except Exception as e:
                    self.popup("Error", "Your image couldn't be uploaded. Error: {}".format(e))
                else:
                    self.popup("Success", "Your image has been uploaded to Flickr")