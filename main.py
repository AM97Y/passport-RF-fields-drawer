import os
from argparse import ArgumentParser
from datetime import datetime

import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import config


class TextFont2Img:
    def __init__(self):
        """
        _fonts_list: List of fonts,
        _colors_list: List of text colors,
        _output_path: Folder to store generated images with text information
        """
        self._fonts_list = []
        self._init_fonts()

        self._colors_list = []
        self._init_colors()

        self._output_path = config.output_path
        if not os.path.exists(self._output_path):
            os.makedirs(self._output_path)

    def _init_fonts(self):
        """
        This function initializes the list of fonts.
        """
        with open(config.fonts, "r") as f:
            for line in f:
                self._fonts_list.append(line.strip())

    def _init_colors(self):
        """
        This function initializes the list of colors.
        """
        with open(config.colors, "r") as file_with_colors:
            for color in file_with_colors:
                r, g, b = color.strip().split(' ')
                self._colors_list.append((int(r), int(g), int(b)))

    def create_text_image(self, text=""):
        """
        text: Text to visualize on image.
        """
        size_font = np.random.randint(config.size_fonts_min, config.size_fonts_max)
        font_name = np.random.choice(self._fonts_list)
        color = self._colors_list[np.random.choice(len(self._colors_list))]
        font = ImageFont.truetype(font_name, size_font)

        img = Image.new("RGBA", config.size_image, config.color_img)
        drawer = ImageDraw.Draw(img)
        self._draw_text(text, drawer, font, color)
        ImageDraw.Draw(img)
        today = datetime.now()
        img.save(f'{config.output_path}/{today.strftime("%Y-%m-%d-%H.%M.%S.%f")}.png')

    @staticmethod
    def _draw_text(text, drawer, font, color):
        """
        drawer: ImageDraw
        font: random font
        color: random color
        """
        xpos = config.weight

        for letter in text:
            drawer.text((xpos, config.height), letter, fill=color, font=font,
                        stroke_width=config.stroke_width, stroke_fill=color)
            letter_width, letter_height = drawer.textsize(letter, font=font)
            xpos += letter_width - config.shift_letter


if __name__ == '__main__':
    generator = TextFont2Img()
    with open(config.text, "r") as f:
        for line in f:
            generator.create_text_image(line.strip())
