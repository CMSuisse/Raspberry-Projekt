from utils.api_handler import API_Handler
import flickrapi

api = API_Handler()
print(api.token_valid(perms="write"))
#api.upload_capture("/home/pi/projects/Raspberry-Projekt/captures/image.jpeg")