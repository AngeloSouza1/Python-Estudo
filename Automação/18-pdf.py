import PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter

# 1 - Versão e Métodos da Lib
print(pdf.__version__)
print(dir(pdf))

# 2 - Importando arquivo PDF
file = open("files/sample.pdf", "rb")
reader = PdfReader(file)
print(reader)
print(reader.metadata)
info = reader.metadata

# 3 - Extraindo algumas informações
print(info.title)
print(info.author)
print(info.creator)
print(info.subject)
print(len(reader.pages))
print(reader.pages[0].extract_text())