from tkinter import *
from tkinter import ttk

import main_users_def

# Definição de funções que limpam o content_frame (chamando a função clear_content_frame())
# e criam um rótulo com os nomes respetivos. O rótulo é adicionado ao content_frame
def show_gestao_utilizadores():
    clear_content_frame()
    label = Label(content_frame, text='Informações de Gestão de Utilizadores', font=('Arial', 14))
    label.pack(pady=20)

def show_gestao_alunos():
    clear_content_frame()
    label = Label(content_frame, text='Informações de Gestão de Alunos', font=('Arial', 14))
    label.pack(pady=20)

def show_gestao_aulas_horarios():
    clear_content_frame()
    label = Label(content_frame, text='Informações de Gestão de Aulas e Horários', font=('Arial', 14))
    label.pack(pady=20)

def show_gestao_pagamentos():
    clear_content_frame()
    label = Label(content_frame, text='Informações de Gestão de Pagamentos', font=('Arial', 14))
    label.pack(pady=20)

def show_avaliacao_alunos():
    clear_content_frame()
    label = Label(content_frame, text='Informações de Avaliação de Alunos', font=('Arial', 14))
    label.pack(pady=20)

def show_performance_alunos():
    clear_content_frame()
    label = Label(content_frame, text='Informações de Performance de Alunos', font=('Arial', 14))
    label.pack(pady=20)

def clear_content_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()

# Definir a aparência inicial da janela principal
root = Tk() # Cria uma instância da classe
root.title('Centro de formação') # Título da janela
root.geometry('1280x640+280+150') # Geometria da janela, especifica a largura, altura e posição inicial
root.resizable(0, 0) # Bloquea a capacidade de alterar o tamanho em largura e altura

# Define a fonte das letras exibidas na interface
FONT = ('Arial', 12)

# Cria um frame dentro da janela raiz, define a sua altura, largura, cor de fundo
# Empacota o frame no local padrão e expande para ocupar o espaço disponível
main_frame = Frame(root, width=1280, height=720, bg='#F5F5F5')
main_frame.pack(fill='both', expand=True)

# Cria um frame dentro do main_frame, define a sua altura, largura, cor de fundo
# Empacota o frame à esquerda e preenche verticalmente o espaço disponível
menu_frame = Frame(main_frame, bg='#383838', width=200, height=720)
menu_frame.pack(side='left', fill='y')

# Cria um frame dentro do content_frame, define a sua altura, largura, cor de fundo
# Empacota o frame à esquerda e expande para ocupar o espaço disponível
content_frame = Frame(main_frame, bg='white', width=1080, height=720)
content_frame.pack(side='left', fill='both', expand=True)

# Define um dictionary para o estilo dos botões
button_styles = {
    'bg': '#008080',
    'fg': 'white',
    'activebackground': '#4C4C4C',
    'activeforeground': 'white',
    'font': FONT,
    'borderwidth': 0,
    'highlightthickness': 0,
    'relief': 'flat',
    'cursor': 'hand2',
}

# Define vários botões a partir do dicionário button_styles
# Empacota-os com preenchimento vertical (pady=10) preenchimento horizontal (padx=20) e preenchimento horizontal completo (fill='x').

# O primeiro botão (button1) em particular Define a função main_users_def.criar_interface(content_frame)
# como o comando a ser executado quando o botão é clicado.
button1 = Button(menu_frame, text='Gestão de Utilizadores', **button_styles, command=lambda: main_users_def.criar_interface(content_frame))
button1.pack(pady=10, padx=20, fill='x')

button2 = Button(menu_frame, text='Gestão de Alunos', **button_styles)
button2.pack(pady=10, padx=20, fill='x')

button3 = Button(menu_frame, text='Gestão de Aulas e Horários', **button_styles)
button3.pack(pady=10, padx=20, fill='x')

button4 = Button(menu_frame, text='Gestão de Pagamentos', **button_styles)
button4.pack(pady=10, padx=20, fill='x')

button5 = Button(menu_frame, text='Avaliações de Alunos', **button_styles)
button5.pack(pady=10, padx=20, fill='x')

button6 = Button(menu_frame, text='Performance de Alunos', **button_styles)
button6.pack(pady=10, padx=20, fill='x')

# Inicia a loop do programa e exibe a janela
root.mainloop()