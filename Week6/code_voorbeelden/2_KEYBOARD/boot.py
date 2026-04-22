import usb_hid

# Enable default HID devices (includes Keyboard)
usb_hid.enable(
    (usb_hid.Device.KEYBOARD,)
)