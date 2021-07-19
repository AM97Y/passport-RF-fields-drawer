from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import unittest


class TestFont:

    @staticmethod
    def test_create_image():
        # font = ImageFont.truetype("Arial-Bold.ttf",14)
        font = ImageFont.truetype("OCR B Bold.ttf", 18)
        img = Image.new("RGBA", (500, 250), (255, 255, 255, 0))
        # (500, 250) - размер изображения, (255, 255, 255,) - цвет фона
        draw = ImageDraw.Draw(img)
        draw.text((100, 1), "УВД", fill=(0, 0, 0), font=font)
        # (100, 1) - координаты текста, fill - цвет текста
        ImageDraw.Draw(img)
        img.save("test.png")

    @staticmethod
    def test_edit_image():
        font = ImageFont.truetype("fronts/OCR B Regular.ttf", 14)
        with Image.open("test.png") as img:
            draw = ImageDraw.Draw(img)
            draw.text((0, 100), "УВД", fill=(0, 0, 0), font=font)
            # (100, 1) - координаты текста, fill - цвет текста
            ImageDraw.Draw(img)
            img.save("Edit_test.png")


    def setUp(self):
        TestFont.count += 1
        print(f'Test {TestFont.count} started')

    def tearDown(self):
        print(f'Test {TestFont.count} finished\n')


if __name__ == '__main__':
    unittest.main()
