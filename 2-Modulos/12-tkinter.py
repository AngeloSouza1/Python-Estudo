import tkinter as tk
from tkinter import ttk, messagebox

# Configuração da janela principal
root = tk.Tk()
root.title("Formulário de Registro - OneBitCode Style")
root.geometry("500x450")
root.configure(bg="#222222")  # Fundo escuro para imitar o site

# Definição de fontes e estilos personalizados
title_font = ("Helvetica", 18, "bold")
default_font = ("Helvetica", 10)
highlight_font = ("Helvetica", 10, "bold")

# Estilos personalizados para ttk usando cores e bordas inspiradas no site
style = ttk.Style()
style.configure("TLabel", font=default_font, background="#333333", foreground="#ffffff")  # Fundo mais claro para labels
style.configure("TButton", font=highlight_font, padding=8, relief="flat", background="#FF6F61", foreground="#ffffff")
style.map("TButton", background=[("active", "#ff4a3d")])  # Cor mais clara ao passar o mouse
style.configure("TFrame", background="#333333", relief="groove", borderwidth=1)
style.configure("TCheckbutton", background="#333333", foreground="#ffffff", font=default_font)

# Frame principal com bordas e padding
main_frame = ttk.Frame(root, padding="20", style="TFrame")
main_frame.pack(fill="both", expand=True, padx=30, pady=30)

# Seção do título centralizado e destacado
title_label = ttk.Label(main_frame, text="Registre-se no OneBitCode", font=title_font, foreground="#FF6F61", background="#222222")
title_label.pack(pady=(0, 20))

# Frame de conteúdo com design de bordas e padding
content_frame = ttk.Frame(main_frame, padding="20", style="TFrame")
content_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Entrada de nome (desativada inicialmente)
name_label = ttk.Label(content_frame, text="Nome Completo:", font=default_font, background="#333333")
name_label.grid(row=0, column=0, sticky="w", pady=(10, 5), padx=5)

name_entry = ttk.Entry(content_frame, width=30, font=default_font, state="disabled")
name_entry.grid(row=0, column=1, pady=(10, 5), padx=5)

# Entrada de email (desativada inicialmente)
email_label = ttk.Label(content_frame, text="Email:", font=default_font, background="#333333")
email_label.grid(row=1, column=0, sticky="w", pady=5, padx=5)

email_entry = ttk.Entry(content_frame, width=30, font=default_font, state="disabled")
email_entry.grid(row=1, column=1, pady=5, padx=5)

# Campo de telefone (desativado inicialmente)
phone_label = ttk.Label(content_frame, text="Telefone:", font=default_font, background="#333333")
phone_label.grid(row=2, column=0, sticky="w", pady=5, padx=5)

phone_entry = ttk.Entry(content_frame, width=30, font=default_font, state="disabled")
phone_entry.grid(row=2, column=1, pady=5, padx=5)

# Checkbox de concordância com os termos
terms_var = tk.BooleanVar()
def toggle_inputs():
    state = "normal" if terms_var.get() else "disabled"
    name_entry.config(state=state)
    email_entry.config(state=state)
    phone_entry.config(state=state)

terms_check = ttk.Checkbutton(
    content_frame,
    text="Eu aceito os Termos de Serviço",
    variable=terms_var,
    command=toggle_inputs,
    style="TCheckbutton"  # Estilo de checkbutton para manter visível
)
terms_check.grid(row=3, column=0, columnspan=2, sticky="w", pady=(10, 5))

# Função para validar o formulário
def validate_form():
    if not name_entry.get().strip():
        return "Nome completo é obrigatório."
    if not email_entry.get().strip():
        return "Email é obrigatório."
    if not phone_entry.get().strip():
        return "Telefone é obrigatório."
    return None

# Função para submeter o formulário
def on_submit():
    error_message = validate_form()
    if error_message:
        messagebox.showerror("Erro de Validação", error_message)
    else:
        title_label.config(text=f"Obrigado, {name_entry.get()}!")
        messagebox.showinfo("Sucesso", "Formulário enviado com sucesso!")

# Frame para os botões
button_frame = ttk.Frame(main_frame, style="TFrame")
button_frame.pack(pady=15)

# Botões de Enviar e Cancelar
submit_button = ttk.Button(button_frame, text="Enviar", command=on_submit)
submit_button.grid(row=0, column=0, padx=(0, 10))

cancel_button = ttk.Button(button_frame, text="Cancelar", command=root.quit)
cancel_button.grid(row=0, column=1)

# Configuração de responsividade
content_frame.grid_columnconfigure(1, weight=1)

# Iniciar a aplicação
root.mainloop()
