#Chama biblioteca TKinter
from tkinter import *
from tkinter import ttk 
from tkcalendar import Calendar, DateEntry

janela = Tk()

class funcs():
    def calendario(self):
        self.calendario1 = Calendar(self.frame2, fg="gray75", bg= "blue")
        self.calendario1.place(r)

class applications(funcs):
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.entry_widgets()
        self.lista_frame2()
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
        self.lb_nome.place(relx= 0.225, rely= 0.23 , relwidth= 0.05, relheight= 0.25)
        

        self.entry_nome = Entry(self.frame1)
        self.entry_nome.place(relx=0.225,rely=0.55,relheight=0.33,relwidth=0.25)

        #Prioridade Label and Entry With list
        self.lb_prioridade = Label(self.frame1, text="Prioridade")
        self.lb_prioridade.place(relx= 0.48, rely= 0.23 , relwidth= 0.1, relheight= 0.2)

        self.prioridadelist = ["Crucial", "Máxima", "Média", "Mínima"]

        self.prioridadecb = ttk.Combobox(self.frame1, values= self.prioridadelist) #Cria uma lista de seleção
        self.prioridadecb.place(relx=0.49, rely=0.55, relwidth=0.1, relheight=0.3)
        self.prioridadecb.set("Crucial")

        #Tipo Label and Entry With list
        self.lb_tipo = Label(self.frame1, text="Tipo")
        self.lb_tipo.place(relx= 0.593, rely= 0.23 , relwidth= 0.1, relheight= 0.2)

        self.tipolist = ["Projeto", "Trabalho", "Minitrabalho", "Tarefa", "Prova"] #Cria as opções da lista

        self.tipocb = ttk.Combobox(self.frame1, values= self.tipolist) #Cria uma lista de seleção
        self.tipocb.place(relx=0.6, rely=0.55, relwidth=0.1, relheight=0.3)
        self.tipocb.set("Projeto")

        #Data entry and label calenda
        self.lb_data = Label(self.frame1, text="Data de início")
        self.lb_data.place(relx= 0.71 , rely= 0.24 , relwidth= 0.1, relheight= 0.2)

        self.data_entry = Entry(self.frame1)
        self.data_entry.place(relx= 0.71, rely=0.55, relwidth= 0.1, relheight=0.3)

    def lista_frame2(self): #Criar a tabela na segunda janela

        self.listaCLi = ttk.Treeview(self.frame2, height=3, columns=("col1, col2, col3, col4, col5")) #Numero de colunas a ser usada
        self.listaCLi.heading("#0", text="") #Nome das colunas
        self.listaCLi.heading("#1", text="Código")
        self.listaCLi.heading("#2", text="Responsável")
        self.listaCLi.heading("#3", text="Tarefa")
        self.listaCLi.heading("#4", text="Tipo")
        self.listaCLi.heading("#5", text="Prioridade")
        
        self.listaCLi.column("#0", width=1) #Largura de cada uma respectivamente
        self.listaCLi.column("#1", width=80)
        self.listaCLi.column("#2", width=130)
        self.listaCLi.column("#3", width=110)
        self.listaCLi.column("#4", width=130)
        self.listaCLi.column("#5", width=130)

        self.listaCLi.place(relx=0.01,rely=0.02,relwidth=0.95,relheight=0.98) #Poisção coluna

        self.scrollLista = Scrollbar(self.frame2, orient='vertical') #Cria uma barra de rolagem 
        self.listaCLi.configure(yscroll=self.scrollLista.set) #Diz que esse Scroll é dessa lista
        self.scrollLista.place(relx=0.96,rely=0.02,relwidth=0.04,relheight=0.95)




applications()


