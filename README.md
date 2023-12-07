# Raspberry-Projekt
Dieses EF Informatik Projekt hatte das Ziel, eine Raspberry Pi so zu programmieren, dass sie gleichzeitig mit physischen Geräten interagiert, sich aber auch via APIs mit dem Internet verbindet. Die Anleitung zum Setup meines finalen Produkts lautet wie folgt (auf Englisch):

<h4>You will need:</h4>  

- A RaspberryPi (obviously)
- A RaspberryPi Touch Display
- A RasperryPi PiCamera

<h4>You should do the follwing:</h4>  

- Connect the Touch Display to the RaspberryPi.
- Connect the PiCamera to the RaspberryPi.
- Save this repo in its entirety on your RaspberryPi.
- Create a <ins>.env</ins> file simply called <ins>.env</ins> on the repo's top folder including a valid Flickr API key and secret.
The file has to look like this:
    ```
    API_KEY = #"Your key here"
    SECRET = #"Your secret here"
    ```
- Update the file path in [cyrill_main.sh](cyrill_main.sh) so that it points to the [main.py](main.py) file.
- Move the [cyrill_main.sh](cyrill_main.sh) file to the Pi's Desktop and make it executable by running
    ```
    chmod u+x cyrill_main.sh
    ```
- Execute [cyrill_main.sh](cyrill_main.sh) (preferrably with terminal output).
- It's possible that you will be prompted to input a code for a Flickr write permission once:
    - Plug in a Keyboard and a mouse.
    - Navigate to the opened webbrowser window.
    - Enter your Flickr credentials.
    - Enter the code into the terminal window (requires "Execute in Terminal").
- The main UI window should now open and you will be able to capture and upload images without any disturbance.

<h4>You should now be able to:</h4>

- Select from a list of possible 16:9 aspect ratio resolutions.
- Select from a list of possible output formats.
- Select a length for which the camera should preview its output.
- Capture an image which will automatically be saved in the <ins>captures</ins> folder.
- Select an option to automatically upload a captured image to the Flickr account your key and secret are attached to.

Hopefully this introduction was helpfull. If you're nonetheless encountering problems, fell free to contact me.