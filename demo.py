#!/usr/bin/python3
import os
import sys
import time

from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
LIB_DIR = os.path.join(BASE_DIR, "lib")
FONT_DIR = os.path.join(BASE_DIR, "fnt")

if os.path.exists(LIB_DIR):
    sys.path.append(LIB_DIR)

from waveshare_epd import epd10in85

FONT_PATH = os.path.join(FONT_DIR, "Aldrich-Regular.ttc")


def main():
    epd = epd10in85.EPD()

    print("init")
    epd.init()
    print("clear")
    epd.Clear()
    time.sleep(1)

    image = Image.new("1", (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(image)

    big = ImageFont.truetype(FONT_PATH, 96)
    small = ImageFont.truetype(FONT_PATH, 36)

    draw.rectangle((10, 10, epd.width - 10, epd.height - 10), outline=0, width=4)
    draw.text((60, 120), "HELLO E-PAPER", font=big, fill=0)
    draw.text((60, 260), f"{epd.width} x {epd.height}", font=small, fill=0)
    draw.text((60, 320), time.strftime("%Y-%m-%d %H:%M:%S"), font=small, fill=0)

    for i, x in enumerate(range(60, 60 + 8 * 40, 40)):
        fill = 0 if i % 2 == 0 else 255
        draw.rectangle((x, 400, x + 30, 440), outline=0, width=2, fill=fill)

    print("display")
    epd.display(epd.getbuffer(image))
    time.sleep(3)

    print("sleep")
    epd10in85.epdconfig.module_exit(cleanup=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        epd10in85.epdconfig.module_exit(cleanup=True)
