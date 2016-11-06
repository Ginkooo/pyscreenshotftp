from pynput.keyboard import Key
from pynput.keyboard import Listener
from pynput.keyboard import KeyCode
from pynput.mouse import Controller
from config import config
import screenshot

mouse = Controller()
key_already_pressed = False
trigger_key = config.get('key_trigger')
exit_key = config.get('exit_key')

def triggered():

    global key_already_pressed
    key_already_pressed = False

    mouse_pos_1 = []
    mouse_pos_2 = []

    def on_press(key):
        global key_already_pressed
        if key == exit_key:
            return False
        if key == trigger_key and not key_already_pressed:
            mouse_pos_1.append(mouse.position)
            key_already_pressed = True
    def on_release(key):
        if key == trigger_key:
            mouse_pos_2.append(mouse.position)
            raise StopIteration

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if not len(mouse_pos_1) or not len(mouse_pos_2):
        return []

    mouse_params = mouse_pos_1[0], mouse_pos_2[0]
    return mouse_params
