# Screen resolution 800x480
from utils import ui_handler
from utils import api_handler
from utils.consts import Anchor, RESOLUTION_SETTINGS, OUTPUT_SETTINGS, DROPDOWN_FONT

def setup_window(API_instance):
    # Set up the UI
    UI_instance = ui_handler.UI_Handler([800, 480], True, "#B0B0B0", DROPDOWN_FONT)

    # Add all frames
    UI_instance.add_frame(
        "resolution_frame", True,
        0.01, 0.2, 380, 150, Anchor.TOPLEFT.value
    )
    UI_instance.add_frame(
        "output_format_frame", True,
        0.99, 0.2, 380, 150, Anchor.TOPRIGHT.value
    )
    UI_instance.add_frame(
        "preview_countdown_frame", True,
        0.8, 0.98, 275, 125, Anchor.BOTTOM.value
    )

    # Add all labels
    UI_instance.add_label(
        "RaspberryPhoto v.1", "Arial", 25, "white", "black",
        0.5, 0.1, 800, None, Anchor.TOP.value
    )
    UI_instance.add_label(
        "Enter your preferred resolution setting:", "Arial", 15, "black", UI_instance.bg_color,
        0.5, 0.1, None, None, Anchor.TOP.value, UI_instance.frames["resolution_frame"]
    )
    UI_instance.add_label(
        "Enter your preferred output format", "Arial", 15, "black", UI_instance.bg_color,
        0.5, 0.1, None, None, Anchor.TOP.value, UI_instance.frames["output_format_frame"]
    )
    UI_instance.add_label(
        "Preview length", "Arial", 15, "black", UI_instance.bg_color,
        0.5, 0.1, None, None, Anchor.TOP.value, UI_instance.frames["preview_countdown_frame"]
    )

    # Add all buttons
    # This button calls the capture image which requires params, which is why a lambda was used
    UI_instance.add_button(
        "CAPTURE", "Arial", 25, "white", "black",
        0.5, 0.9, None, None, Anchor.CENTER.value,
        callback_function=lambda e: UI_instance.capture_image(API_instance)
    )

    # Add all dropdowns
    UI_instance.add_dropdown(
        list(RESOLUTION_SETTINGS.keys()), 0, "resolution", DROPDOWN_FONT,
        0.5, 0.5, None, None, Anchor.CENTER.value, UI_instance.frames["resolution_frame"]
    )
    UI_instance.add_dropdown(
        OUTPUT_SETTINGS, 0, "output", DROPDOWN_FONT,
        0.5, 0.5, None, None, Anchor.CENTER.value, UI_instance.frames["output_format_frame"]
    )

    # Add sliders
    UI_instance.add_slider(
        "preview_length", 0, 10, True, "black", UI_instance.bg_color, ["Arial", 15],
        0.5, 0.65, 250, 30, Anchor.CENTER.value, UI_instance.frames["preview_countdown_frame"]
    )

    # Add checkboxes
    UI_instance.add_checkbox(
        "Bild auf Flickr hochladen", "Arial", 18, "upload_image", "black", UI_instance.bg_color,
        0.5, 0.6, None, None, Anchor.CENTER.value
    )

    print("UI loading complete")
    UI_instance.window.mainloop()

def main():
    try:
        # Establish connection with the Flickr API
        API_instance = api_handler.API_Handler()
        print("Write token present: {}".format(API_instance.token_valid(perms="write")))

        setup_window(API_instance)
    except Exception as e:
        print("Something went wrong wrong. Maybe just try again?")
        print(e)
    finally:
        print("Goodbye")

if __name__ == "__main__":
    main()