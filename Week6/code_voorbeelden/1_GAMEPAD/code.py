# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import analogio
import board
import digitalio
import usb_hid
from hid_gamepad import Gamepad

print("Hello World!")

gamepad = Gamepad(usb_hid.devices)

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
    digitalio.DigitalInOut(board.GP15),
    digitalio.DigitalInOut(board.GP6),
]

for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

# Koppel elke knop aan een gamepad-knopnummer (1 t/m 16).
button_numbers = [
    1,  # GP15
    2,  # GP6
]

# Analoge joystick. GP26 = A3, GP27 = A1
joystick_x = analogio.AnalogIn(board.A3)
joystick_y = analogio.AnalogIn(board.A1)


def range_map(x, in_min, in_max, out_min, out_max):
    """Werkt hetzelfde als de map()-functie van Arduino."""
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


# Houd bij welke knoppen op dit moment zijn ingedrukt.
# Alle knoppen bij het opstarten losgelaten (False)
buttons_pressed = [False, False]

print("Gamepad ready! Press buttons and move the joystick.")

while True:
    # Loop over elke knop
    for i in range(len(buttons)):
        button = buttons[i]
        button_number = button_numbers[i]

        if not button.value:  # Knop ingedrukt (verbonden met GND)
            if not buttons_pressed[i]:
                gamepad.press_buttons(button_number)
                buttons_pressed[i] = True
                print(" press. button:", i, "gamepad:", button_number, end="")
        else:  # Knop losgelaten
            if buttons_pressed[i]:
                gamepad.release_buttons(button_number)
                buttons_pressed[i] = False
                print(" release. button:", i, "gamepad:", button_number, end="")

    # Zet de analoge waarde van 0-65535 om naar een joystickwaarde van -127 tot 127.
    gamepad.move_joysticks(
        x=range_map(joystick_x.value, 0, 65535, -127, 127),
        y=range_map(joystick_y.value, 0, 65535, -127, 127),
    )
    print(" x", joystick_x.value, "y", joystick_y.value, end="")
