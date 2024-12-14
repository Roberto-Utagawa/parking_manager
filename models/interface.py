import tkinter as tk
from tkinter import messagebox
from models import Usuario, Vaga, Reserva

# Função para criar um usuário
def criar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    
    if not nome or not email or not telefone:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return
    
    novo_usuario = Usuario(len(usuarios) + 1, nome, email, "COMUM", telefone)
    usuarios.append(novo_usuario)
    
    messagebox.showinfo("Sucesso", f"Usuário {novo_usuario.nome} cadastrado com sucesso!")
    limpar_campos_usuario()

# Função para criar uma reserva
def criar_reserva():
    nome_usuario = entry_nome_usuario.get()
    vaga = entry_vaga.get()
    
    if not nome_usuario or not vaga:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return
    
    usuario = buscar_usuario(nome_usuario)
    if not usuario:
        messagebox.showerror("Erro", f"Usuário {nome_usuario} não encontrado.")
        return
    
    vaga_obj = buscar_vaga(vaga)
    if not vaga_obj or vaga_obj.status != "LIVRE":
        messagebox.showerror("Erro", "Vaga indisponível ou inválida.")
        return
    
    nova_reserva = Reserva(len(reservas) + 1, usuario, vaga_obj, "Reservada")
    reservas.append(nova_reserva)
    vaga_obj.status = "OCUPADA"
    
    messagebox.showinfo("Sucesso", f"Reserva feita para o usuário {usuario.nome} na vaga {vaga_obj.localizacao}.")
    limpar_campos_reserva()

# Função para buscar um usuário pelo nome
def buscar_usuario(nome):
    for usuario in usuarios:
        if usuario.nome == nome:
            return usuario
    return None

# Função para buscar uma vaga
def buscar_vaga(localizacao):
    for vaga in vagas:
        if vaga.localizacao == localizacao:
            return vaga
    return None

# Função para limpar os campos de usuário
def limpar_campos_usuario():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

# Função para limpar os campos de reserva
def limpar_campos_reserva():
    entry_nome_usuario.delete(0, tk.END)
    entry_vaga.delete(0, tk.END)

# Função para iniciar a interface gráfica
def iniciar_interface():
    # Criando a janela principal
    root = tk.Tk()
    root.title("Gerenciamento de Estacionamento")

    # Listas de objetos
    usuarios = []
    vagas = [Vaga(1, "A1", "LIVRE"), Vaga(2, "A2", "LIVRE"), Vaga(3, "B1", "OCUPADA")]
    reservas = []

    # Frames
    frame_usuario = tk.Frame(root)
    frame_usuario.pack(pady=10)

    frame_reserva = tk.Frame(root)
    frame_reserva.pack(pady=10)

    # Widgets para cadastro de usuário
    label_nome = tk.Label(frame_usuario, text="Nome:")
    label_nome.grid(row=0, column=0, padx=5, pady=5)
    entry_nome = tk.Entry(frame_usuario)
    entry_nome.grid(row=0, column=1, padx=5, pady=5)

    label_email = tk.Label(frame_usuario, text="E-mail:")
    label_email.grid(row=1, column=0, padx=5, pady=5)
    entry_email = tk.Entry(frame_usuario)
    entry_email.grid(row=1, column=1, padx=5, pady=5)

    label_telefone = tk.Label(frame_usuario, text="Telefone:")
    label_telefone.grid(row=2, column=0, padx=5, pady=5)
    entry_telefone = tk.Entry(frame_usuario)
    entry_telefone.grid(row=2, column=1, padx=5, pady=5)

    btn_criar_usuario = tk.Button(frame_usuario, text="Criar Usuário", command=criar_usuario)
    btn_criar_usuario.grid(row=3, column=0, columnspan=2, pady=10)

    # Widgets para reserva
    label_nome_usuario = tk.Label(frame_reserva, text="Nome do Usuário:")
    label_nome_usuario.grid(row=0, column=0, padx=5, pady=5)
    entry_nome_usuario = tk.Entry(frame_reserva)
    entry_nome_usuario.grid(row=0, column=1, padx=5, pady=5)

    label_vaga = tk.Label(frame_reserva, text="Vaga (ex: A1):")
    label_vaga.grid(row=1, column=0, padx=5, pady=5)
    entry_vaga = tk.Entry(frame_reserva)
    entry_vaga.grid(row=1, column=1, padx=5, pady=5)

    btn_reservar = tk.Button(frame_reserva, text="Reservar Vaga", command=criar_reserva)
    btn_reservar.grid(row=2, column=0, columnspan=2, pady=10)

    # Inicia o loop principal da interface
    root.mainloop()
