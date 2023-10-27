'''
Automatically level up through the BLOODWEB in DEAD BY DAYLIGHT.
Will not automatically prestige characters.

RUN THE SCRIPT:
 1. Install Python.
 2. Install pyautogui via command 'pip install pyautogui'.
 3. Run script via command: 'python bloodwebber.py'

MOVE MOUSE TO ANY SCREEN CORNER AT ANY TIME TO STOP.
'''

import ctypes
import sys
import time
import pyautogui as pag

def main():

    rings = {
        "center": (
            (680, 580)
        ),
        "inner": (
            (675, 460), (575, 520), (570, 645),
            (680, 690), (770, 630), (780, 520)
        ),
        "middle": (
            (615, 345), (500, 410), (440, 520),
            (435, 645), (510, 750), (620, 800),
            (740, 800), (855, 755), (910, 640),
            (920, 520), (855, 410), (740, 350)
        ),
        "outer": (
            (680, 220), (500, 270), (370, 400),
            (320, 580), (365, 760), (495, 900),
            (680, 945), (860, 895), (995, 760),
            (1045, 580), (985, 405), (860, 280)
        )
    }

    scale_factor = get_scale_factor()

    if sys.argv[-1] == 'position':
        get_position()
    elif sys.argv[-1] == 'first-prestige':
        autolevel_first_prestige(rings)
    else:
        autolevel(rings)

def get_position() -> None:
    '''Print location of mouse cursor.'''

    print(pag.position())

def autolevel_first_prestige(rings: tuple[tuple[tuple]]) -> None:
    '''Automatically level to the first prestige.'''

    i = 0
    while i <= 50:
        i += 1
        time.sleep(3)
        for ring in rings:
            for x, y in ring:
                click(x, y)

def autolevel(rings: tuple[tuple[tuple]]) -> None:
    '''Automatically prestige once, after prestige already reached.'''

    i = 0
    while i <= 50:
        i += 1
        time.sleep(5)
        x, y = rings['center']
        click(x, y)

def get_scale_factor() -> tuple:
    '''Get scaling factor between coded and current monitor resolutions.'''

    user32 = ctypes.windll.user32
    new_res = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    scale_factor = new_res[0] / 1920, \
                   new_res[1] / 1080

    return scale_factor

def scale(pair: tuple | list, scale_factor: tuple | list) -> tuple:
    '''Scale coordinate pair to current monitor size.'''

    scaled_pair = pair[0] * scale_factor[0], \
                  pair[1] * scale_factor[1]

    return scaled_pair

def click(moveToX: int, moveToY: int) -> None:
    '''Press and hold the left mouse button for one second.'''

    pag.moveTo(moveToX, moveToY, 0.2)
    time.sleep(0.1)
    pag.mouseDown()
    time.sleep(0.4)
    pag.mouseUp()

if __name__ == '__main__': main()
