import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from tkinter import messagebox

def buscar_registros():
    global table  # Declarar a variável table como global

    # Realize a conexão com o banco de dados MySQL
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="tf_prog_av"
    )

    # Crie um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Execute a consulta para buscar os registros
    cursor.execute("SELECT * FROM q_utilizadores")

    # Obtenha os registros retornados pela consulta
    registros = cursor.fetchall()

    # Obtenha os nomes das colunas
    colunas = [i[0] for i in cursor.description]

    # Nomes verdadeiros das tabelas e labels correspondentes
    tabela_utilizadores = "q_utilizadores"
    labels_colunas = ["ID_User", "Nome", "Email", "Contacto", "Morada", "Localidade", "Nascimento", "Senha", "Perfil"]

    # Crie uma tabela (Treeview) para exibir os registros
    table = ttk.Treeview(root, columns=colunas, show="headings", style="Custom.Treeview")
    table.grid(row=2, column=0, columnspan=3, sticky="nsew")
    table.column("utilizador_id", width=100)
    table.column("utilizador_nome", width=100)
    table.column("utilizador_email", width=100)
    table.column("utilizador_contacto", width=100)
    table.column("utilizador_morada", width=100)
    table.column("utilizador_localidade", width=100)
    table.column("utilizador_nascimento", width=100)
    table.column("utilizador_senha", width=100)
    table.column("utilizador_perfil", width=100)

    # Defina o estilo da tabela
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#C0C0C0")

    # Adicione os nomes das colunas na tabela
    for coluna, label in zip(colunas, labels_colunas):
        table.heading(coluna, text=label)

    # Adicione os registros na tabela
    for registro in registros:
        table.insert("", "end", values=registro)

    # Crie a barra de rolagem vertical
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=table.yview)
    scrollbar.grid(row=2, column=3, sticky="ns")

    # Vincular a barra de rolagem à tabela
    table.configure(yscrollcommand=scrollbar.set)

    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()

def apagar_utilizador(table):
    # Obter o ID do utilizador selecionado na tabela
    selecionado = table.focus()
    if selecionado:
        utilizador_id = table.item(selecionado)["values"][0]

        # Confirmar a exclusão do utilizador
        if messagebox.askyesno("Confirmação", f"Deseja apagar o utilizador com ID {utilizador_id}?"):
            # Realizar a conexão com o banco de dados MySQL
            conexao = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="tf_prog_av"
            )

            # Criar um cursor para executar comandos SQL
            cursor = conexao.cursor()

            # Executar o comando para apagar o utilizador
            cursor.execute("DELETE FROM q_utilizadores WHERE utilizador_id = %s", (utilizador_id,))

            # Efetuar o commit das alterações
            conexao.commit()

            # Fechar o cursor e a conexão
            cursor.close()
            conexao.close()

            # Atualizar a exibição dos registros
            buscar_registros()

    else:
        messagebox.showinfo("Aviso", "Nenhum utilizador selecionado.")

