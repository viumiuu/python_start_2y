from PIL import Image
from PIL import ImageFilter


class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.chenged = list()

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print("Файл не знайдено")
        self.original.show()


    def do_left(self):
        roteted = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.chenged.append(roteted)

        temp_filename = self.filename.split(".")
        new_filename = temp_filename[0] + str(len(self.chenged)) + ".jpg"
        roteted.save(new_filename)


    # бонус. Обрізати фотографію
    def do_cropped(self):
        pass


MyImage = ImageEditor('original_new.jpg')
MyImage.open()


MyImage.do_left()
MyImage.do_cropped()


for im in MyImage.changed:
    im.show()
