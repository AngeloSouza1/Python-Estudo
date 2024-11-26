import PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import os

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
            
def get_pdf_upto(pdf_path, start_page:int=0,stop_page:int=0):
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

def fetch_all_pdf_files(parent_folder:str):
    target_files = []
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            if name.endswith(".pdf"):
                target_files.append(os.path.join(path,name))
    return target_files

def merge_pdf(list_pdfs, output_filename="files/final_pdf.pdf"):
    merger = PdfMerger()
    with open(output_filename, "wb") as f:
        for file in list_pdfs:
            merger.append(file)
        merger.write(f)

def rotate_pdf(pdf_path, page_num:int, rotation:int=90):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])
        writer.pages[page_num].rotate(rotation)
        filename = os.path.split(pdf_path)[1]
        output_filename = f"files/{filename}_{rotation}_rotated_page.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)

# print(get_pdf_metadata("files/sample.pdf"))
# print(get_pdf_metadata("files/sample.pdf").title)
# print(get_pdf_metadata("files/sample.pdf").author)
# print(extract_text_from_pdf("files/sample.pdf"))
# bvsplit_pdf("files/teste.pdf")
# get_pdf_upto("files/teste.pdf", 1, 2)
# print(fetch_all_pdf_files("files/"))
# pdf_list = fetch_all_pdf_files("files/")
# merge_pdf(pdf_list)

rotate_pdf("files/sample.pdf", 0)
