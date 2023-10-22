from enum import Enum

# The tkinter argument anchor to set the position only takes a select amount of inputs
class Anchor(Enum):
    TOPLEFT = "nw"
    TOP = "n"
    TOPRIGHT = "ne"
    RIGHT = "e"
    BOTTOMRIGHT = "se"
    BOTTOM = "s"
    BOTTOMLEFT = "sw"
    LEFT = "w"
    CENTER = "center"

RESOLUTION_SETTINGS = {
    "360p": [480, 360],
    "480p": [720, 480],
    "720p": [1280, 720],
    "1080p": [1920, 1080],
}

OUTPUT_SETTINGS = (
    "jpeg",
    "png",
    "gif",
    "rgb",
    "rgba",
    "raw"
)