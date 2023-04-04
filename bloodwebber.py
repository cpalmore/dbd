'''
Automatically level up through the BLOODWEB in DEAD BY DAYLIGHT.
Will not automatically prestige characters.

IF YOUR SCREEN RESOLUTION IS NOT 1920x1080:
 1. For each position that needs to be clicked:
    a. Move your mouse to the position to be clicked.
    b. Run the command: 'python bloodwebber.py position'.
    c. See printed coordinates.
 2. Using the printed positions, update the RINGS() function.

RUN THE SCRIPT:
 1. Install Python.
 2. Install pyautogui via command 'pip install pyautogui'.
 3. Run script via command: 'python bloodwebber.py'

MOVE MOUSE TO ANY SCREEN CORNER AT ANY TIME TO STOP.
'''

def RINGS() -> tuple:
    '''Manually define positions to click on screen.'''

    center = (
        (680, 580)
    )

    inner = (
        (675, 460),
        (575, 520),
        (570, 645),
        (680, 690),
        (770, 630),
        (780, 520)
    )

    middle = (
        (615, 345),
        (500, 410),
        (440, 520),
        (435, 645),
        (510, 750),
        (620, 800),
        (740, 800),
        (855, 755),
        (910, 640),
        (920, 520),
        (855, 410),
        (740, 350)
    )

    outer = (
        (680, 220),
        (500, 270),
        (370, 400),
        (320, 580),
        (365, 760),
        (495, 900),
        (680, 945),
        (860, 895),
        (995, 760),
        (1045, 580),
        (985, 405),
        (860, 280)
    )

    return (inner, middle, outer)

import sys
import time
import pyautogui as pag

def main():
    if sys.argv[-1] == 'position':
        get_position()
    else:
        autolevel(RINGS())

def get_position() -> None:
    '''Print location of mouse cursor.'''

    print(pag.position())

def autolevel(rings: tuple[tuple[tuple]]) -> None:
    '''Run the auto-leveling process.'''

    i = 0
    while i <= 50:
        i += 1
        time.sleep(3)

        for ring in rings:
            for x, y in ring:
                click(x, y)

def click(moveToX: int, moveToY: int) -> None:
    '''Press and hold the left mouse button for one second.'''

    pag.moveTo(moveToX, moveToY, 0.2)
    time.sleep(0.1)
    pag.mouseDown()
    time.sleep(1)
    pag.mouseUp()

if __name__ == '__main__': main()