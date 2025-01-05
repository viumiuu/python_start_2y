from PIL import Image
from PIL import ImageFilter
# для бонусного завдання
from PIL import ImageEnhance


with Image.open('original.jpg') as pic_original:
    print ("Зображення відкрито\nРозмір:", pic_original.size)
    print("Формат:", pic_original.format)
    print("Тип:", pic_original.mode)
    pic_original.show()

    pic_grey = pic_original.convert("L")
    pic_grey.save("gray.jpg")
    print ("Зображення відкрито\nРозмір:", pic_grey.size)
    print("Формат:", pic_grey.format)
    print("Тип:", pic_grey.mode)
    pic_grey.show()

    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save("blured.jpg")
    pic_blured.show()

    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.save("up.jpg")
    pic_up.show()

    pic_mirrow = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_mirrow.save("mirrow.jpg")
    pic_mirrow.show()

    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast= pic_contrast.enhance(1.5)
    pic_contrast.save("contr.jpg")
    pic_contrast.show()