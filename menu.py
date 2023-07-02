from tkinter import *
from tkinter import ttk

def show_table():
    table_frame = Frame(root)
    table_frame.pack(side='left', fill='both', expand=True)

    # Cria o widget Treeview
    treeview = ttk.Treeview(table_frame, columns=('Coluna1', 'Coluna2'), show='headings')
    treeview.pack(side='left', fill='both', expand=True)

    # Define o cabeçalho das colunas
    treeview.heading('Coluna1', text='Menino')
    treeview.heading('Coluna2', text='Menina')

    # Insere os valores nas colunas
    treeview.insert('', 'end', values=('Carlos', 'Joana'))

def open_users():
    import main_users
    main_users.show_users(root)  # Chame a função do módulo main_users.py passando a janela root como argumento

root = Tk()
root.title('Centro de formação')
root.geometry('1280x640+280+150')
root.resizable(0, 0)

main_frame = Frame(root, bg='black', width=root.winfo_width() // 4, height=root.winfo_height())
main_frame.pack(side='left', fill='y')

button_styles = {
    'bg': '#008080',
    'fg': 'white',
    'activebackground': '#4C4C4C',
    'activeforeground': 'white',
    'font': "Arial 12",
    'borderwidth': 0,
    'highlightthickness': 0,
    'relief': 'flat',
    'cursor': 'hand2',
}

button1 = Button(main_frame, text='Gestão de Utilizadores', width=50, **button_styles, command=open_users)
button1.pack(pady=10)

button2 = Button(main_frame, text='Gestão de Alunos', width=50, **button_styles)
button2.pack(pady=10)

button3 = Button(main_frame, text='Gestão de Aulas e Horários', width=50, **button_styles)
button3.pack(pady=10)

button4 = Button(main_frame, text='Gestão de Pagamentos', width=50, **button_styles)
button4.pack(pady=10)

button5 = Button(main_frame, text='Gestão de Cursos', width=50, **button_styles)
button5.pack(pady=10)

button6 = Button(main_frame, text='Performance dos Alunos', width=50, **button_styles)
button6.pack(pady=10)

root.mainloop()
