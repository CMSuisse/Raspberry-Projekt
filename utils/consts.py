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
