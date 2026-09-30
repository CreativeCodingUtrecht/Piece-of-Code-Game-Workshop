# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import digitalio
from digitalio import DigitalInOut
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

print("Hello World!")

keyboard = Keyboard(usb_hid.devices)

# Pas de pinnen aan op basis van jouw bedrading.
#
#             GP0 GP1 GP2 GP3 etc.
#              *   *   *   *
#              0   1   2   3   4   5   6   7   8
#             +--------------------------------+  8
#             |                                |  9
#          U--|                                | 10
#          S--|          RP2040-Zero           | 11
#          B--|                                | 12
#             |                                | 13
#             +--------------------------------+ 14
#              5V GND  3V3  29  28  27  26  15  14
#
buttons = [
    # pin,                                  key,               pressed?
    [ DigitalInOut(board.GP0),      Keycode.RIGHT_ARROW,        False ],
    [ DigitalInOut(board.GP1),      Keycode.UP_ARROW,           False ],
    [ DigitalInOut(board.GP2),      Keycode.DOWN_ARROW,         False ],
    [ DigitalInOut(board.GP3),      Keycode.LEFT_ARROW,         False ],
]

# De pinnen voor de knoppen zijn input
# Voor knoppen gebruikt je daarbij een pull-up weerstand: https://en.wikipedia.org/wiki/Pull-up_resistor
for pin, key, pressed in buttons:
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP

print("Keyboard ready! Press buttons for arrow keys.")

while True:
    # Loop over elke knop
    for i in range(len(buttons)):
        pin, key, pressed = buttons[i]

        if not pin.value:  # Knop ingedrukt (verbonden met GND)
            if not pressed:
                # De toets is net ingedrukt. pressed: False -> True
                keyboard.press(key)
                pressed = True
                print(" press. button:", i, "key:", key, end="")
        else:  # Knop losgelaten
            if pressed:
                # De toets is net losgelaten. pressed: True -> False
                keyboard.release(key)
                pressed = False
                print(" release. button:", i, "key:", key, end="")


