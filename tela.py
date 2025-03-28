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
janela.geometry('810x535')
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

# Criando os inputs -----------------------------------------------------------
l_nome = Label(frame_formulario, text="Nome *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_formulario, width=30, justify='left', font=('Ivy 10'))
e_nome.place(x=7, y=40)

l_email = Label(frame_formulario, text="E-mail *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_formulario, width=30, justify='left', font=('Ivy 10'))
e_email.place(x=7, y=100)

l_telefone = Label(frame_formulario, text="Telefone *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_telefone.place(x=4, y=130)
e_telefone = Entry(frame_formulario, width=15, justify='left', font=('Ivy 10'))
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
e_endereco = Entry(frame_formulario, width=30, justify='left', font=('Ivy 10'))
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


janela.mainloop()