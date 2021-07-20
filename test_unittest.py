from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import unittest


class TestFont(unittest.TestCase):

    @staticmethod
    def test_create_image():
        # font = ImageFont.truetype("Arial-Bold.ttf",14)
        font = ImageFont.truetype("fronts/OCR B Bold.ttf", 18)
        img = Image.new("RGBA", (500, 250), (255, 255, 255, 0))
        # (500, 250) - размер изображения, (255, 255, 255,) - цвет фона
        drawer = ImageDraw.Draw(img)
        drawer.text((100, 1), "УВД", fill=(0, 0, 0), font=font)
        # (100, 1) - координаты текста, fill - цвет текста
        ImageDraw.Draw(img)
        img.save("test.png")

    @staticmethod
    def test_edit_image():
        font = ImageFont.truetype("fronts/OCR B Regular.ttf", 14)
        with Image.open("test.png") as img:
            drawer = ImageDraw.Draw(img)
            drawer.text((0, 100), "УВД", fill=(0, 0, 0), font=font)
            # (100, 1) - координаты текста, fill - цвет текста
            ImageDraw.Draw(img)
            img.save("Edit_test.png")

    def setUp(self):
        print(f'Test started')

    def tearDown(self):
        print(f'Test finished\n')


if __name__ == '__main__':
    unittest.main()
