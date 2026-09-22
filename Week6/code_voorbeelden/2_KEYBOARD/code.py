# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

print("Hello World!")

keyboard = Keyboard(usb_hid.devices)

# Pas de pinnen aan op basis van jouw bedrading.
#
# RP2040-Zero pinout: 
#
#             GP0 GP1 GP2 GP3 etc.
#              *   *   *   *
#              0   1   2   3   4   5   6   7   8
#             +--------------------------------+  8
#             |                                |  9
#          U--|          RP2040-Zero           | 10
#          S--|                                | 11
#          B--|                                | 12
#             |                                | 13
#             +--------------------------------+ 14
#              5V GND  3V3  29  28  27  26  15  14
#
buttons = [
    digitalio.DigitalInOut(board.GP0),
    digitalio.DigitalInOut(board.GP1),
    digitalio.DigitalInOut(board.GP2),
    digitalio.DigitalInOut(board.GP3),
]

for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP


# Zie KEYCODES.md voor de lijst met beschikbare toetsen
keys = [
    Keycode.RIGHT_ARROW,
    Keycode.UP_ARROW,
    Keycode.DOWN_ARROW,
    Keycode.LEFT_ARROW,
]

# Houd bij welke toetsen op dit moment zijn ingedrukt.
# Alle toetsen bij het opstarten losgelaten (False)
keys_pressed = [False, False, False, False]



print("Keyboard ready! Press buttons for arrow keys.")

while True:
    # Loop over elke knop
    for i in range(len(buttons)):
        button = buttons[i]
        key = keys[i]

        if not button.value:  # Knop ingedrukt (verbonden met GND)
            if not keys_pressed[i]:
                # De toets is net ingedrukt.
                keyboard.press(key)
                keys_pressed[i] = True
                print(" press. button:", i, "key:", key, end="")
        else:  # Knop losgelaten
            if keys_pressed[i]:
                # De toets is net losgelaten.
                keyboard.release(key)
                keys_pressed[i] = False
                print(" release. button:", i, "key:", key, end="")


