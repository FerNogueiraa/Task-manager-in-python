#Chama biblioteca TKinter
from tkinter import *
from tkinter import ttk 

janela = Tk()


class applications():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.entry_widgets()
        janela.mainloop() #coloca janela e loop

    def tela(self):
        self.janela.title("Interface_TreeView") #Titulo Janela
        self.janela.config(background= '#2B4E69') #Configura o Background
        self.janela.minsize(width= 800, height= 530) #Define A Resolução minima que a janela irá abrir

    def frames_da_tela(self):
        self.frame1 = Frame(self.janela, bd=4, highlightbackground= '#7FB7E3', highlightthickness=3)
        self.frame1.place(relx=0.02,rely=0.03,relwidth=0.96,relheight=0.15) 

        self.frame2 = Frame(self.janela, bd= 4, highlightbackground= '#7FB7E3', highlightthickness=3)
        self.frame2.place(relx=0.02,rely=0.2,relwidth=0.96,relheight=0.79)

    def entry_widgets(self):
        #Criando botões
        
        #Botão Buscarr
        self.bt_buscar = Button(self.frame1, text="Buscar") #Cria um botão + Texto + Variável botão
        self.bt_buscar.place(relx= 0.02, rely=0.2, relwidth= 0.2, relheight=0.7)

        #Label e Entry 
        self.lb_nome = Label(self.frame1, text="Nome")
        self.lb_nome.place(relx= 0.225, rely= 0.43 , relwidth= 0.05, relheight= 0.25)



applications()
