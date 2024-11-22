import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk  # Biblioteca necessária para lidar com imagens
from organizador import organizar_arquivos  # Importar a função do organizador.py

def selecionar_diretorio():
    """
    Abre o diálogo para selecionar o diretório e define no campo de entrada.
    """
    diretorio = filedialog.askdirectory(title="Selecione o diretório para organizar")
    if diretorio:
        entrada_diretorio.set(diretorio)

def organizar():
    """
    Chama a função de organização do módulo organizador.
    """
    diretorio = entrada_diretorio.get()
    if not diretorio:
        messagebox.showwarning("Aviso", "Por favor, selecione um diretório!")
        return
    try:
        organizar_arquivos(diretorio)  # Chama a função do organizador.py
        messagebox.showinfo("Sucesso", f"Arquivos organizados com sucesso no diretório:\n{diretorio}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao organizar os arquivos: {str(e)}")

def fechar():
    """
    Fecha a aplicação.
    """
    janela.quit()

# Funções de criação de elementos da interface (mesmas do seu código)
def criar_botao_com_label(canvas, imagem, texto, comando, largura, altura, x, y, cor_fundo, cor_hover, cor_texto):
    raio = altura // 2
    # Fundo do botão arredondado
    oval_esq = canvas.create_oval(x, y, x + altura, y + altura, fill=cor_fundo, outline="")
    oval_dir = canvas.create_oval(x + largura - altura, y, x + largura, y + altura, fill=cor_fundo, outline="")
    retangulo = canvas.create_rectangle(x + raio, y, x + largura - raio, y + altura, fill=cor_fundo, outline="")
    botao_imagem = canvas.create_image(
        x + largura // 2,
        y + altura // 2,
        image=imagem,
        anchor="center",
    )
    # Label abaixo do botão
    texto_label = canvas.create_text(
        x + largura // 2,
        y + altura + 15,  # Ajusta a posição do texto
        text=texto,
        fill=cor_texto,
        font=("Roboto", 10),
    )
    # Agrupa elementos
    botao_id = f"botao_{texto}"
    canvas.addtag_withtag(botao_id, oval_esq)
    canvas.addtag_withtag(botao_id, oval_dir)
    canvas.addtag_withtag(botao_id, retangulo)
    canvas.addtag_withtag(botao_id, botao_imagem)
    canvas.addtag_withtag(botao_id, texto_label)
    # Efeitos de hover
    def hover_enter(event):
        canvas.itemconfig(oval_esq, fill=cor_hover)
        canvas.itemconfig(oval_dir, fill=cor_hover)
        canvas.itemconfig(retangulo, fill=cor_hover)
    def hover_leave(event):
        canvas.itemconfig(oval_esq, fill=cor_fundo)
        canvas.itemconfig(oval_dir, fill=cor_fundo)
        canvas.itemconfig(retangulo, fill=cor_fundo)
    canvas.tag_bind(botao_id, "<Button-1>", lambda e: comando())
    canvas.tag_bind(botao_id, "<Enter>", hover_enter)
    canvas.tag_bind(botao_id, "<Leave>", hover_leave)

def criar_campo_redondo(canvas, largura, altura, x, y, cor_fundo):
    raio = altura // 2
    canvas.create_oval(x, y, x + altura, y + altura, fill=cor_fundo, outline="")
    canvas.create_oval(x + largura - altura, y, x + largura, y + altura, fill=cor_fundo, outline="")
    canvas.create_rectangle(x + raio, y, x + largura - raio, y + altura, fill=cor_fundo, outline="")
    entry = tk.Entry(
        canvas,
        textvariable=entrada_diretorio,
        font=("Roboto", 12),
        bg=cor_fundo,
        fg="#f8f8f2",
        insertbackground="#f8f8f2",
        relief="flat",
        highlightthickness=0,
        width=30,
    )
    canvas.create_window(x + largura // 2, y + altura // 2, window=entry, width=largura - 20, height=altura - 10)
    return entry

# Configuração da janela principal
janela = tk.Tk()
janela.title("")
janela.geometry("700x450")
janela.configure(bg="#0d1117")
janela.resizable(False, False)

# Variável para o campo de entrada
entrada_diretorio = tk.StringVar()

# Banner
frame_banner = tk.Frame(janela, bg="#0d1117", height=100)
frame_banner.pack(fill="x", pady=10)

try:
    banner_img = Image.open("banner.png").resize((700, 100))
    banner_tk = ImageTk.PhotoImage(banner_img)
    banner_label = tk.Label(frame_banner, image=banner_tk, bg="#0d1117")
    banner_label.pack()
except FileNotFoundError:
    titulo = tk.Label(
        frame_banner,
        text="Organizador de Arquivos",
        font=("Roboto", 24, "bold"),
        bg="#0d1117",
        fg="#ffffff",
    )
    titulo.pack(pady=10)

# Campo de entrada
frame_campo = tk.Frame(janela, bg="#0d1117")
frame_campo.pack(pady=20)

rotulo_diretorio = tk.Label(
    frame_campo,
    text="Diretório:",
    font=("Roboto", 12),
    bg="#0d1117",
    fg="#58a6ff",
)
rotulo_diretorio.pack(anchor="center", pady=5)

canvas_campo = tk.Canvas(frame_campo, bg="#0d1117", highlightthickness=0, width=700, height=60)
canvas_campo.pack()

campo_diretorio = criar_campo_redondo(canvas_campo, largura=600, altura=40, x=60, y=10, cor_fundo="#161b22")

# Botões
canvas_botoes = tk.Canvas(janela, bg="#0d1117", highlightthickness=0, width=700, height=150)
canvas_botoes.pack()

# Carregando imagens
try:
    img_selecionar = ImageTk.PhotoImage(Image.open("selecionar.png").resize((30, 30)))
    img_organizar = ImageTk.PhotoImage(Image.open("organizar.png").resize((30, 30)))
    img_fechar = ImageTk.PhotoImage(Image.open("fechar.png").resize((30, 30)))
except FileNotFoundError as e:
    print(f"Erro ao carregar imagens: {e}")
    janela.destroy()

criar_botao_com_label(
    canvas_botoes,
    img_selecionar,
    "Selecionar",
    selecionar_diretorio,
    largura=150,
    altura=33,
    x=75,
    y=30,
    cor_fundo="#161b22",
    cor_hover="#1a2735",
    cor_texto="#f8f8f2",
)

criar_botao_com_label(
    canvas_botoes,
    img_organizar,
    "Organizar",
    organizar,
    largura=150,
    altura=33,
    x=275,
    y=30,
    cor_fundo="#161b22",
    cor_hover="#1a2735",
    cor_texto="#f8f8f2",
)

criar_botao_com_label(
    canvas_botoes,
    img_fechar,
    "Fechar",
    fechar,
    largura=150,
    altura=33,
    x=475,
    y=30,
    cor_fundo="#161b22",
    cor_hover="#1a2735",
    cor_texto="#f8f8f2",
)

# Rodapé
rodape = tk.Label(
    janela,
    text="Criado por Angelo Souza © 2024",
    font=("Roboto", 10),
    bg="#0d1117",
    fg="#58a6ff",
)
rodape.pack(side="bottom", pady=10)

# Loop da Interface
janela.mainloop()
