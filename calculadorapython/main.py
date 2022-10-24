from tkinter import ttk
from tkinter import *

#cores

cor1 = "#3b3b3b" #preta
cor2 = "#feffff" #branca
cor3 = "#38576b" #azul carregado
cor3 = "#38576b" #azul carregado
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #laranja

janela = Tk()
janela.geometry('235x310')
janela.title('Calculadora')
janela.config(bg = cor1)
janela.resizable(width=False, height=False)
janela.iconphoto(False, PhotoImage(file='s-l300.png'))


#Divindo em 2 partes
frame_display = Frame(janela, width = 235, height = 50, bg = cor1)
frame_display.grid(row = 0, column = 0)

frame_corpo = Frame(janela, width = 235, height = 268)
frame_corpo.grid(row = 1, column = 0)

resultado = ""
def sete():
    global resultado
    resultado = resultado + "7"
    visor['text'] = resultado

def oito():
    global resultado
    resultado = resultado + "8"
    visor['text'] = resultado

def nove():
    global resultado
    resultado = resultado + "9"
    visor['text'] = resultado

def seis():
    global resultado
    resultado = resultado + "6"
    visor['text'] = resultado

def cinco():
    global resultado
    resultado = resultado + "5"
    visor['text'] = resultado

def quatro():
    global resultado
    resultado = resultado + "4"
    visor['text'] = resultado

def tres():
    global resultado
    resultado = resultado + "3"
    visor['text'] = resultado

def dois():
    global resultado
    resultado = resultado + "2"
    visor['text'] = resultado

def um():
    global resultado
    resultado = resultado + "1"
    visor['text'] = resultado

def zero():
    global resultado
    resultado = resultado + "0"
    visor['text'] = resultado

def ponto():
    global resultado
    try:
        if resultado[len(resultado) - 1] != ".":
            resultado = resultado + "."
            visor['text'] = resultado
    except:
            resultado = resultado
def limpar():
    global resultado
    resultado = ""
    visor['text'] = resultado

def divisor():
    global resultado
    try:
        if resultado[len(resultado) - 1] != "/":
            resultado = resultado + "/"
            visor['text'] = resultado
    except:
            resultado = resultado

def multiplicador():
    global resultado
    try:
        if resultado[len(resultado) - 1] != "*":
            resultado = resultado + "*"
            visor['text'] = resultado
    except:
            resultado = resultado

def somador():
    global resultado
    try:
        if resultado[len(resultado) - 1] != "+":
            resultado = resultado + "+"
            visor['text'] = resultado
    except:
            resultado = resultado

def subtrator():
    global resultado
    try:
        if resultado[len(resultado) - 1] != "-":
            resultado = resultado + "-"
            visor['text'] = resultado
    except:
            resultado = resultado

def porcentagemcalc():
    global resultado
    try:
        if resultado[len(resultado) - 1] != "%":
            resultado = resultado + "%"
            visor['text'] = resultado
    except:
            resultado = resultado

def resultador():
    global resultado
    try:
        resultado = str(eval(resultado))
        visor['text'] = resultado
    except:
        resultado = ""
        visor['text'] = "Operação Inválida, tente novamente"


#Botões
#Limpar
clear = Button(frame_corpo, text = "C", fg = cor1, bg = cor4, width=11, height=2, command=limpar, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
clear.place(x=0, y=0)

#Porcentagem
porcentagem = Button(frame_corpo, text = "%", fg = cor1, bg = cor4, width=5, height=2, command=porcentagemcalc, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
porcentagem.place(x=119, y=0)

#Divisão
divisao = Button(frame_corpo, text = "/", fg = cor2, bg = cor5, width=5, height=2, command=divisor, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
divisao.place(x=178, y=0)

#Multiplicação
multiplicacao = Button(frame_corpo, text = "*", fg = cor2, bg = cor5, width=5, height=2, command=multiplicador, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
multiplicacao.place(x=178, y=52)

#Subtração
subtracao = Button(frame_corpo, text = "-", fg = cor2, bg = cor5, width=5, height=2, command=subtrator, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
subtracao.place(x=178, y=104)

#Soma
soma = Button(frame_corpo, text = "+", fg = cor2, bg = cor5, width=5, height=2, command=somador, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
soma.place(x=178, y=156)

#Igual
igual = Button(frame_corpo, text = "=", fg = cor2, bg = cor5, width=5, height=2, command=resultador, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
igual.place(x=178, y=208)

#Números


n7 = Button(frame_corpo, text = "7", fg = cor1, bg = cor4, width=5, height=2, command=sete, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
n7.place(x=0, y=52)

n8 = Button(frame_corpo, text = "8", fg = cor1, bg = cor4, width=5, height=2, command=oito, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
n8.place(x=59, y=52)

n9 = Button(frame_corpo, text = "9", fg = cor1, bg = cor4, width=5, height=2, command=nove, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
n9.place(x=118, y=52)

n4 = Button(frame_corpo, text = "4", fg = cor1, bg = cor4, width=5, height=2, command=quatro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
n4.place(x=0, y=104)

n5 = Button(frame_corpo, text = "5", fg = cor1, bg = cor4, width=5, height=2, command=cinco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
n5.place(x=59, y=104)

n6 = Button(frame_corpo, text = "6", fg = cor1, bg = cor4, width=5, height=2, command=seis, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
n6.place(x=118, y=104)

n3 = Button(frame_corpo, text = "3", fg = cor1, bg = cor4, width=5, height=2, command=tres, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
n3.place(x=0, y=156)

n2 = Button(frame_corpo, text = "2", fg = cor1, bg = cor4, width=5, height=2, command=dois, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
n2.place(x=59, y=156)

n1 = Button(frame_corpo, text = "1", fg = cor1, bg = cor4, width=5, height=2, command=um, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
n1.place(x=118, y=156)

n0 = Button(frame_corpo, text = "0", fg = cor1, bg = cor4, width=11, height=2, command=zero, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
n0.place(x=0, y=208)

ponto = Button(frame_corpo, text = ".", fg = cor1, bg = cor4, width=5, height=2, command=ponto, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
ponto.place(x=118, y=208)

#Visor
visor = Label(frame_display, width = 15, height = 2, bg = cor1, fg="White", text = resultado, relief=FLAT, anchor='e', font=('Ivy 18 bold'))
visor.place(x = 0, y = 0)


janela.mainloop()