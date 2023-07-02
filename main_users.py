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

        # Fechar a janela de criação de utilizador
        janela_criar.destroy()

        # Atualizar a exibição dos registros
        buscar_registros()

    # Criar uma nova janela para preencher os dados do novo utilizador
    janela_criar = tk.Toplevel(root)
    janela_criar.title("Criar Utilizador")

    # Criar os campos e os rótulos para inserção dos dados
    tk.Label(janela_criar, text="Nome:").grid(row=0, column=0)
    entry_nome = tk.Entry(janela_criar)
    entry_nome.grid(row=0, column=1)

    tk.Label(janela_criar, text="Email:").grid(row=1, column=0)
    entry_email = tk.Entry(janela_criar)
    entry_email.grid(row=1, column=1)

    tk.Label(janela_criar, text="Contacto:").grid(row=2, column=0)
    entry_contacto = tk.Entry(janela_criar)
    entry_contacto.grid(row=2, column=1)

    tk.Label(janela_criar, text="Morada:").grid(row=3, column=0)
    entry_morada = tk.Entry(janela_criar)
    entry_morada.grid(row=3, column=1)

    tk.Label(janela_criar, text="Localidade:").grid(row=4, column=0)
    entry_localidade = tk.Entry(janela_criar)
    entry_localidade.grid(row=4, column=1)

    tk.Label(janela_criar, text="Nascimento:").grid(row=5, column=0)
    entry_nascimento = tk.Entry(janela_criar)
    entry_nascimento.grid(row=5, column=1)

    tk.Label(janela_criar, text="Senha:").grid(row=6, column=0)
    entry_senha = tk.Entry(janela_criar)
    entry_senha.grid(row=6, column=1)

    tk.Label(janela_criar, text="Perfil:").grid(row=7, column=0)
    entry_perfil = tk.Entry(janela_criar)
    entry_perfil.grid(row=7, column=1)

    # Criar o botão de salvar
    btn_salvar = tk.Button(janela_criar, text="Salvar", command=salvar_utilizador)
    btn_salvar.grid(row=8, column=0, columnspan=2)


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
        janela_alterar = tk.Toplevel(root)
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

    else:
        messagebox.showwarning("Aviso", "Selecione um utilizador para atualizar.")


def criar_interface():
    global root, table

    root = tk.Tk()
    root.title("Utilizadores")

    frame = ttk.Frame(root, padding="10")
    frame.grid()

    # Criar a tabela para exibir os registros
    columns = ("ID", "Nome", "Email", "Contacto", "Morada", "Localidade", "Nascimento", "Senha", "Perfil")
    table = ttk.Treeview(frame, columns=columns, show="headings")
    table.grid(row=0, column=0, columnspan=3, pady=10)

    # Adicionar os cabeçalhos da tabela
    for col in columns:
        table.heading(col, text=col)

    # Criar os botões
    btn_atualizar = ttk.Button(frame, text="Atualizar", command=alterar_utilizador)
    btn_atualizar.grid(row=1, column=0, padx=5, pady=5)

    btn_apagar = ttk.Button(frame, text="Apagar", command=apagar_utilizador)
    btn_apagar.grid(row=1, column=1, padx=5, pady=5)

    btn_criar = ttk.Button(frame, text="Criar", command=criar_utilizador)
    btn_criar.grid(row=1, column=2, padx=5, pady=5)

    # Definir o redimensionamento das colunas da tabela
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    # Inicializar a exibição dos registros
    buscar_registros()

    root.mainloop()

# Iniciar a interface
criar_interface()