import vibra
import display
import utime
import buttons

vibration_speed = 10
disp = display.open()

def init():
    vibration_speed = 10

def headline():
    # disp.print("Personal \n Massager", posy=0, fg=[0, 255, 255])
    # disp.print("Left=Lower", posy=-10, fg=[0, 255, 255])
    # stuff_in_string = f"Vibe Speed \n  {vibration_speed}."
    stuff_in_string = "Vibe Speed \n  {vibration_speed}."
    disp.print(stuff_in_string, posy=0, fg=[0, 255, 255])

def goSlower():
    if vibration_speed > 1:
        vibration_speed = vibration_speed - 1

def goFaster():
    vibration_speed = vibration_speed + 1


button_pressed = False
while True:
    disp.clear()
    headline()
    v = buttons.read(buttons.BOTTOM_LEFT | buttons.BOTTOM_RIGHT)
    if v == 0:
        button_pressed = False
    if not button_pressed and v & buttons.BOTTOM_LEFT != 0:
        button_pressed = True
        goSlower()
    if not button_pressed and v & buttons.BOTTOM_RIGHT != 0:
        button_pressed = True
        goFaster()


    vibra.vibrate(100)
    utime.sleep_ms(vibration_speed)