def criar_utilizador():
    # Criar uma nova janela para preencher os dados do novo utilizador
    janela_criar = tk.Toplevel(root)
    janela_criar.title("Criar Utilizador")

    # Criar os widgets para preencher os dados do novo utilizador
    label_nome = tk.Label(janela_criar, text="Nome:")
    entry_nome = tk.Entry(janela_criar)
    label_email = tk.Label(janela_criar, text="Email:")
    entry_email = tk.Entry(janela_criar)
    label_contacto = tk.Label(janela_criar, text="Contacto:")
    entry_contacto = tk.Entry(janela_criar)
    label_morada = tk.Label(janela_criar, text="Morada:")
    entry_morada = tk.Entry(janela_criar)
    label_localidade = tk.Label(janela_criar, text="Localidade:")
    entry_localidade = tk.Entry(janela_criar)
    label_nascimento = tk.Label(janela_criar, text="Nascimento:")
    entry_nascimento = tk.Entry(janela_criar)
    label_senha = tk.Label(janela_criar, text="Senha:")
    entry_senha = tk.Entry(janela_criar)
    label_perfil = tk.Label(janela_criar, text="Perfil:")
    entry_perfil = tk.Entry(janela_criar)

    # Posicionar os widgets na janela usando o gerenciador de layout grid
    label_nome.grid(row=0, column=0, padx=10, pady=10)
    entry_nome.grid(row=0, column=1, padx=10, pady=10)
    label_email.grid(row=1, column=0, padx=10, pady=10)
    entry_email.grid(row=1, column=1, padx=10, pady=10)
    label_contacto.grid(row=2, column=0, padx=10, pady=10)
    entry_contacto.grid(row=2, column=1, padx=10, pady=10)
    label_morada.grid(row=3, column=0, padx=10, pady=10)
    entry_morada.grid(row=3, column=1, padx=10, pady=10)
    label_localidade.grid(row=4, column=0, padx=10, pady=10)
    entry_localidade.grid(row=4, column=1, padx=10, pady=10)
    label_nascimento.grid(row=5, column=0, padx=10, pady=10)
    entry_nascimento.grid(row=5, column=1, padx=10, pady=10)
    label_senha.grid(row=6, column=0, padx=10, pady=10)
    entry_senha.grid(row=6, column=1, padx=10, pady=10)
    label_perfil.grid(row=7, column=0, padx=10, pady=10)
    entry_perfil.grid(row=7, column=1, padx=10, pady=10)

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

        # Realizar a conexão com o banco de dados MySQL
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="tf_prog_av"
        )

        # Criar um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # Executar o comando para criar um novo utilizador
        cursor.execute("INSERT INTO q_utilizadores (utilizador_nome, utilizador_email, utilizador_contacto, utilizador_morada, utilizador_localidade, utilizador_nascimento, utilizador_senha, utilizador_perfil) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (nome, email, contacto, morada, localidade, nascimento, senha, perfil))

        # Efetuar o commit das alterações
        conexao.commit()

        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

        # Fechar a janela de criação de utilizador
        janela_criar.destroy()

        # Atualizar a exibição dos registros
        buscar_registros()

    # Botão para salvar o novo utilizador
    button_salvar = tk.Button(janela_criar, text="Salvar", command=salvar_utilizador)
    button_salvar.grid(row=8, column=1, sticky="se", padx=10, pady=10)

def alterar_utilizador(table):
    # Obter o ID do utilizador selecionado na tabela
    selecionado = table.focus()
    if selecionado:
        # Obter os valores do utilizador selecionado na tabela
        valores_selecionados = table.item(selecionado)["values"]

        def salvar_alteracoes():
            # Obter os novos valores inseridos nos campos
            novo_valores = [entry.get() for entry in entries]

            # Verificar se algum campo foi alterado
            campos_alterados = [indice for indice, novo_valor in enumerate(novo_valores) if
                                indice + 1 < len(valores_selecionados) and
                                novo_valor != valores_selecionados[indice + 1]]

            if not campos_alterados:
                # Nenhum campo foi alterado, encerrar a função
                janela_alterar.destroy()
                return

            # Realizar a conexão com o banco de dados MySQL
            conexao = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="tf_prog_av"
            )

            # Criar um cursor para executar comandos SQL
            cursor = conexao.cursor()

            # Obter os cabeçalhos da tabela através de uma consulta SQL
            tabela = "q_utilizadores"
            cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tabela}'")
            cursor.execute("SET FOREIGN_KEY_CHECKS=0")
            colunas = [column[0] for column in cursor.fetchall()]

            # Construir a consulta SQL com base nos campos alterados
            sql = "UPDATE q_utilizadores SET utilizador_nome = %s, utilizador_email = %s, utilizador_contacto = %s, utilizador_morada = %s, utilizador_localidade = %s, utilizador_nascimento = %s, utilizador_senha = %s, utilizador_perfil = %s WHERE utilizador_id = %s"
            parametros = ("Novo Nome", "novo_email@example.com", "987654321", "Nova Morada", "Nova Localidade", "2000-01-01","nova_senha", 1, 1)
            parametros = []


            for indice in campos_alterados:
                campo = colunas[indice + 1]  # Ignorar a primeira coluna (utilizador_id)
                sql += f"{campo} = %s, "
                parametros.append(novo_valores[indice])

            # Remover a vírgula extra e o espaço no final da consulta SQL
            sql = sql.rstrip(", ")

            # Adicionar a cláusula WHERE para atualizar apenas o registro selecionado
            sql += " WHERE utilizador_id = %s"
            parametros.append(valores_selecionados[0])

            # Executar o comando para atualizar o utilizador
            cursor.execute(sql, parametros)
            conexao.commit()

            # Reativar a verificação de chave estrangeira
            cursor.execute("SET FOREIGN_KEY_CHECKS=1")

            # Fechar o cursor e a conexão
            cursor.close()
            conexao.close()

            # Atualizar a exibição dos registros
            buscar_registros()

            # Fechar a janela de alteração do utilizador
            janela_alterar.destroy()

        # Criar uma nova janela para alterar os valores do utilizador
        janela_alterar = tk.Toplevel(root)
        janela_alterar.title("Alterar Utilizador")

        # Criar listas para armazenar as entradas de texto
        entries = []

        # Criar os widgets para editar os valores do utilizador
        labels_colunas = ["ID_User", "Nome", "Email", "Contacto", "Morada", "Localidade", "Nascimento", "Senha", "Perfil"]

        for i, label in enumerate(labels_colunas):
            # Criar o rótulo da coluna
            label_coluna = tk.Label(janela_alterar, text=label)
            label_coluna.grid(row=i, column=0, padx=10, pady=10)

            # Criar a caixa de entrada para o valor da coluna
            entry = tk.Entry(janela_alterar)
            entry.grid(row=i, column=1, padx=10, pady=10)

            # Inserir o valor existente na caixa de entrada
            entry.insert(0, valores_selecionados[i])

            # Adicionar a caixa de entrada à lista de entradas
            entries.append(entry)

        # Botão para salvar as alterações
        button_salvar = tk.Button(janela_alterar, text="Salvar", command=salvar_alteracoes)
        button_salvar.grid(row=len(labels_colunas), column=0, columnspan=2, padx=10, pady=10)

    else:
        messagebox.showinfo("Aviso", "Nenhum utilizador selecionado.")

