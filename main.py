import os
from argparse import ArgumentParser
from datetime import datetime
import json

import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class TextFont2Img:
    def __init__(self, config_file: str):
        """
        _config: Config params,
        _fonts_list: List of fonts,
        _colors_list: List of text colors,
        _output_path: Folder to store generated images with text information
        """

        with open(config_file) as f:
            self._config = json.load(f)

        self.output_path = self._config['output_path']

        self._fonts_list = []
        self._init_fonts()

        self._colors_list = []
        self._init_colors()

        self._output_path = self._config['output_path']
        if not os.path.exists(self._output_path):
            os.makedirs(self._output_path)

    def _init_fonts(self) -> None:
        """
        This function initializes the list of fonts.
        """
        with open(self._config['fonts_file'], "r") as f:
            for line in f:
                self._fonts_list.append(line.strip())

    def _init_colors(self) -> None:
        """
        This function initializes the list of colors.
        """
        with open(self._config['colors_file'], "r") as file_with_colors:
            for color in file_with_colors:
                r, g, b = color.strip().split(' ')
                self._colors_list.append((int(r), int(g), int(b)))

    def create_text_images(self) -> None:
        """
        This function creates images for each line of text with a random font and color.
        """
        with open(self._config['text_file'], "r") as f:
            for line in f:
                text = line.strip()

                size_font = np.random.randint(
                    self._config["fonts_param"]['size_fonts_min'],
                    self._config["fonts_param"]['size_fonts_max'])
                font_name = np.random.choice(self._fonts_list)
                font = ImageFont.truetype(font_name, size_font)

                color = self._colors_list[np.random.choice(
                    len(self._colors_list))]

                img = Image.new(
                    "RGBA", tuple(
                        self._config["img_params"]['size_image']), tuple(
                        self._config["img_params"]['color_img']))
                drawer = ImageDraw.Draw(img)
                self._draw_text(text, drawer, font, color)
                ImageDraw.Draw(img)

                today = datetime.now()

                img.save(
                    f'{self.output_path}/{today.strftime("%Y-%m-%d-%H.%M.%S.%f")}.png')

    def _draw_text(self, text: str, drawer, font, color) -> None:
        """
        This function draws text letter by letter.
        drawer: ImageDraw
        font: random font
        color: random color
        """
        xpos = self._config["img_params"]['weight']

        for letter in text:
            drawer.text(
                (xpos,
                 self._config["img_params"]['height']),
                letter,
                fill=color,
                font=font,
                stroke_width=self._config["fonts_param"]['stroke_width'],
                stroke_fill=color)
            letter_width, letter_height = drawer.textsize(letter, font=font)
            xpos += letter_width - self._config["fonts_param"]['shift_letter']


def init_argparse() -> None:
    """
    Initializes argparse.
    Returns parser.
    """
    parser = ArgumentParser(
        description='This project randomly generates images with the transparent '
        'background from the proposed test, color and fonts generates images. '
        'It is used as a top layer for generating of passports. ')
    parser.add_argument(
        '--config_file',
        nargs='?',
        help='Path to config file.',
        default='configs/default.json',
        type=str)

    parser.add_argument(
        '--output_path',
        nargs='?',
        help='path to save files',
        default='output_path/',
        type=str)
    return parser


if __name__ == '__main__':
    args = init_argparse().parse_args()
    generator = TextFont2Img(args.config_file)
    generator.create_text_images()
