from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import Image, ImageTk

from tkcalendar import Calendar, DateEntry
from datetime import date

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

#criando a janela
janela = Tk()
janela.title('')
janela.geometry('870x535')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Criando Frames

frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


frame_formulario = Frame(janela, width=800, height=200, bg=co1, relief=RAISED)
frame_formulario.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=200, bg=co1, relief=RAISED)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

global imagem, imagem_string, l_imagem

#Criando o logo ---------------------------------------------------------------
app_lg = Image.open('static/logo.png')
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Sistema de Registro de Alunos", width=850, compound=LEFT, anchor=NW, font=('Vendana 15 bold'), bg=co6, fg=co1)
app_logo.place(x=5, y=0)

imagem = Image.open('static/logo.png')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_formulario, image=imagem, bg=co1, fg=co4)
l_imagem.place(x=500, y=10)

# Criando os inputs -----------------------------------------------------------
l_nome = Label(frame_formulario, text="Nome *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_formulario, width=30, justify='left', font=('Ivy 10'), relief="solid")
e_nome.place(x=7, y=40)

l_email = Label(frame_formulario, text="E-mail *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_formulario, width=30, justify='left', font=('Ivy 10'), relief="solid")
e_email.place(x=7, y=100)

l_telefone = Label(frame_formulario, text="Telefone *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_telefone.place(x=4, y=130)
e_telefone = Entry(frame_formulario, width=15, justify='left', font=('Ivy 10'), relief="solid")
e_telefone.place(x=7, y=160)

l_sexo = Label(frame_formulario, text="Sexo *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_sexo.place(x=127, y=130)
c_sexo = Combobox(frame_formulario, width=7, font=('Ivy 8 bold'), justify='center')
c_sexo['values'] = ('M', 'F')
c_sexo.place(x=130, y=160)

l_nascimento = Label(frame_formulario, text="Data de nascimento *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nascimento.place(x=240, y=10)
e_nascimento = DateEntry(
    frame_formulario, 
    width=18, 
    justify='center', 
    background="darkblue", 
    foreground='white', 
    borderwidth=2,
    year=2025)
e_nascimento.place(x=240, y=40)

l_endereco = Label(frame_formulario, text="Endereço *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_endereco.place(x=240, y=70)
e_endereco = Entry(frame_formulario, width=30, justify='left', font=('Ivy 10'), relief="solid")
e_endereco.place(x=240, y=100)

l_curso = Label(frame_formulario, text="Curso *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_curso.place(x=240, y=130)
c_curso = Combobox(frame_formulario, width=30, font=('Ivy 8 bold'), justify='left')
c_curso['values'] = ('Informática', 'Administração', 'Contabilidade', 'Gastronomia', 'Logística', 'Marketing', 'Recursos Humanos', 'Turismo')
c_curso.place(x=240, y=160)

# Função para escolher a imagem -------------------------------------------------
def escolher_imagem():
    global imagem, imagem_string, l_imagem
    imagem = fd.askopenfilename(title='Selecione uma imagem', filetypes=(('Arquivos PNG', '*.png'), ('Todos os arquivos', '*.*')))
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_formulario, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=500, y=10)

botao_carregar = Button(frame_formulario, command=escolher_imagem, text='Carregar Foto', width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_carregar.place(x=500, y=160)

botao_carregar['text'] = 'Trocar foto'

# Tabela de listagem de alunos -----------------------------------------------
def mostrar_alunos():
    
    list_headers = ('ID', 'Nome', 'E-mail', 'Telefone', 'Sexo', 'Nascimento', 'Endereço', 'Curso')

    # visualizar alunos
    df_list = []

    tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_headers, show='headings')

    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)
    
    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(row=1, column=0, sticky='nsew')
    vsb.grid(row=1, column=1, sticky='ns')
    hsb.grid(row=2, column=0, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=12)
    
    hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
    h = [40, 150, 150, 70, 70, 100, 140, 100]
    n = 0
    for col in list_headers:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        tree_aluno.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)

# Criando o procuar aluno -----------------------------------------------------
frame_procurar = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

l_nome = Label(frame_procurar, text="Procurar aluno [por Id]", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

e_procurar = Entry(frame_procurar, width=5, justify='left', font=('Ivy 10'), relief="solid")
e_procurar.grid(row=1, column=0, padx=0, pady=10, sticky=NSEW)

botao_procurar = Button(frame_procurar, text='Procurar', width=9, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_procurar.grid(row=1, column=1, padx=0, pady=10, sticky=NSEW)

# Botões de ações ------------------------------------------------------------
app_img_adicionar = Image.open('static/add.png')
app_img_adicionar = app_img_adicionar.resize((20, 20))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_botoes, image=app_img_adicionar,  relief=GROOVE, text=' Adicionar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)

app_img_atualizar = Image.open('static/update.png')
app_img_atualizar = app_img_atualizar.resize((20, 20))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_botoes, image=app_img_atualizar, relief=GROOVE, text=' Atualizar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_atualizar.grid(row=2, column=0, padx=10, pady=5, sticky=NSEW)

app_img_deletar = Image.open('static/delete.png')
app_img_deletar = app_img_deletar.resize((20, 20))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
app_deletar = Button(frame_botoes, image=app_img_deletar, relief=GROOVE, text=' Deletar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_deletar.grid(row=3, column=0, padx=10, pady=5, sticky=NSEW)

# Linha separatoria ----------------------------------------------------------
l_linha = Label(frame_botoes, relief=GROOVE, text='h', width=1, height=123, anchor=NW, font=('Ivy 1'), bg=co0, fg=co1)
l_linha.place(x=240, y=15)

#chamar a tabela
mostrar_alunos()


janela.mainloop()