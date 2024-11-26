import PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import os
import fitz
from PIL import Image

def get_pdf_metadata(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        info = reader.metadata
    return info

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        results = []
        for i in range(0, len(reader.pages)):
            selected_page = reader.pages[i]
            text = selected_page.extract_text()
            results.append(text)
        return ' '.join(results)

def split_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        for page_num in range(0, len(reader.pages)):
            selected_page = reader.pages[page_num]
            writer = PdfWriter()
            writer.add_page(selected_page)
            filename = os.path.split(pdf_path)[1]
            output_filename = f"files/{filename}_{page_num+1}.pdf"
            with open(output_filename, "wb") as out:
                writer.write(out)
            print(f"PDF criado com o nome: {output_filename}")

def get_pdf_upto(pdf_path, start_page: int = 0, stop_page: int = 0):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        for page_num in range(start_page, stop_page):
            selected_page = reader.pages[page_num]
            writer.add_page(selected_page)
        filename = os.path.split(pdf_path)[1]
        output_filename = f"files/{filename}_from_{start_page+1}_to_{stop_page+1}.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)

def fetch_all_pdf_files(parent_folder: str):
    target_files = []
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            if name.endswith(".pdf"):
                target_files.append(os.path.join(path, name))
    return target_files

def merge_pdf(list_pdfs, output_filename="files/final_pdf.pdf"):
    merger = PdfMerger()
    with open(output_filename, "wb") as f:
        for file in list_pdfs:
            merger.append(file)
        merger.write(f)

def rotate_pdf(pdf_path, page_num: int, rotation: int = 90):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])
        writer.pages[page_num].rotate(rotation)
        filename = os.path.split(pdf_path)[1]
        output_filename = f"files/{filename}_{rotation}_rotated_page.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)

def extract_main_image_from_each_page(pdf_path, output_folder="files"):
    """
    Extrai apenas uma imagem por página do PDF.
    :param pdf_path: Caminho para o arquivo PDF.
    :param output_folder: Pasta de saída para salvar as imagens.
    """
    # Certifique-se de que a pasta de saída exista
    os.makedirs(output_folder, exist_ok=True)

    # Abrir o PDF
    pdf_document = fitz.open(pdf_path)

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        images = page.get_images(full=True)  # Obtem todas as imagens da página

        if not images:
            print(f"Nenhuma imagem encontrada na página {page_num + 1}.")
            continue

        # Selecionar apenas a primeira imagem (principal) da página
        xref = images[0][0]  # Referência da primeira imagem
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]  # Extensão da imagem (png, jpeg, etc.)

        # Nome do arquivo de saída
        img_filename = f"{output_folder}/page{page_num + 1}_main_image.{image_ext}"

        # Salvar a imagem
        with open(img_filename, "wb") as img_file:
            img_file.write(image_bytes)

        print(f"Imagem principal extraída da página {page_num + 1}: {img_filename}")

    print("Extração de imagens concluída.")
    
def convert_img_pdf(image_file):
    my_image = Image.open(image_file)
    img = my_image.convert("RGB")
    filename = f"{os.path.splitext(image_file)[0]}.pdf"
    img.save(filename)


# Exemplo de uso

#  Buscando Dados e Metadados de um Arquivo PDF 
# print(get_pdf_metadata("files/sample.pdf"))
# print(get_pdf_metadata("files/sample.pdf").title)
# print(get_pdf_metadata("files/sample.pdf").author)
# print(extract_text_from_pdf("files/sample.pdf"))
# Dividindo PDF por página
# bvsplit_pdf("files/teste.pdf")
# Dividindo PDF por Página Selecionada
# get_pdf_upto("files/teste.pdf", 1, 2)
# Listando PDFs / Merge
# print(fetch_all_pdf_files("files/"))
# pdf_list = fetch_all_pdf_files("files/")
# merge_pdf(pdf_list)
# Rotacionando Página
# rotate_pdf("files/sample.pdf", 0)
# Extração de Imagens
# extract_main_image_from_each_page("files/teste1.pdf")
# Conversão de Imagem
convert_img_pdf("files/page1_main_image.png")
