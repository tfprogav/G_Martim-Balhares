import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from tkinter import messagebox

# Estabelecer uma conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="tf_prog_av"
)

# Buscar registros da tabela "q_utilizadores"
def buscar_registros():
    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Execute a consulta para buscar os registros
    cursor.execute("SELECT * FROM q_utilizadores")

    # Obtenha os registros retornados pela consulta
    registros = cursor.fetchall()

    # Fechar o cursor
    cursor.close()

    # Limpar a tabela existente
    for item in table.get_children():
        table.delete(item)

    # Adicionar os registros na tabela
    for registro in registros:
        table.insert("", "end", values=registro)

# Apagar o utilizador selecionado na tabela
def apagar_utilizador():
    # Obter o ID do utilizador selecionado na tabela
    selecionado = table.focus()
    if selecionado:
        utilizador_id = table.item(selecionado)["values"][0]

        # Confirmar a exclusão do utilizador
        if messagebox.askyesno("Confirmação", f"Deseja apagar o utilizador com ID {utilizador_id}?"):

            try:
                # Desabilitar temporariamente a restrição da chave estrangeira
                cursor = conexao.cursor()
                cursor.execute("SET FOREIGN_KEY_CHECKS=0")

                # Executar o comando para apagar o utilizador
                cursor.execute("DELETE FROM q_utilizadores WHERE utilizador_id = %s", (utilizador_id,))

                # Efetuar o commit das alterações
                conexao.commit()

                # Habilitar a restrição da chave estrangeira novamente
                cursor.execute("SET FOREIGN_KEY_CHECKS=1")

                # Fechar o cursor
                cursor.close()

                # Atualizar a exibição dos registros
                buscar_registros()

            except mysql.connector.Error as error:
                # Em caso de erro, imprimir a mensagem e reverter a desativação da restrição
                print("Erro ao apagar o utilizador:", error)
                cursor.execute("SET FOREIGN_KEY_CHECKS=1")
                cursor.close()
        # Caso o usuário se esqueça de selecionar um registo na tabela
        else:
            messagebox.showinfo("Aviso", "Nenhum utilizador selecionado.")

