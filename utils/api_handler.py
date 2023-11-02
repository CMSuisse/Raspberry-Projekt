import random
import string
import webbrowser

import dotenv
from flickrapi.core import FlickrAPI

class API_Handler(FlickrAPI):
    # Grab the values from the .env file directly instead of them being passed
    # as parameters for __init__
    def __init__(self):
        config = dotenv.get_variables("/home/pi/projects/Raspberry-Projekt/.env")
        api_key = str(config["API_KEY"])
        api_secret = str(config["SECRET"])
        super().__init__(api_key, api_secret)

        # Validate that a write permission token exists
        # Otherwise ask user to create one
        if not self.token_valid(perms="write"):
            self.get_request_token(oauth_callback="oob")

            # Open a browser where a token can be requested
            authorization_url = self.auth_url(perms="write")
            webbrowser.open_new_tab(authorization_url)
            verifier = str(input("Verification code: "))

            self.get_access_token(verifier)

    def upload_capture(self, photo_path: str) -> None:
        params = {}
        # Add a (probably) unique identifier to avoid errors when uploading
        photo_id = "".join(random.choice(string.ascii_letters) for _ in range(10))

        params["file_name"] = photo_path
        params["title"] = photo_path.split("/")[-1] + "_" + photo_id
        params["description"] = "Image uploaded using FlickrAPI"
        self.upload_photo(**params)