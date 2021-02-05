import pyautogui
from ctypes import windll, Structure, c_long, byref

# !! Deprecated !!
'''
class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def _query_mouse_position():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {'x': pt.x, 'y': pt.y}
'''


# Get mouse position
def query_mouse_position():
    x, y = pyautogui.position()
    return {'x': x, 'y': y}
