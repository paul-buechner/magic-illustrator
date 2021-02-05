import numpy as np
import cv2
import time
import threading
import pyautogui

from src.direct_keys import query_mouse_position
from src.image_search import scan
from PIL import ImageGrab
from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Button, Controller


# Declare image which should be drawn and corresponding trigger
path = "assets/images/ez_clap.png"
start_stop_key_d = KeyCode(char='d')
# Specify custom image dimensions or use default, uncomment which you want to use
# image_dimensions = (300, 200)
image_dimensions = cv2.imread(path).shape

# Trigger to fill the screen
start_stop_key_c = KeyCode(char='c')

# EXIT key, interrupts everything and closes the thread
exit_key = KeyCode(char='e')

# Pyautogui config
pyautogui.PAUSE = 0

mouse = Controller()
button = Button.left
delay = 0.0001


class ClickMouse(threading.Thread):
    def __init__(self, delay, button, path, image_dimensions):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.path = path
        self.image_dimensions = image_dimensions
        self.running = False
        self.program_running = True

    def start_clicking(self):
        global pressed_key

        if pressed_key == KeyCode(char='c'):
            self.screen_cnt, self.screen_cords = scan(
                np.array(ImageGrab.grab(bbox=None)))
        self.running = True

    def stop_clicking(self):
        self.running = False

    def clear_screen(self):
        for x in range(self.screen_cnt[0, 0, 0], self.screen_cnt[3, 0, 0], 8):
            for y in range((self.screen_cnt[0, 0, 1]),
                           (self.screen_cnt[2, 0, 1] - 6),
                           (abs(self.screen_cnt[0, 0, 1] - self.screen_cnt[2, 0, 1])) - 7):
                pyautogui.dragTo(x, y, button='left')
                time.sleep(0.001)
            # Check if interrupt
            if self.running == False:
                return
        return

    def draw_image(self):
        image = cv2.imread(self.path)
        image = cv2.resize(
            image, (self.image_dimensions[0], self.image_dimensions[1]))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.mouse_position = query_mouse_position()
        # Draw image
        for y in range(len(image)):
            for x in range(len(image[y])):
                if image[y][x] < 180:  # Pixel color threshold
                    actual_x = self.mouse_position['x'] + x
                    actual_y = self.mouse_position['y'] + y
                    pyautogui.moveTo(actual_x, actual_y)
                    mouse.click(self.button)
                    time.sleep(0.001)
            # Check if interrupt
            if self.running == False:
                return
        return

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                global pressed_key
                # Fill everything
                if pressed_key == KeyCode(char='c'):
                    self.clear_screen()
                    self.stop_clicking()

                # Draw selected image
                elif pressed_key == KeyCode(char='d'):
                    self.draw_image()
                    self.stop_clicking()


def initialize():
    global click_thread, listener
    # Start click_thread thread
    click_thread = ClickMouse(delay, button, path, image_dimensions)
    click_thread.start()

    # Start listener thread
    with Listener(on_press=on_press) as listener:
        listener.join()


def on_press(key):
    global pressed_key
    pressed_key = key
    # Start & Stop Thread
    if (key == start_stop_key_c) or (key == start_stop_key_d):
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()

    # EXIT
    if key == exit_key:
        click_thread.stop_clicking()
        click_thread.exit()
        listener.stop()
