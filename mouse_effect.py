import mouse
import playsound

while True:
    if mouse.is_pressed():
        playsound.playsound('beep.wav')
