from PIL import Image, ImageEnhance, ImageFilter

# 1 - Importando a Imagem / Convertendo a imagem em escala de cinza
img = Image.open('data/moto.png')
print(img)
img.show()

gray_img = img.convert('L')
gray_img.show()