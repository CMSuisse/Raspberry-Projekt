import random
import string
from time import sleep

import picamera
import tkinter as tk

from utils.api_handler import API_Handler
from utils.popup import popup
from utils.consts import ANCHOR

class Camera_Handler(picamera.PiCamera):
    # This class is a picamera but also stores user-defined parameters
    def __init__(self, 
            preview_length: int, 
            resolution: list, 
            output: str, 
            should_upload: int,
            UI_instance):
        super().__init__()
        # These are the user-defined values
        self.resolution = resolution
        self.output_format = output
        self.preview_length = preview_length
        self.should_upload = should_upload
        # This is the UI_Handler instance the camera "belongs" to
        self.ui_instance = UI_instance
        # Precalculate the dimensions of the preview window
        # 1 is equal to screen width, 2 is 1/2 screen width, etc (for a 360p).
        cam_prev_width_factor = 1.1
        # Adjust for the different possible resolutions by scaling to a 360p
        cam_prev_width_factor_resolution = cam_prev_width_factor/(640/self.resolution[0])
        # Center the window in the x-axis and add set a y-offset
        self.prev_window_x_pos = 400 - int(self.resolution[0]/cam_prev_width_factor_resolution)//2
        self.prev_window_y_pos = 10
        # Set width and height while conserving the 16:9 aspect ratio of the resolution
        self.prev_window_width = int(self.resolution[0]/cam_prev_width_factor_resolution)
        self.prev_window_height = int(self.resolution[0]/cam_prev_width_factor_resolution)*9//16

    # Create a new temporary window to contain the countdown
    def do_countdown(self) -> None:
        # Create top level full screen window
        countdown_window = tk.Toplevel(self.ui_instance.window)
        countdown_window.configure(bg=self.ui_instance.bg_color)
        countdown_window.attributes("-fullscreen", True)
        # Then start the preview
        cam_prev = self.start_preview()
        cam_prev.fullscreen = False
        # Create the preview window using the precalculated values
        cam_prev.window = (self.prev_window_x_pos,
                        self.prev_window_y_pos,
                        self.prev_window_width,
                        self.prev_window_height)
        # Then do the countdown
        counter = self.preview_length
        while counter > 0:
            self.ui_instance.add_label(str(counter), "Arial", 100, "black", 
                self.ui_instance.bg_color, 0.5, 0.99, 100, None, ANCHOR.BOTTOM.value, countdown_window)
            # Normally, Tkinter waits until the program is idle but we want an update now
            self.ui_instance.window.update()
            sleep(1)
            counter -= 1
        # This takes ridiculously long sometimes, but i dont really care about fixing it
        countdown_window.destroy()
    
    def capture_image(self, API_instance: API_Handler) -> None:
        try:
            # Add a (probably) unique identifier to allow several images to be saved
            photo_id = "".join(random.choice(string.ascii_letters) for _ in range(10))
            image_path = "/home/pi/projects/Raspberry-Projekt/captures/image_{}.{}".format(
                photo_id, self.output_format)

            self.do_countdown()
            self.capture(image_path, format=self.output_format)

        except Exception as e:
            # Handle errors with popup here
            popup("Error", "An error occured. Please try again. Error: {}".format(e))
        
        else:
            popup("Success", "Your image was captured and saved under {}".format(image_path))

        finally:
            self.close()
            # If the user selected it, upload the image to Flickr
            # Inform the user of the success or failure of his requested action
            if self.should_upload == 1:
                try:
                    API_instance.upload_capture(image_path)
                except Exception as e:
                    popup("Error", "Your image couldn't be uploaded. Error: {}".format(e))
                else:
                    popup("Success", "Your image has been uploaded to Flickr")
