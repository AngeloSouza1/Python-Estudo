from PIL import Image, ImageEnhance, ImageFilter

# 1 - Importando a Imagem / Convertendo a imagem em escala de cinza
img = Image.open('data/moto.png')
# print(img)
img.show()

gray_img = img.convert('L')
# gray_img.show()

# 2 - Utilizando Operações em Imagem I
rotated_img = img.rotate(180)
# rotated_img.show()

transpose_img = img.transpose(Image.FLIP_LEFT_RIGHT)
# transpose_img.show()

resize_img_small = img.resize((300, 500))
# resize_img_small.show()

resize_img_big = img.resize((900, 1000))
# resize_img_big.show()

dim = (200, 200, 250, 300)
crop_img = img.crop(dim)
# crop_img.show()

# 3 - Utilizando Operações em Imagem II
enhancer = ImageEnhance.Brightness(img)
bright_img = enhancer.enhance(2)
# bright_img.show()

enhancer = ImageEnhance.Contrast(img)
contrast_img = enhancer.enhance(3)
# contrast_img.show()

# 4 - Utilizando Filtros
# filtro_blur = img.filter(ImageFilter.BLUR)
# filtro_blur = img.filter(ImageFilter.CONTOUR)
filtro_blur = img.filter(ImageFilter.DETAIL)
# filtro_blur = img.filter(ImageFilter.EMBOSS)
# filtro_blur = img.filter(ImageFilter.SMOOTH)
filtro_blur.show()