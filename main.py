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
        _output_path: Results folder.
        """
        self._fonts_list = []
        self._init_fronts()

        self._colors_list = []
        self._init_colors()

        self._output_path = config.output_path

    def _init_fronts(self):
        with open(config.fronts, "r") as f:
            for line in f:
                self._fonts_list.append(line.strip())

    def _init_colors(self):
        with open(config.colors, "r") as f:
            for line in f:
                color = line.strip().split(' ')
                self._colors_list.append((int(color[0]), int(color[1]), int(color[2])))

    def create_random_image(self, text=""):
        """
        text: Print text on picture.
        """
        size_font = np.random.randint(config.size_fronts_min, config.size_fronts_max)
        font_name = np.random.choice(self._fonts_list)
        color = self._colors_list[np.random.choice(len(self._colors_list))]
        font = ImageFont.truetype(font_name, size_font)

        img = Image.new("RGBA", config.size_image, config.color_img)
        drawer = ImageDraw.Draw(img)
        drawer.text((config.weight, config.height), text, fill=color, font=font,
                    stroke_width=config.stroke_width, stroke_fill=color)
        ImageDraw.Draw(img)
        self._makedirs(f'{config.output_path}/')

        today = datetime.datetime.today()
        img.save(f'{config.output_path}/{today.strftime("%Y-%m-%d-%H.%M.%S")}.png')

    @staticmethod
    def _makedirs(path):
        if not os.path.exists(path):
            os.makedirs(path)


if __name__ == '__main__':
    generator = TextFont2Img()
    with open(config.text, "r") as f:
        for line in f:
            generator.create_random_image(line.strip())
