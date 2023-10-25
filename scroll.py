# SPDX-FileCopyrightText: 2019 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
from digitalio import DigitalInOut
import adafruit_requests as requests
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi

import os
import time
# import ssl
# import wifi
import board
import terminalio
# import socketpool
from adafruit_matrixportal.matrixportal import MatrixPortal

SCROLL_DELAY = 0.03
time_interval = 5

text_color = 0xFC6900  # e.g., Retro Orange

matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=True)

matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(0, (matrixportal.graphics.display.height // 2) - 1),
    scrolling=True,
)

NYT_header_text_area = matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(0, (matrixportal.graphics.display.height // 6) - 1),
)

matrixportal.set_text("OSHMKUFA", NYT_header_text_area)
while True:
    titles = ['Gelbana', 'IBN5100', 'Divergence', 'Gunvarrel', 'Dr. P', 'CRT']

    for title in titles:
        matrixportal.set_text(title)
        matrixportal.set_text_color(text_color)
        matrixportal.scroll_text(SCROLL_DELAY)

    time.sleep(time_interval)