from PIL import Image, ImageFilter, ImageDraw

class Filter:

    def filter_blur(self, poto):
        self.img = Image.open(poto)
        self.blurred = self.img.filter(ImageFilter.BLUR)
        self.blurred.save("filtred2.jpg", "JPEG")

    def filter_contour(self, poto):
        self.img = Image.open(poto)
        self.contour = self.img.filter(ImageFilter.CONTOUR)
        self.contour.save('filtred3.jpg', "JPEG")

    def filter_negative(self,poto):
        self.img = Image.open(poto)
        self.draw = ImageDraw.Draw(self.img)  # Создаем инструмент для рисования.
        self.width = self.img.size[0]  # Определяем ширину.
        self.height = self.img.size[1]  # Определяем высоту.
        self.pix = self.img.load()  # Выгружаем значения пикселей.
        for i in range(self.width):
            for j in range(self.height):
                a = self.pix[i, j][0]
                b = self.pix[i, j][1]
                c = self.pix[i, j][2]
                self.draw.point((i, j), (255 - a, 255 - b, 255 - c))
        self.img.save('filtred.jpg', "JPEG")
        del self.draw

    def filter_sepia(self,poto):
        self.img = Image.open(poto)
        self.draw = ImageDraw.Draw(self.img)  # Создаем инструмент для рисования.
        self.width = self.img.size[0]  # Определяем ширину.
        self.height = self.img.size[1]  # Определяем высоту.
        self.pix = self.img.load()  # Выгружаем значения пикселей.
        for i in range(self.width):
            for j in range(self.height):
                a = self.pix[i, j][0]
                b = self.pix[i, j][1]
                c = self.pix[i, j][2]
                S = (a + b + c) // 3
                self.draw.point((i, j), (S, S, S))
        self.img.save('filtred1.jpg', "JPEG")
        del self.draw

