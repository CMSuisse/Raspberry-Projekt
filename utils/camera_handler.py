import random
import string

from utils import api_handler
import picamera
from time import sleep


from utils import consts

class Camera_Handler():
    # Overlay the countdown onto the preview of the PiCamera
    def do_countdown(self, camera: picamera.PiCamera, preview_length: int) -> None:
        sleep(preview_length)
    
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
            cam_prev = camera.start_preview()
            cam_prev.fullscreen = False
            # Create window using the 16:9 aspect ratio that all resolutions have
            cam_prev.window = (0, 0, self.resolution[0]//2, self.resolution[0]//2*9//16)
            self.do_countdown(camera, preview_length)
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