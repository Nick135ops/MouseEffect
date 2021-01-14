try:
    from pynput.mouse import Listener
    import playsound
finally:
    import os
    os.system('python -3 -m pip install pynput')
    os.system('python -3 -m pip install playsound')
def on_click(x, y, button, pressed):
    if pressed:
        playsound.playsound('beep.wav')

with Listener(on_click=on_click) as listener:
    listener.join()
