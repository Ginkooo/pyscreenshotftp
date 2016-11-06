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
keys = config.get('key_combination')

def triggered():

    mouse_pos_1 = []
    mouse_pos_2 = []

    pressed = [False for x in keys]

    def on_press(key):
        print('{key} pressed'.format(key = key))
        if key in keys:
            idx = keys.index(key)
            mouse_pos_1.append(mouse.position)
            pressed[idx] = True
        if key == Key.esc:
            return False


    def on_release(key):
        all_pressed = True
        for val in pressed:
            if not val:
                all_pressed = False
                mouse_pos_1.clear()
                mouse_pos_2.clear()
                for i in range(len(pressed)):
                    pressed[i] = False
        if all_pressed:
            mouse_pos_2.append(mouse.position)
            raise StopIteration

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

        if not len(mouse_pos_1) or not len(mouse_pos_2):
            return []

        mouse_params = mouse_pos_1[0], mouse_pos_2[0]
        return mouse_params
