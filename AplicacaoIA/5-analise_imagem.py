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
