# Screen resolution 800x480p
from enum import Enum

from utils.ui_handler import UI
from utils.consts import Anchor

try:
    UI_instance = UI([500, 100], False)
    UI_instance.add_label("test", "Hello World", "white", "black", 0.5, 0.5, Anchor.TOPLEFT.value)
finally:
    UI_instance.window.mainloop()