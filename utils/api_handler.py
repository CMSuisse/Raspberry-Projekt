import instagrapi

class API_Handler():
    def __init__(self, username, password):
        self.client = instagrapi.Client()
        try:
            self.client.login(username=username, password=password)
        except Exception as e:
            print("The Login failed. The returned error message is: {}".format(str(e)))

    def upload_image(self, image_path: str, caption: str):
        try:
            media = self.client.album_upload(
                path=image_path, 
                caption=caption,
                extra_data={
                    "like_and_view_counts_disabled": 1,
                    "disable_comments": 1
                }
            )
        except Exception as e:
            print("Your image couldn't be uploaded. The returned error message is: {}".format(str(e)))
        else:
            print("Image uploaded successfully")
            print(media.dict())