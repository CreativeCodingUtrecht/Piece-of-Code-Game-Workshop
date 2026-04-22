# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

print("Hello World!")

kbd = Keyboard(usb_hid.devices)

# Pins voor 4 knoppen.
button_pins = (board.GP0, board.GP1, board.GP2, board.GP10)

# Koppel de knoppen aan pijltjestoetsen.
# Dit kun je aanpassen naar andere toetsen als je wilt.
button_keys = (
    Keycode.RIGHT_ARROW,    # GP0
    Keycode.UP_ARROW,  # GP1
    Keycode.DOWN_ARROW,  # GP2
    Keycode.LEFT_ARROW, # GP10
)

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

# Houd bij welke toetsen op dit moment zijn ingedrukt,
# zodat indrukken en loslaten goed werken.
keys_pressed = [False] * len(buttons)

print("Keyboard ready! Press buttons for arrow keys.")

while True:
    # Controleer elke knop.
    for i, button in enumerate(buttons):
        key = button_keys[i]
        
        if not button.value:  # Knop ingedrukt (verbonden met GND)
            if not keys_pressed[i]:
                # De toets is net ingedrukt.
                kbd.press(key)
                keys_pressed[i] = True
                print(" press. Key:", key, ", pin:", button_pins[i], end="")
        else:  # Knop losgelaten
            if keys_pressed[i]:
                # De toets is net losgelaten.
                kbd.release(key)
                keys_pressed[i] = False
                print(" release. Key:", key, ", pin:", button_pins[i], end="")

    # Hier kun je eventueel een kleine vertraging toevoegen tegen contactdender.
    # Laat dit weg als je een snellere reactie wilt.