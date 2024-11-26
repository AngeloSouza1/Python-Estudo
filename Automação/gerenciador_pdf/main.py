import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys
from pdf_functions import (
    get_pdf_metadata, extract_text_from_pdf, split_pdf,
    extract_main_image_from_each_page, rotate_pdf, merge_pdf, convert_img_pdf
)




# Funções GUI
def selecionar_arquivo():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        entrada_arquivo.delete(0, tk.END)
        entrada_arquivo.insert(0, pdf_path)

def get_pdf_metadata_gui():
    pdf_path = entrada_arquivo.get()
    if not pdf_path or not os.path.isfile(pdf_path):
        messagebox.showerror("Erro", "Por favor, selecione um arquivo PDF válido.")
        return
    info = get_pdf_metadata(pdf_path)
    messagebox.showinfo("Metadados do PDF", f"Metadados: {info}")

def extract_text_gui():
    pdf_path = entrada_arquivo.get()
    if not pdf_path or not os.path.isfile(pdf_path):
        messagebox.showerror("Erro", "Por favor, selecione um arquivo PDF válido.")
        return
    text = extract_text_from_pdf(pdf_path)
    messagebox.showinfo("Texto Extraído", text[:500] + "..." if len(text) > 500 else text)

def exibir_entrada_rotacao():
    pdf_path = entrada_arquivo.get()
    if not pdf_path or not os.path.isfile(pdf_path):
        messagebox.showerror("Erro", "Por favor, selecione um arquivo PDF válido antes de rotacionar.")
        return
    rotacao_frame.pack(pady=10)
    entrada_rotacao.delete(0, tk.END)
    entrada_rotacao.insert(0, "90")
    root.geometry("500x700")  # Aumenta a altura do formulário

def rotate_pdf_gui(rotation_angle):
    pdf_path = entrada_arquivo.get()
    if not pdf_path or not os.path.isfile(pdf_path):
        messagebox.showerror("Erro", "Por favor, selecione um arquivo PDF válido.")
        return
    try:
        rotation_angle = int(rotation_angle)
        if rotation_angle not in [90, 180, 270, 360]:
            raise ValueError("Ângulo inválido")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um ângulo válido (90, 180, 270 ou 360 graus).")
        return
    try:
        output_path = os.path.join("files", "rotated_file.pdf")
        rotate_pdf(pdf_path, 0, rotation_angle, output_path)
        messagebox.showinfo("Rotação Concluída", f"PDF rotacionado com sucesso! Salvo em: {output_path}")
        rotacao_frame.pack_forget()
        root.geometry("500x600")  # Retorna ao tamanho original
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao rotacionar o PDF: {str(e)}")

def split_pdf_gui():
    pdf_path = entrada_arquivo.get()
    if not pdf_path or not os.path.isfile(pdf_path):
        messagebox.showerror("Erro", "Por favor, selecione um arquivo PDF válido.")
        return
    try:
        split_pdf(pdf_path)
        messagebox.showinfo("Divisão Completa", "PDF dividido com sucesso! Verifique a pasta 'files'.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao dividir o PDF: {str(e)}")

def extract_images_gui():
    pdf_path = entrada_arquivo.get()
    if not pdf_path or not os.path.isfile(pdf_path):
        messagebox.showerror("Erro", "Por favor, selecione um arquivo PDF válido.")
        return
    try:
        extract_main_image_from_each_page(pdf_path, output_folder="files")
        messagebox.showinfo("Extração de Imagens", "Imagens extraídas com sucesso! Verifique a pasta 'files'.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao extrair imagens: {str(e)}")

def merge_pdf_gui():
    pdf_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if not pdf_paths:
        messagebox.showerror("Erro", "Nenhum arquivo PDF foi selecionado.")
        return
    try:
        merge_pdf(pdf_paths, output_filename="files/merged_output.pdf")
        messagebox.showinfo("PDFs Mesclados", "PDFs combinados com sucesso! Verifique a pasta 'files'.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao mesclar PDFs: {str(e)}")

def convert_image_to_pdf_gui():
    image_path = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[
            ("Imagens", "*.png *.jpg *.jpeg *.bmp *.tiff *.gif"),
            ("Todos os Arquivos", "*.*"),
        ]
    )
    if not image_path:
        messagebox.showerror("Erro", "Nenhuma imagem foi selecionada.")
        return
    try:
        convert_img_pdf(image_path)
        messagebox.showinfo("Conversão Concluída", "Imagem convertida para PDF com sucesso! Verifique a pasta 'files'.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao converter a imagem: {str(e)}")

# Interface Gráfica
root = tk.Tk()
root.title("Gerenciador de PDF")
root.geometry("500x600")
root.configure(bg="#121212")
root.resizable(False, False)

from tkinter import PhotoImage

banner_image = PhotoImage(file="image/banner.png")
banner_label = tk.Label(root, image=banner_image, bg="#121212")
banner_label.pack(fill=tk.X)

input_frame = tk.Frame(root, bg="#1E1E1E", bd=2, relief="flat")
input_frame.pack(pady=10, padx=20, fill="x")

entrada_arquivo = tk.Entry(
    input_frame,
    width=40,
    font=("Arial", 12),
    bg="#2C2C2C",
    fg="white",
    relief="flat",
    justify="left"
)
entrada_arquivo.pack(padx=10, pady=5, fill="x")

btn_selecionar = tk.Button(
    input_frame,
    text="Selecionar Arquivo",
    command=selecionar_arquivo,
    bg="#2C2C2C",
    fg="white",
    font=("Arial", 10),
    relief="flat"
)
btn_selecionar.pack(pady=5)

rotacao_frame = tk.Frame(root, bg="#121212")
rotacao_label = tk.Label(rotacao_frame, text="Ângulo de Rotação:", bg="#121212", fg="white", font=("Arial", 12))
rotacao_label.grid(row=0, column=0, padx=5)

entrada_rotacao = tk.Entry(rotacao_frame, width=10, font=("Arial", 12), bg="#1E1E1E", fg="white")
entrada_rotacao.grid(row=0, column=1, padx=5)

tk.Button(
    rotacao_frame,
    text="Confirmar Rotação",
    command=lambda: rotate_pdf_gui(entrada_rotacao.get()),
    bg="#1E1E1E",
    fg="white",
    font=("Arial", 12)
).grid(row=1, column=0, columnspan=2, pady=5)

rotacao_frame.pack_forget()

funcoes = [
    ("📜 Obter Metadados", get_pdf_metadata_gui),
    ("✍ Extrair Texto", extract_text_gui),
    ("🔄 Dividir PDF", split_pdf_gui),
    ("🖼 Extrair Imagens", extract_images_gui),
    ("➕ Mesclar PDFs", merge_pdf_gui),
    ("📑 Imagem para PDF", convert_image_to_pdf_gui),
    ("🔁 Rotacionar Página", exibir_entrada_rotacao),
]

for func_name, func in funcoes:
    tk.Button(root, text=func_name, command=func, width=30, bg="#1E1E1E", fg="white", font=("Arial", 12)).pack(pady=5)

rodape = tk.Label(root, text="Criado por Angelo Souza © 2024", bg="#121212", fg="white", font=("Arial", 10))
rodape.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
