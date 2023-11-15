#Chama biblioteca TKinter
from tkinter import *
from tkinter import ttk 

janela = Tk()

#Criando Classe para Funções da interface:
class Funcs():
    def limpar_tela(self):
        self.codigo_entry.delete(0, END)
        self.responsavel_entry.delete(0, END)
        self.tarefa_entry.delete(0, END)
        self.datainicio_entry.delete(0, END)
        self.datafim_entry.delete(0, END)


#criação de Classe com funções:
class applications(Funcs):
    def __init__(self): #Onde se irá executar todas as outras funções
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.entry_widgets()
        self.lista_frame2()
        janela.mainloop() #Deixa a janela em loop

    def tela(self): #Criar configurações da tela
        self.janela.title("Interface_principal") #Titulo Janela
        self.janela.config(background= '#2B4E69') #Configura o Background
        self.janela.minsize(width= 800, height= 530) #Define A Resolução minima que a janela irá abrir

        #self.janela.maxsize(width= 800, height= 530) #Define a resolução maxima que a janela irá abrir
        #self.janela.resizable(False, False) #Define se a Janela será expandida ou não
         
    def frames_da_tela(self): #Cria as janelas para separar cada coisa (É UMA DIV)
        self.frame_1 = Frame(self.janela, bd= 4, highlightbackground= '#7FB7E3', highlightthickness=3) #Configura a janela, background, bordam etc
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth= 0.96, relheight= 0.46) #relx/y = posição e relwidth/height = largura e altura.

        self.frame_2 = Frame(self.janela, bd= 4, highlightbackground= '#7FB7E3', highlightthickness=3)
        self.frame_2.place(relx= 0.02, rely=0.5, relwidth= 0.96, relheight= 0.46)

    def entry_widgets(self):
        #CREATE BUTTONS

        #Botão Buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar") #Cria um botão + Texto + Variável botão
        self.bt_buscar.place(relx= 0.2, rely=0.1, relwidth= 0.1, relheight=0.1)
        #Botão Limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", command=self.limpar_tela) #Cria um botão + Texto + Variável botão
        self.bt_limpar.place(relx= 0.31, rely=0.1, relwidth= 0.1, relheight=0.1)
        #Botão Novo
        self.bt_novo = Button(self.frame_1, text="Novo") #Cria um botão + Texto + Variável botão
        self.bt_novo.place(relx= 0.58, rely=0.1, relwidth= 0.1, relheight=0.1)
        #Botão Alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar") #Cria um botão + Texto + Variável botão
        self.bt_alterar.place(relx= 0.69, rely=0.1, relwidth= 0.1, relheight=0.1)
        #Botão Excluir
        self.bt_excluir = Button(self.frame_1, text="Excluir") #Cria um botão + Texto + Variável botão
        self.bt_excluir.place(relx= 0.8, rely=0.1, relwidth= 0.1, relheight=0.1)

        #CREATE ENTRYS AND LABELS

        #Código Label and Entry
        self.lb_codigo = Label(self.frame_1, text="Código")
        self.lb_codigo.place(relx= 0.03, rely= 0.01 , relwidth= 0.1, relheight= 0.1)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx= 0.035, rely=0.1, relwidth= 0.1, relheight=0.1)

        #Nome Tarefa Label and Entry
        self.lb_tarefa = Label(self.frame_1, text="Tarefa")
        self.lb_tarefa.place(relx= 0.011, rely= 0.25 , relwidth= 0.1, relheight= 0.1)

        self.tarefa_entry = Entry(self.frame_1)
        self.tarefa_entry.place(relx= 0.035, rely=0.36, relwidth= 0.6, relheight=0.1)

        #Nome Responsável Label and Entry
        self.lb_responsavel = Label(self.frame_1, text="Responsável")
        self.lb_responsavel.place(relx= 0.03, rely= 0.5 , relwidth= 0.1, relheight= 0.1)

        self.responsavel_entry = Entry(self.frame_1)
        self.responsavel_entry.place(relx= 0.035, rely=0.6, relwidth= 0.6, relheight=0.1)

        #Data de Inicio Label and Entry
        self.lb_datainicio = Label(self.frame_1, text="Data de início")
        self.lb_datainicio.place(relx= 0.17, rely= 0.73 , relwidth= 0.1, relheight= 0.1)

        self.datainicio_entry = Entry(self.frame_1)
        self.datainicio_entry.place(relx= 0.17, rely=0.83, relwidth= 0.1, relheight=0.1)

        #Data de Fim Label and Entry
        self.lb_datafim = Label(self.frame_1, text="Data Final")
        self.lb_datafim.place(relx= 0.35, rely= 0.73 , relwidth= 0.1, relheight= 0.1)

        self.datafim_entry = Entry(self.frame_1)
        self.datafim_entry.place(relx= 0.35, rely=0.83, relwidth= 0.1, relheight=0.1)

        #Tipo Label and Entry With list
        self.lb_tipo = Label(self.frame_1, text="Tipo")
        self.lb_tipo.place(relx= 0.69, rely= 0.36 , relwidth= 0.1, relheight= 0.1)

        self.tipolist = ["Projeto", "Trabalho", "Minitrabalho", "Tarefa", "Prova"] #Cria as opções da lista

        self.tipocb = ttk.Combobox(self.frame_1, values= self.tipolist) #Cria uma lista de seleção
        self.tipocb.place(relx=0.69, rely=0.48, relwidth=0.1, relheight=0.1)
        self.tipocb.set("Projeto")

        #Prioridade Label and Entry With list
        self.lb_prioridade = Label(self.frame_1, text="Prioridade")
        self.lb_prioridade.place(relx= 0.81, rely= 0.36 , relwidth= 0.1, relheight= 0.1)

        self.prioridadelist = ["Crucial", "Máxima", "Média", "Mínima"]

        self.prioridadecb = ttk.Combobox(self.frame_1, values= self.prioridadelist) #Cria uma lista de seleção
        self.prioridadecb.place(relx=0.81, rely=0.48, relwidth=0.1, relheight=0.1)
        self.prioridadecb.set("Crucial")

    def lista_frame2(self): #Criar a tabela na segunda janela

        self.listaCLi = ttk.Treeview(self.frame_2, height=3, columns=("col1, col2, col3, col4, col5")) #Numero de colunas a ser usada
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

        self.listaCLi.place(relx=0.01,rely=0.1,relwidth=0.95,relheight=0.85) #Poisção coluna

        self.scrollLista = Scrollbar(self.frame_2, orient='vertical') #Cria uma barra de rolagem 
        self.listaCLi.configure(yscroll=self.scrollLista.set) #Diz que esse Scroll é dessa lista
        self.scrollLista.place(relx=0.96,rely=0.1,relwidth=0.04,relheight=0.85)

        
applications()