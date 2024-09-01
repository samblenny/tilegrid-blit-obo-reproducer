<!-- SPDX-License-Identifier: MIT -->
<!-- SPDX-FileCopyrightText: Copyright 2024 Sam Blenny -->
# TileGrid Blit Off by One Reproducer

This reproduces a blit glitch with displayio.TileGrid using sprites.


## Board and CircuitPython Version

- Adafruit ESP32-S3 TFT Feather - 4MB Flash, 2MB PSRAM
  ([product page](https://www.adafruit.com/product/5483))

```
Adafruit CircuitPython 9.1.3 on 2024-08-29; Adafruit Feather ESP32-S3 TFT with ESP32S3
```

## Library Versions

Library packages (adafruit_imageload and adafruit_st7789) came from:
https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20240827/adafruit-circuitpython-bundle-9.x-mpy-20240827.zip
