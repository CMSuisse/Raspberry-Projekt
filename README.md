# Raspberry-Projekt
Dieses EF Informatik Projekt hatte das Ziel, eine Rapsberry Pi so zu programmieren, dass sie gleichzeitig mit physischen Geräten interagiert, sich aber auch mit APIs mit dem Internet verbindet. Die Anleitung zum Setup meines finalen Produkts lautet wie folgt (auf Englisch):

<ins>You will need:</ins>  
- A RaspberryPi (obviously)\
- A RaspberryPi Touch Display\
- A RasperryPi PiCamera

<ins>You should do the follwing:</ins>  
- Connect the Touch Display to the RaspberryPi.
- Connect the PiCamera to the RaspberryPi.
- Save this repo in its entirety on your RaspberryPi.
- Create a .env file and include a valid Flickr API key and and secret (as strings).
    The file has to look like this:
    ```
    API_KEY = #Your key here
    SECRET = #Your secret here
    ```

- Update the file path in the "cyrill_main.sh" so that it points to the "main.py" file of the repo.
- Move the "cyrill_main.sh" file to the Pi's Desktop and make it executable.
- Execute "cyrill_main.sh" (preferable with terminal output).
- It's possible that you will be prompted to input a code for the Flickr write permission once:
    - Plug in a Keyboard and a mouse.
    - Navigate to the opened webbrowser window.
    - Enter your Flickr credentials.
    - Enter the code into the terminal window (requires "Execute in Terminal").
- The main UI window should now open and you will be able to capture and upload images without any disturbance.

<ins>You should now be able to:</ins>  
- Select from a list of possble 16:9 aspect ratio resolutions.
- Select from a list of possible output formats.
- Select a length for which the camera should preview its output.
- Capture an image which will auomatically saved under "captures/".
- Select an option to automatically upload a captured image to the Flickr account your key and secret are attached to.