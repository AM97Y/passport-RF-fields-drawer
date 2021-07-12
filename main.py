from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class TestFont:
    def __init__(self):
        pass

    def test(self):
        self.create_image()
        self.edit_image()

    @staticmethod
    def create_image():
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
    def edit_image():
        font = ImageFont.truetype("OCR B Regular.ttf", 14)
        with Image.open("test.png") as img:
            draw = ImageDraw.Draw(img)
            draw.text((0, 100), "УВД", fill=(0, 0, 0), font=font)
            # (100, 1) - координаты текста, fill - цвет текста
            ImageDraw.Draw(img)
            img.save("Edit_test.png")


class TextFont2Img:
    def __init__(self, font_name="OCR B Bold.ttf", size_font=18, size_image=(500, 250)):
        """
        font_name: Имя файла шрифта. Также подходит font_name = "OCR B Regular.ttf".
        size_font: Размер шрифта.
        size_image: Размер самого изображения.
        """
        self.font_name = font_name
        self.size_font = size_font
        self.size_image = size_image
        self.font = ImageFont.truetype(self.font_name, self.size_font)
        self.color_text = (0, 0, 0)

    def create_image(self, text="УВД России", height=0, weight=0, name_image="font.png"):
        """
        text: текст печати.
        height: высота раположения текста.
        weight: ширина раположения текста.
        name_image: имя картинки при сохранении (png).
        """
        
        img = Image.new("RGBA", self.size_image, (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        draw.text((weight, height), text, fill=self.color_text, font=self.font)
        ImageDraw.Draw(img)
        img.save(name_image)


if __name__ == '__main__':

    text = "УВД России по Яр обл"
    height = 100
    weight = 105
    name_image = "test_font_ocr.png"

    TextFont2Img().create_image(text, height, weight, name_image)
