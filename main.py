from tkinter import *
from tkinter import ttk

#cores

cor1 = "#1e1f1e"  #preto
cor2 = "#feffff"   #branco
cor3 = "#38576b"   #azul
cor4 = "#ECEFF1"   #cinza
cor5 = "#FFAB40"   #laranja

#Configurando a Janela
janela = Tk()
janela.title('Calculadora')
janela.geometry("235x310")
janela.config(bg=cor1)


#Criando Frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)
frame_corpo = Frame(janela, width=235 , height=268, )
frame_corpo.grid(row=1, column=0)

todos_valores = ''
valor_texto = StringVar()

#criando função
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores) 
    valor_texto.set(str(resultado))
    limpar()
    entrar_valores(resultado)

def limpar():
    global todos_valores
    todos_valores = ''  
    valor_texto.set('')   


#criando label
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7,anchor="e",
                   relief=FLAT, justify=RIGHT, font=("Ivy 18"), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


#Criando os botões
#linha1
b1 = Button(frame_corpo, command=limpar, text="C", width=11, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frame_corpo,command=lambda:entrar_valores('%') , text="%", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b2.place(x=118, y=0)
b3 = Button(frame_corpo,command=lambda:entrar_valores('/') , text="/", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b3.place(x=177, y=0)

#linha2
b4 = Button(frame_corpo,command=lambda:entrar_valores('7') , text="7", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5 = Button(frame_corpo,command=lambda:entrar_valores('8') , text="8", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=52)
b6 = Button(frame_corpo, command=lambda:entrar_valores('9') ,text="9", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=52)
b7 = Button(frame_corpo, command=lambda:entrar_valores('*') ,text="*", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b7.place(x=177, y=52)

#linha3
b8 = Button(frame_corpo,command=lambda:entrar_valores('4') , text="4", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)
b9 = Button(frame_corpo, command=lambda:entrar_valores('5') ,text="5", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b9.place(x=59, y=104)
b10 = Button(frame_corpo,command=lambda:entrar_valores('6') , text="6", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b10.place(x=118, y=104)
b11 = Button(frame_corpo,command=lambda:entrar_valores('-') , text="-", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b11.place(x=177, y=104)

#linha4
b12 = Button(frame_corpo, text="3", command=lambda:entrar_valores('3') ,width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=156)
b13 = Button(frame_corpo, text="2",command=lambda:entrar_valores('2') , width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b13.place(x=59, y=156)
b14 = Button(frame_corpo, text="1",command=lambda:entrar_valores('1') , width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b14.place(x=118, y=156)
b15 = Button(frame_corpo, text="+", command=lambda:entrar_valores('+'), width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b15.place(x=177, y=156)
#linha5
b16 = Button(frame_corpo, text="0",command=lambda:entrar_valores('0') , width=11, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=208)
b17 = Button(frame_corpo, text=".",command=lambda:entrar_valores('.') , width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=208)
b17 = Button(frame_corpo, text="=",command=calcular , width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b17.place(x=177, y=208)


janela.mainloop()