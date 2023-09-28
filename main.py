# Screen resolution 800x480

from utils.ui_handler import UI
from utils.consts import Anchor, RESOLUTION_SETTINGS

# Set up the window
try:
    UI_instance = UI([800, 480], True, "#B0B0B0")

    # Add all frames
    UI_instance.add_frame(
        "resolution_frame", True,
        0.1, 0.15, 400, 100, Anchor.CENTER.value
    )

    # Add all labels
    UI_instance.add_label(
        "RaspberryPhoto v.1", "Arial", 25, "white", "black",
        0.5, 0.1, 800, None, Anchor.TOP.value
    )
    UI_instance.add_label(
        "Enter your preferred resolution setting:", "Arial", 13, "black", UI_instance.bg_color,
        0.5, 0.1, None, None, Anchor.TOP.value, UI_instance.frames["resolution_frame"]
    )

    # Add all buttons
    UI_instance.add_button(
        "CAPTURE", "Arial", 25, "white", "black",
        0.5, 0.95, None, None, Anchor.BOTTOM.value
    )

    # Add all dropdowns
    UI_instance.add_dropdown(
        list(RESOLUTION_SETTINGS.keys()),
        0.5, 0.5, None, None, Anchor.CENTER.value, UI_instance.frames["resolution_frame"]
    )

# Then let it run
finally:
    UI_instance.window.mainloop()