# Keycode-overzicht

**Printversie voor in de les:** [KEYCODES-print.md](./KEYCODES-print.md)

Gebruik deze namen in je code, bijvoorbeeld in `pin_button_map` in [2_KEYBOARD/code.py](./code_voorbeelden/2_KEYBOARD/code.py):

```python
from adafruit_hid.keycode import Keycode

pin_button_map = [
    Keycode.RIGHT_ARROW,
    Keycode.UP_ARROW,
    Keycode.SPACE,
    Keycode.ENTER,
]
```

Volledige documentatie: [Adafruit HID Keycode](https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit_hid.keycode.Keycode)

## Letters

| Code | Toets | Code | Toets | Code | Toets | Code | Toets |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Keycode.A` | A | `Keycode.B` | B | `Keycode.C` | C | `Keycode.D` | D |
| `Keycode.E` | E | `Keycode.F` | F | `Keycode.G` | G | `Keycode.H` | H |
| `Keycode.I` | I | `Keycode.J` | J | `Keycode.K` | K | `Keycode.L` | L |
| `Keycode.M` | M | `Keycode.N` | N | `Keycode.O` | O | `Keycode.P` | P |
| `Keycode.Q` | Q | `Keycode.R` | R | `Keycode.S` | S | `Keycode.T` | T |
| `Keycode.U` | U | `Keycode.V` | V | `Keycode.W` | W | `Keycode.X` | X |
| `Keycode.Y` | Y | `Keycode.Z` | Z | | | | |

## Cijfers

| Code | Toets | Code | Toets | Code | Toets | Code | Toets | Code | Toets |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Keycode.ZERO` | 0 | `Keycode.ONE` | 1 | `Keycode.TWO` | 2 | `Keycode.THREE` | 3 | `Keycode.FOUR` | 4 |
| `Keycode.FIVE` | 5 | `Keycode.SIX` | 6 | `Keycode.SEVEN` | 7 | `Keycode.EIGHT` | 8 | `Keycode.NINE` | 9 |

## Pijltjes en navigatie

| Code | Toets |
| --- | --- |
| `Keycode.UP_ARROW` | Pijl omhoog |
| `Keycode.DOWN_ARROW` | Pijl omlaag |
| `Keycode.LEFT_ARROW` | Pijl links |
| `Keycode.RIGHT_ARROW` | Pijl rechts |
| `Keycode.HOME` | Home |
| `Keycode.END` | End |
| `Keycode.PAGE_UP` | Page Up |
| `Keycode.PAGE_DOWN` | Page Down |
| `Keycode.INSERT` | Insert |
| `Keycode.DELETE` | Delete (vooruit) |

## Veelgebruikte toetsen

| Code | Toets |
| --- | --- |
| `Keycode.ENTER` | Enter |
| `Keycode.ESCAPE` | Escape |
| `Keycode.TAB` | Tab |
| `Keycode.SPACEBAR` | Spatiebalk |
| `Keycode.BACKSPACE` | Backspace |
| `Keycode.CAPS_LOCK` | Caps Lock |
| `Keycode.PRINT_SCREEN` | Print Screen |
| `Keycode.SCROLL_LOCK` | Scroll Lock |
| `Keycode.PAUSE` | Pause |
| `Keycode.APPLICATION` | Menu-toets |

## Modifier-toetsen (Shift, Ctrl, Alt, …)

| Code | Toets |
| --- | --- |
| `Keycode.SHIFT` | Shift (links) |
| `Keycode.CONTROL` | Ctrl (links) |
| `Keycode.ALT` | Alt / Option (links) |
| `Keycode.GUI` | Windows / Command (links) |
| `Keycode.RIGHT_SHIFT` | Shift (rechts) |
| `Keycode.RIGHT_CONTROL` | Ctrl (rechts) |
| `Keycode.RIGHT_ALT` | Alt (rechts) |
| `Keycode.RIGHT_GUI` | Windows / Command (rechts) |

## Tekens

| Code | Tekens |
| --- | --- |
| `Keycode.MINUS` | `-` `_` |
| `Keycode.EQUALS` | `=` `+` |
| `Keycode.LEFT_BRACKET` | `[` `{` |
| `Keycode.RIGHT_BRACKET` | `]` `}` |
| `Keycode.BACKSLASH` | `\` `\|` |
| `Keycode.SEMICOLON` | `;` `:` |
| `Keycode.QUOTE` | `'` `"` |
| `Keycode.GRAVE_ACCENT` | `` ` `` `~` |
| `Keycode.COMMA` | `,` `<` |
| `Keycode.PERIOD` | `.` `>` |
| `Keycode.FORWARD_SLASH` | `/` `?` |

## Functietoetsen

| Code | Toets | Code | Toets | Code | Toets | Code | Toets |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Keycode.F1` | F1 | `Keycode.F2` | F2 | `Keycode.F3` | F3 | `Keycode.F4` | F4 |
| `Keycode.F5` | F5 | `Keycode.F6` | F6 | `Keycode.F7` | F7 | `Keycode.F8` | F8 |
| `Keycode.F9` | F9 | `Keycode.F10` | F10 | `Keycode.F11` | F11 | `Keycode.F12` | F12 |

## Combinaties met Shift of Ctrl

Gebruik meerdere keycodes tegelijk met `kbd.press()`:

```python
# Hoofdletter A
kbd.press(Keycode.SHIFT, Keycode.A)

# Ctrl + C
kbd.press(Keycode.CONTROL, Keycode.C)
```

Vergeet niet `kbd.release(...)` te gebruiken wanneer de toets weer los moet.
