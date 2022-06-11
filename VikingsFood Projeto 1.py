from tkinter import *
import pygame
import time


janela = Tk()
janela.title("Programa Mateus")
janela.geometry("800x600+400+100")
janela.resizable(False,False)           ## CONFIGURANDO A JANELA PRINCIPAL
janela.iconbitmap('icone.ico')
img = PhotoImage(file = "BG11.png")
label_BG = Label(janela, image=img)


label_BG.place(x=0, y=0)                    ## Colocando background   


janela2 = Toplevel()                   ## CRIANDO AS DUAS JANELAS
janela2.title("Pedido")
img2 = PhotoImage(file = "BG22.png")
janela2.iconbitmap('icone.ico')
janela2.geometry("400x300+100+100")
label_BG2 = Label(janela2, image=img2)
label_BG2.place(relx=0.0,rely=0.0, relheight=1,relwidth=1)


entre1 = Entry(janela, width= 15)
entre1.place(x=47,y=110)                ## espaço para colocar o valor

pygame.mixer.init()

def Passar():                           
    #background='#de5900' 
    
    intvalor = entre1.get()             ## Metodo para enviar o valor para a outra janela
    valor = str(intvalor)
    label2_pedido = Label(janela2, text = valor, font=('Viking-Normal',115),foreground='white',background='#ff0000')
    label2_pedido.place(x=600, y=320)
    pygame.mixer.music.load("sino.mp3")
    pygame.mixer.music.play(loops=0)



def limpar():
                                        ##Metodo para limpar o valor enviado
    label2_pedido = Label(janela2, text = "      ", font=('Viking-Normal',180), bg='#de5900')
    label2_pedido.place(x=600, y=320)
    



enviar = Button(janela, text='Enviar',font='bold', command=Passar,bd=3,bg='#FFA500')
limpar = Button(janela, text='Limpar',font='bold', command=limpar,bd=3,bg='#FFA500')
enviar.place(x=47,y=140)
limpar.place(x=150,y=140)


janela.mainloop()