# Crie a janela principal
root = tk.Tk()
root.title("Gestão de Utilizadores")

# Configurar o sistema de grade para expandir a tabela verticalmente
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# Crie uma seção para os botões "Criar Utilizador" e "Apagar Utilizador"
frame_botoes = tk.Frame(root, bg="#E0E0E0")
frame_botoes.grid(row=0, column=0, columnspan=3, sticky="ew")

# Botão para criar um novo utilizador
button_criar = tk.Button(frame_botoes, text="Criar Utilizador", command=criar_utilizador)
button_criar.grid(row=0, column=0, padx=10, pady=5)

# Botão para apagar um utilizador
button_apagar = tk.Button(frame_botoes, text="Apagar Utilizador", command=lambda: apagar_utilizador(table))
button_apagar.grid(row=0, column=1, padx=10, pady=5)

# Botão para alterar um utilizador
button_alterar = tk.Button(frame_botoes, text="Alterar Utilizador", command=lambda: alterar_utilizador(table))
button_alterar.grid(row=0, column=2, padx=10, pady=5)

# Botão para fechar o programa
button_fechar = tk.Button(frame_botoes, text="Fechar", command=root.quit)
button_fechar.grid(row=0, column=3, padx=10, pady=5)


# Exibir os registros na tabela
buscar_registros()

# Iniciar o loop principal do tkinter
root.mainloop()