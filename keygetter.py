from pynput.keyboard import Key
from pynput.keyboard import Listener
from pynput.keyboard import KeyCode
from pynput.mouse import Controller
import screenshot

key_pressed = False
config_key = 'a'
key_already_pressed = False
mouse = Controller()

def triggered():
    mouse_pos_1 = []
    mouse_pos_2 = []

    def on_press(key):
#        print('{key} pressed'.format(key=key))
        global key_already_pressed
        if key == KeyCode.from_char('a') and not key_already_pressed:
            mouse_pos_1.append(mouse.position)
            key_already_pressed = True
    def on_release(key):
#        print('{key} released'.format(key=key))
        if key == Key.esc:
            return False
        if key == KeyCode.from_char('a'):
            mouse_pos_2.append(mouse.position)
            raise StopIteration

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    mouse_params = mouse_pos_1[0], mouse_pos_2[0]
    return mouse_params
