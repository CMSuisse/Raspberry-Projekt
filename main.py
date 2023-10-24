# Screen resolution 800x480

from utils.ui_handler import UI
from utils.consts import Anchor, RESOLUTION_SETTINGS, OUTPUT_SETTINGS

# Set up the window
try:
    UI_instance = UI([800, 480], True, "#B0B0B0")

    # Add all frames
    UI_instance.add_frame(
        "resolution_frame", True,
        0.01, 0.2, 380, 100, Anchor.TOPLEFT.value
    )
    UI_instance.add_frame(
        "output_format_frame", True,
        0.99, 0.2, 380, 100, Anchor.TOPRIGHT.value
    )
    UI_instance.add_frame(
        "preview_countdown_frame", True,
        0.8, 0.9, 200, 75, Anchor.CENTER.value
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
    UI_instance.add_label(
        "Enter your prefered output format", "Arial", 13, "black", UI_instance.bg_color,
        0.5, 0.1, None, None, Anchor.TOP.value, UI_instance.frames["output_format_frame"]
    )
    UI_instance.add_label(
        "Preview length", "Arial", 13, "black", UI_instance.bg_color,
        0.5, 0.1, None, None, Anchor.TOP.value, UI_instance.frames["preview_countdown_frame"]
    )

    # Add all buttons
    UI_instance.add_button(
        "CAPTURE", "Arial", 25, "white", "black",
        0.5, 0.9, None, None, Anchor.CENTER.value, UI_instance.capture_image
    )

    # Add all dropdowns
    UI_instance.add_dropdown(
        list(RESOLUTION_SETTINGS.keys()), "resolution",
        0.5, 0.5, None, None, Anchor.CENTER.value, UI_instance.frames["resolution_frame"]
    )
    UI_instance.add_dropdown(
        OUTPUT_SETTINGS, "output",
        0.5, 0.5, None, None, Anchor.CENTER.value, UI_instance.frames["output_format_frame"]
    )

    # Add sliders
    UI_instance.add_slider(
        0, 5, True, "black", UI_instance.bg_color, 0.5, 0.7, None, None, Anchor.CENTER.value, UI_instance.frames["preview_countdown_frame"]
    )

    # Add checkboxes
    UI_instance.add_checkbox(
        "test", "Arial", 50, "test_var", "black", UI_instance.bg_color,
        0.5, 0.5, 25, 25, Anchor.CENTER.value, None
    )

# Then let it run
finally:
    UI_instance.window.mainloop()