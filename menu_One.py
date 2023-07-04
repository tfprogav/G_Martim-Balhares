import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from tkinter import messagebox

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="tf_prog_av"
)

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

        else:
            messagebox.showinfo("Aviso", "Nenhum utilizador selecionado.")

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


def abrir_janela_atualizar():
    print("Função abrir_janela_atualizar foi chamada.")
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

        def salvar_atualizacao():
            nome = entry_nome.get()
            email = entry_email.get()
            contacto = entry_contacto.get()
            morada = entry_morada.get()
            localidade = entry_localidade.get()
            nascimento = entry_nascimento.get()
            senha = entry_senha.get()
            perfil = entry_perfil.get()

            cursor = conexao.cursor()

            cursor.execute("UPDATE q_utilizadores SET utilizador_nome = %s, utilizador_email = %s, utilizador_contacto = %s, utilizador_morada = %s, utilizador_localidade = %s, utilizador_nascimento = %s, utilizador_senha = %s, utilizador_perfil = %s WHERE utilizador_id = %s",
                           (nome, email, contacto, morada, localidade, nascimento, senha, perfil, utilizador_id))

            conexao.commit()

            cursor.close()

            buscar_registros()

        janela_atualizacao = tk.Toplevel()
        janela_atualizacao.title("Atualizar Utilizador")

        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM q_utilizadores WHERE utilizador_id = %s", (utilizador_id,))
        utilizador = cursor.fetchone()

        label_nome = ttk.Label(janela_atualizacao, text="Nome:")
        entry_nome = ttk.Entry(janela_atualizacao)
        entry_nome.insert(0, utilizador[1])

        label_email = ttk.Label(janela_atualizacao, text="Email:")
        entry_email = ttk.Entry(janela_atualizacao)
        entry_email.insert(0, utilizador[2])

        label_contacto = ttk.Label(janela_atualizacao, text="Contacto:")
        entry_contacto = ttk.Entry(janela_atualizacao)
        entry_contacto.insert(0, utilizador[3])

        label_morada = ttk.Label(janela_atualizacao, text="Morada:")
        entry_morada = ttk.Entry(janela_atualizacao)
        entry_morada.insert(0, utilizador[4])

        label_localidade = ttk.Label(janela_atualizacao, text="Localidade:")
        entry_localidade = ttk.Entry(janela_atualizacao)
        entry_localidade.insert(0, utilizador[5])

        label_nascimento = ttk.Label(janela_atualizacao, text="Nascimento:")
        entry_nascimento = ttk.Entry(janela_atualizacao)
        entry_nascimento.insert(0, utilizador[6])

        label_senha = ttk.Label(janela_atualizacao, text="Senha:")
        entry_senha = ttk.Entry(janela_atualizacao)
        entry_senha.insert(0, utilizador[7])

        label_perfil = ttk.Label(janela_atualizacao, text="Perfil:")
        entry_perfil = ttk.Entry(janela_atualizacao)
        entry_perfil.insert(0, utilizador[8])

        btn_salvar = ttk.Button(janela_atualizacao, text="Salvar", command=salvar_atualizacao)

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

        janela_atualizacao.mainloop()
    else:
        messagebox.showinfo("Aviso", "Nenhum utilizador selecionado.")

def criar_interface(content_frame):
    global table, frame

    for widget in content_frame.winfo_children():
        widget.destroy()

    frame = ttk.Frame(content_frame, padding="10")
    frame.pack()

    table = ttk.Treeview(frame, columns=("ID", "Nome", "Email", "Contacto", "Morada", "Localidade", "Nascimento","Password", "Perfil"), show="headings")

    table.column("ID", width=50)
    table.column("Nome", width=150)
    table.column("Email", width=150)
    table.column("Contacto", width=100)
    table.column("Morada", width=150)
    table.column("Localidade", width=100)
    table.column("Nascimento", width=100)
    table.column("Password", width=100)
    table.column("Perfil", width=100)

    table.heading("ID", text="ID")
    table.heading("Nome", text="Nome")
    table.heading("Email", text="Email")
    table.heading("Contacto", text="Contacto")
    table.heading("Morada", text="Morada")
    table.heading("Localidade", text="Localidade")
    table.heading("Nascimento", text="Nascimento")
    table.heading("Password", text="Password")
    table.heading("Perfil", text="Perfil")

    scroll = ttk.Scrollbar(frame, orient="vertical", command=table.yview)
    table.configure(yscroll=scroll.set)

    btn_atualizar = ttk.Button(content_frame, text="Atualizar", command=abrir_janela_atualizar)
    btn_apagar = ttk.Button(content_frame, text="Apagar", command=apagar_utilizador)
    btn_criar = ttk.Button(content_frame, text="Criar", command=criar_utilizador)

    btn_atualizar.pack(pady=5)
    btn_apagar.pack(pady=5)
    btn_criar.pack(pady=5)

    table.pack(side="left")
    scroll.pack(side="right", fill="y")

    buscar_registros()