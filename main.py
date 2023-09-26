# Screen resolution 800x480
from time import sleep

from utils.ui_handler import UI
from utils.consts import Anchor

# Set up the window
try:
    UI_instance = UI([800, 480], True, "#B0B0B0")
    UI_instance.add_label("RaspberryPhoto v.1", "Arial", 25, "white", "black", 0.5, 0.1, 800, None, Anchor.TOP.value)

# Then let it run
finally:
    UI_instance.window.mainloop()