# Criar um novo utilizador
def criar_utilizador():
    def salvar_utilizador():
        # Obter os valores inseridos nos campos
        nome = entry_nome.get()
        email = entry_email.get()
        contacto = entry_contacto.get()
        morada = entry_morada.get()
        localidade = entry_localidade.get()
        nascimento = entry_nascimento.get()
        senha = entry_senha.get()
        perfil = entry_perfil.get()

        # Criar um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # Executar o comando para criar um novo utilizador
        cursor.execute(
            "INSERT INTO q_utilizadores (utilizador_nome, utilizador_email, utilizador_contacto, utilizador_morada, utilizador_localidade, utilizador_nascimento, utilizador_senha, utilizador_perfil) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (nome, email, contacto, morada, localidade, nascimento, senha, perfil))

        # Efetuar o commit das alterações
        conexao.commit()

        # Fechar o cursor
        cursor.close()

        # Atualizar a exibição dos registros
        buscar_registros()

        # Fechar a janela de criação de utilizador
        janela_utilizador.destroy()

    # Criar a janela para criação de utilizador
    janela_utilizador = tk.Toplevel()
    janela_utilizador.title("Criar Utilizador")

    label_nome = ttk.Label(janela_utilizador, text="Nome:")
    entry_nome = ttk.Entry(janela_utilizador)

    label_email = ttk.Label(janela_utilizador, text="Email:")
    entry_email = ttk.Entry(janela_utilizador)

    label_contacto = ttk.Label(janela_utilizador, text="Contacto:")
    entry_contacto = ttk.Entry(janela_utilizador)

    label_morada = ttk.Label(janela_utilizador, text="Morada:")
    entry_morada = ttk.Entry(janela_utilizador)

    label_localidade = ttk.Label(janela_utilizador, text="Localidade:")
    entry_localidade = ttk.Entry(janela_utilizador)

    label_nascimento = ttk.Label(janela_utilizador, text="Nascimento:")
    entry_nascimento = ttk.Entry(janela_utilizador)

    label_senha = ttk.Label(janela_utilizador, text="Senha:")
    entry_senha = ttk.Entry(janela_utilizador)

    label_perfil = ttk.Label(janela_utilizador, text="Perfil:")
    entry_perfil = ttk.Entry(janela_utilizador)

    # Botão responsável por salvar o novo registo
    btn_salvar = ttk.Button(janela_utilizador, text="Salvar", command=salvar_utilizador)

    label_nome.pack(padx=5, pady=5)
    entry_nome.pack(padx=5, pady=5)

    label_email.pack(padx=5, pady=5)
    entry_email.pack(padx=5, pady=5)

    label_contacto.pack(padx=5, pady=5)
    entry_contacto.pack(padx=5, pady=5)

    label_morada.pack(padx=5, pady=5)
    entry_morada.pack(padx=5, pady=5)

    label_localidade.pack(padx=5, pady=5)
    entry_localidade.pack(padx=5, pady=5)

    label_nascimento.pack(padx=5, pady=5)
    entry_nascimento.pack(padx=5, pady=5)

    label_senha.pack(padx=5, pady=5)
    entry_senha.pack(padx=5, pady=5)

    label_perfil.pack(padx=5, pady=5)
    entry_perfil.pack(padx=5, pady=5)

    btn_salvar.pack(padx=5, pady=10)

# Alterar o utilizador selecionado na tabela
def alterar_utilizador():
    # Obter o utilizador selecionado na tabela
    selecionado = table.focus()
    if selecionado:
        # Obter o ID do utilizador selecionado
        utilizador_id = table.item(selecionado)['values'][0]

        # Obter os dados do utilizador do banco de dados
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM q_utilizadores WHERE utilizador_id = %s", (utilizador_id,))
        utilizador = cursor.fetchone()
        cursor.close()

        def atualizar_utilizador():
            # Obter os valores inseridos nos campos
            nome = entry_nome.get()
            email = entry_email.get()
            contacto = entry_contacto.get()
            morada = entry_morada.get()
            localidade = entry_localidade.get()
            nascimento = entry_nascimento.get()
            senha = entry_senha.get()
            perfil = entry_perfil.get()

            # Criar um cursor para executar comandos SQL
            cursor = conexao.cursor()

            # Executar o comando para atualizar o utilizador
            cursor.execute(
                "UPDATE q_utilizadores SET utilizador_nome = %s, utilizador_email = %s, utilizador_contacto = %s, utilizador_morada = %s, utilizador_localidade = %s, utilizador_nascimento = %s, utilizador_senha = %s, utilizador_perfil = %s WHERE utilizador_id = %s",
                (nome, email, contacto, morada, localidade, nascimento, senha, perfil, utilizador_id))

            # Efetuar o commit das alterações
            conexao.commit()

            # Fechar o cursor
            cursor.close()

            # Fechar a janela de alteração de utilizador
            janela_alterar.destroy()

            # Atualizar a exibição dos registros
            buscar_registros()

        # Criar uma nova janela para editar os dados do utilizador
        janela_alterar = tk.Toplevel()
        janela_alterar.title("Alterar Utilizador")

        # Preencher os campos de entrada com os dados atuais do utilizador
        tk.Label(janela_alterar, text="Nome:").grid(row=0, column=0)
        entry_nome = tk.Entry(janela_alterar)
        entry_nome.insert(0, utilizador[1])
        entry_nome.grid(row=0, column=1)

        tk.Label(janela_alterar, text="Email:").grid(row=1, column=0)
        entry_email = tk.Entry(janela_alterar)
        entry_email.insert(0, utilizador[2])
        entry_email.grid(row=1, column=1)

        tk.Label(janela_alterar, text="Contacto:").grid(row=2, column=0)
        entry_contacto = tk.Entry(janela_alterar)
        entry_contacto.insert(0, utilizador[3])
        entry_contacto.grid(row=2, column=1)

        tk.Label(janela_alterar, text="Morada:").grid(row=3, column=0)
        entry_morada = tk.Entry(janela_alterar)
        entry_morada.insert(0, utilizador[4])
        entry_morada.grid(row=3, column=1)

        tk.Label(janela_alterar, text="Localidade:").grid(row=4, column=0)
        entry_localidade = tk.Entry(janela_alterar)
        entry_localidade.insert(0, utilizador[5])
        entry_localidade.grid(row=4, column=1)

        tk.Label(janela_alterar, text="Nascimento:").grid(row=5, column=0)
        entry_nascimento = tk.Entry(janela_alterar)
        entry_nascimento.insert(0, utilizador[6])
        entry_nascimento.grid(row=5, column=1)

        tk.Label(janela_alterar, text="Senha:").grid(row=6, column=0)
        entry_senha = tk.Entry(janela_alterar)
        entry_senha.insert(0, utilizador[7])
        entry_senha.grid(row=6, column=1)

        tk.Label(janela_alterar, text="Perfil:").grid(row=7, column=0)
        entry_perfil = tk.Entry(janela_alterar)
        entry_perfil.insert(0, utilizador[8])
        entry_perfil.grid(row=7, column=1)

        # Botão para atualizar o utilizador
        btn_atualizar = tk.Button(janela_alterar, text="Atualizar", command=atualizar_utilizador)
        btn_atualizar.grid(row=8, column=0, columnspan=2)
        # Caso o usuário se esqueça de selecionar um registo na tabela
    else:
        messagebox.showwarning("Aviso", "Selecione um utilizador para atualizar.")

# Criar uma interface gráfica para exibir registros da tabela no formato em árvore (treeview)
def criar_interface(content_frame):
    global table, frame# Variações globais

    # Remove todos os widgets filhos existentes
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Cria um novo frame dentro do content_frame
    frame = ttk.Frame(content_frame, padding="10")
    frame.pack()

    # Cria um objeto que exibe apenas os cabeçalhos das colunas
    table = ttk.Treeview(frame, columns=("ID", "Nome", "Email", "Contacto", "Morada", "Localidade", "Nascimento","Password", "Perfil"), show="headings")

    # Define as configurações de largura para cada coluna
    table.column("ID", width=50)
    table.column("Nome", width=150)
    table.column("Email", width=150)
    table.column("Contacto", width=100)
    table.column("Morada", width=150)
    table.column("Localidade", width=100)
    table.column("Nascimento", width=100)
    table.column("Perfil", width=100)

    # Define os cabeçalhos das colunas
    table.heading("ID", text="ID")
    table.heading("Nome", text="Nome")
    table.heading("Email", text="Email")
    table.heading("Contacto", text="Contacto")
    table.heading("Morada", text="Morada")
    table.heading("Localidade", text="Localidade")
    table.heading("Nascimento", text="Nascimento")
    table.heading("Password", text="Password")
    table.heading("Perfil", text="Perfil")

    # Cria uma barra de rolagem vertical e associa-a à visualização vertical da tabela
    scroll = ttk.Scrollbar(frame, orient="vertical", command=table.yview)
    table.configure(yscroll=scroll.set)

    # Cria 3 botões associados
    btn_atualizar = ttk.Button(content_frame, text="Atualizar", command=alterar_utilizador)
    btn_apagar = ttk.Button(content_frame, text="Apagar", command=apagar_utilizador)
    btn_criar = ttk.Button(content_frame, text="Criar", command=criar_utilizador)

    # Empacota os botões
    btn_atualizar.pack(pady=5)
    btn_apagar.pack(pady=5)
    btn_criar.pack(pady=5)

    # Empacota a tabela à esquerda e a barra de rolagem à direita
    table.pack(side="left")
    scroll.pack(side="right", fill="y")

    # Exibe os registros na tabela
    buscar_registros()