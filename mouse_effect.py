try:
    import mouse
    import playsound
    import os
finally:
    os.system('python -3 -m pip install playsound')
    os.system('python -3 -m pip install mouse')

while True:
    if mouse.is_pressed():
        playsound.playsound('beep.wav')
