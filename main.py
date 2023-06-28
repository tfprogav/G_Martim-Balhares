import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector

def buscar_registros():
    # Ocultar o botão "Buscar Registros"
    button.grid_forget()

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

    # Crie uma tabela (Treeview) para exibir os registros
    table = ttk.Treeview(root, columns=colunas, show="headings", style="Custom.Treeview")
    table.grid(row=1, column=0, sticky="nsew")

    # Defina o estilo da tabela
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#C0C0C0")

    # Adicione os nomes das colunas na tabela
    for coluna in colunas:
        table.heading(coluna, text=coluna)

    # Adicione os registros na tabela
    for registro in registros:
        table.insert("", "end", values=registro)

    # Crie a barra de rolagem vertical
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=table.yview)
    scrollbar.grid(row=1, column=1, sticky="ns")

    # Vincule a barra de rolagem à tabela
    table.configure(yscrollcommand=scrollbar.set)

    # Feche o cursor e a conexão
    cursor.close()
    conexao.close()

# Crie a janela principal
root = tk.Tk()
root.title("Gestão de Utilizadores")

# Crie um botão para buscar os registros
button = tk.Button(root, text="Buscar Registros", command=buscar_registros)
button.grid(row=0, column=0)

# Configure o sistema de grade para expandir a tabela verticalmente
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Execute a janela principal
root.mainloop()

