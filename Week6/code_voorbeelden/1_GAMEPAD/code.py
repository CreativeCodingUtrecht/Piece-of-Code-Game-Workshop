# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import analogio
import board
import digitalio
import usb_hid
from hid_gamepad import Gamepad

print("Hello World!")

gp = Gamepad(usb_hid.devices)

# Pins voor de knoppen. Pas dit aan op basis van jouw bedrading.
button_pins = (board.GP15,board.GP6 )

# Koppel de knoppen aan de knopnummers van de gamepad.
gamepad_buttons = (1, 2)

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

# Analoge joystick op GP26 (ADC0) en GP27 (ADC1).
ax = analogio.AnalogIn(board.A3)
ay = analogio.AnalogIn(board.A1)


def range_map(x, in_min, in_max, out_min, out_max):
    """Werkt hetzelfde als de map()-functie van Arduino."""
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


while True:
    # Een knop is ingedrukt als deze naar GND getrokken wordt (.value = False).
    for i, button in enumerate(buttons):
        gamepad_button_num = gamepad_buttons[i]
        if button.value:
            gp.release_buttons(gamepad_button_num)
            print(" release", gamepad_button_num, end="")
        else:
            gp.press_buttons(gamepad_button_num)
            print(" press", gamepad_button_num, end="")

    # Zet de analoge waarde van 0-65535 om naar een joystickwaarde van -127 tot 127.
    gp.move_joysticks(
        x=range_map(ax.value, 0, 65535, -127, 127),
        y=range_map(ay.value, 0, 65535, -127, 127),
    )
    print(" x", ax.value, "y", ay.value)