from pynput.mouse import Listener
import playsound

def on_click(x, y, button, pressed):
    if pressed:
        playsound.playsound('beep.wav')

with Listener(on_click=on_click) as listener:
    listener.join()
