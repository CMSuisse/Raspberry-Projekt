from enum import Enum

# Using tkinter's direction anchors would have been stupid
# This makes them more intuitive to work with (for me, at least)
class ANCHOR(Enum):
    TOPLEFT = "nw"
    TOP = "n"
    TOPRIGHT = "ne"
    RIGHT = "e"
    BOTTOMRIGHT = "se"
    BOTTOM = "s"
    BOTTOMLEFT = "sw"
    LEFT = "w"
    CENTER = "center"

# The possible resolution settings the user can select
RESOLUTION_SETTINGS = {
    "360p": [640, 360],
    "480p": [854, 480],
    "720p": [1280, 720],
    "1080p": [1920, 1080],
}

# The possible output options the user can select
OUTPUT_SETTINGS = (
    "jpeg",
    "png",
    "gif",
    "rgb",
    "rgba",
    "raw"
)

# The font I want to have for the UI's dropdowns
DROPDOWN_FONT = ("Arial", 18)