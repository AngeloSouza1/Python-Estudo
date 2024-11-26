import os
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import fitz  # PyMuPDF
from PIL import Image

def get_pdf_metadata(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        return reader.metadata

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        return " ".join(page.extract_text() for page in reader.pages)

def split_pdf(pdf_path, output_folder="files"):
    os.makedirs(output_folder, exist_ok=True)
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)
            output_filename = f"{output_folder}/{os.path.basename(pdf_path).split('.')[0]}_page_{i+1}.pdf"
            with open(output_filename, "wb") as out:
                writer.write(out)

def extract_main_image_from_each_page(pdf_path, output_folder="files"):
    """
    Extrai todas as imagens de todas as páginas de um PDF.
    :param pdf_path: Caminho do arquivo PDF.
    :param output_folder: Pasta para salvar as imagens extraídas.
    """
    os.makedirs(output_folder, exist_ok=True)
    pdf_document = fitz.open(pdf_path)

    for page_index, page in enumerate(pdf_document):
        images = page.get_images(full=True)
        for image_index, image in enumerate(images):
            xref = image[0]
            base_image = pdf_document.extract_image(xref)
            image_ext = base_image["ext"]
            image_bytes = base_image["image"]
            output_path = os.path.join(output_folder, f"page_{page_index+1}_image_{image_index+1}.{image_ext}")

            with open(output_path, "wb") as img_file:
                img_file.write(image_bytes)


def rotate_pdf(pdf_path, page_num, rotation, output_path):
    """
    Rotaciona a página especificada de um PDF.
    :param pdf_path: Caminho do arquivo PDF.
    :param page_num: Número da página a ser rotacionada.
    :param rotation: Ângulo de rotação (em graus).
    :param output_path: Caminho para salvar o arquivo rotacionado.
    """
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        page = reader.pages[page_num]
        page.rotate(rotation)
        writer.add_page(page)
        with open(output_path, "wb") as out:
            writer.write(out)

def merge_pdf(list_pdfs, output_filename="files/merged.pdf"):
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    merger = PdfMerger()
    for pdf in list_pdfs:
        merger.append(pdf)
    with open(output_filename, "wb") as out:
        merger.write(out)

def convert_img_pdf(image_file, output_folder="files"):
    """
    Converte uma imagem em PDF e salva na pasta especificada.
    :param image_file: Caminho do arquivo de imagem.
    :param output_folder: Pasta de saída para o PDF.
    """
    # Criar a pasta de saída, se não existir
    os.makedirs(output_folder, exist_ok=True)

    # Abrir a imagem e converter para PDF
    img = Image.open(image_file).convert("RGB")
    output_filename = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(image_file))[0]}.pdf")
    
    # Salvar o PDF
    img.save(output_filename)
    return output_filename
