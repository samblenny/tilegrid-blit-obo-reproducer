# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: Copyright 2024 Sam Blenny
#
# Hardware & CircuitPython version:
#  Adafruit CircuitPython 9.1.3 on 2024-08-29; Adafruit Feather ESP32-S3 TFT with ESP32S3
# Packages (adafruit_imageload and adafruit_st7789) came from:
#  https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20240827/adafruit-circuitpython-bundle-9.x-mpy-20240827.zip
from board import SPI, TFT_CS, TFT_DC
from displayio import (Bitmap, Group, Palette, TileGrid, release_displays)
from fourwire import FourWire
import adafruit_imageload
from adafruit_st7789 import ST7789

# Initialize ST7789 display
release_displays()
bus = FourWire(SPI(), command=TFT_DC, chip_select=TFT_CS)
display = ST7789(bus, rotation=270, width=240, height=135, rowstart=40,
    colstart=53, auto_refresh=False)

# The point of this next part to set up a side by side comparison
# of TileGrid sprite blitting for a from-scratch bitmap, an
# adafruit_imageload BMP bitmap, and an adafruit_imageload PNG
# bitmap...

# Make spritesheet of 2 vertically stacked 8x8 px sprites from scratch
(wide, high) = (8, 8)
(bitmap1, palette1) = (Bitmap(wide, 2*high, 4), Palette(4))
palette1[0] = 0x000000  # black
palette1[1] = 0xFF0000  # red
palette1[2] = 0x0000FF  # blue
for y in range(high):
    for x in range(wide):
        # Top sprite is solid blue rectangle
        bitmap1[x, y] = 2
        # Bottom sprite has red stripes on black background
        bitmap1[x, y+high] = 1 if ((x + y) % 3 == 0) else 0
tg1a = TileGrid(bitmap1, pixel_shader=palette1, width=1, height=1,
    tile_width=8, tile_height=8, x=5, y=8, default_tile=0)
tg1b = TileGrid(bitmap1, pixel_shader=palette1, width=1, height=1,
    tile_width=8, tile_height=8, x=15, y=8, default_tile=1)

# Load what should be the same spritesheet from a PNG
(bitmap2, palette2) = adafruit_imageload.load("sprites.png", bitmap=Bitmap,
    palette=Palette)
tg2a = TileGrid(bitmap2, pixel_shader=palette2, width=1, height=1,
    tile_width=8, tile_height=8, x=30, y=8, default_tile=0)
tg2b = TileGrid(bitmap2, pixel_shader=palette2, width=1, height=1,
    tile_width=8, tile_height=8, x=40, y=8, default_tile=1)

# Load what should be the same spritesheet from a BMP
(bitmap3, palette3) = adafruit_imageload.load("sprites.bmp", bitmap=Bitmap,
    palette=Palette)
tg3a = TileGrid(bitmap3, pixel_shader=palette3, width=1, height=1,
    tile_width=8, tile_height=8, x=55, y=8, default_tile=0)
tg3b = TileGrid(bitmap3, pixel_shader=palette3, width=1, height=1,
    tile_width=8, tile_height=8, x=65, y=8, default_tile=1)

# Add all the TileGrid objects to the root group
grp = Group(scale=3)
for tg in [tg1a, tg1b, tg2a, tg2b, tg3a, tg3b]:
    grp.append(tg)
display.root_group = grp
display.refresh()

while True:
    pass
