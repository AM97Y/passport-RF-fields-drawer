from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import unittest
import config


class TestFont(unittest.TestCase):

    @staticmethod
    def test_create_image():
        # font = ImageFont.truetype("Arial-Bold.ttf",14)
        font = ImageFont.truetype("fonts/OCR B Bold.ttf", 18)
        img = Image.new("RGBA", (500, 250), (255, 255, 255, 0))
        # (500, 250) - размер изображения, (255, 255, 255,) - цвет фона
        drawer = ImageDraw.Draw(img)
        drawer.text((100, 1), "России", fill=(0, 0, 0), font=font)
        # (100, 1) - координаты текста, fill - цвет текста
        ImageDraw.Draw(img)
        img.save("test.png")

    @staticmethod
    def test_edit_image():
        font = ImageFont.truetype("fonts/OCR B Regular.ttf", 18)
        with Image.open("test.png") as img:
            drawer = ImageDraw.Draw(img)
            drawer.text((0, 100), "России", fill=(0, 0, 0), font=font,
                        stroke_width=1,
                        stroke_fill=(0, 0, 0))
            # (100, 1) - координаты текста, fill - цвет текста
            ImageDraw.Draw(img)
            img.save("Edit_test.png")

    @staticmethod
    def test_fonts_image():
        ypix = 0
        img = Image.new("RGBA", (500, 250), (255, 255, 255, 0))
        with open(config.fronts, "r") as f:
            for line in f:
                font = ImageFont.truetype(line.strip(), 18)
                drawer = ImageDraw.Draw(img)
                drawer.text((0, ypix), "России", fill=(0, 0, 0), font=font)
                # (100, 1) - координаты текста, fill - цвет текста
                ImageDraw.Draw(img)
                ypix += 20
        img.save("test_fonts.png")

    def setUp(self):
        print(f'Test started')

    def tearDown(self):
        print(f'Test finished\n')


if __name__ == '__main__':
    unittest.main()
