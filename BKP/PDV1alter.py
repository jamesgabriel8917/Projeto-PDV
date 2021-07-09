import tkinter
from tkinter import *
import sqlite3
import datetime
import math

conn = sqlite3.connect("BancoDados.db")
cursor = conn.cursor()

# acrescentei dia 20-05
products_list = []
products_price = []
products_quantity = []
products_id = []
get_precoFinal = []


class telaPdv:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        #Frame da esquerda
        self.Tops = Frame(master, width=530, height=680, bd=5, relief="raise")
        self.Tops.place(x=10, y=10)

        self.TopsRisco = Label(self.Tops, text="-------------------------------------", font=('arial 30'), fg='gray65')
        self.TopsRisco.place(x=0, y=10)

        # Por a data no frame da esquerda
        self.date = datetime.datetime.now().date()

        self.date1 = Label(self.Tops, text='DATA de HOJE  : ' + str(self.date), font='arial 10')
        self.date1.place(x=5, y=5)

        #Por nomes fixo no frame da venda
        self.resh = Label(self.Tops, text='#', font='arial 10')
        self.resh.place(x=10, y=50)

        self.IdVenda = Label(self.Tops, text='Cód ', font='arial 10')
        self.IdVenda.place(x=55, y=50)

        self.NomeProduto = Label(self.Tops, text='Descrição  ', font='arial 10')
        self.NomeProduto.place(x=120, y=50)

        self.qtd = Label(self.Tops, text='Qtd  Un', font='arial 10')
        self.qtd.place(x=250, y=50)

        self.PrecoU = Label(self.Tops, text='VL Unit.', font='arial 10')
        self.PrecoU.place(x=310, y=50)

        self.PrecoT = Label(self.Tops, text='VL Total.', font='arial 10')
        self.PrecoT.place(x=400, y=50)


        #Frame da Direita superior
        self.TopsDireitaSuperior = Frame(master, width=370, height=200, bd=5, relief="raise")
        self.TopsDireitaSuperior.place(x=960, y=10)

        #Frame da Direita Meio
        self.TopsDireitaMeio = Frame(master, width=370, height=259, bd=5, relief="raise")
        self.TopsDireitaMeio.place(x=960, y=220)

        #Frame da Direita de Baixo
        TopsDireitaBaixo = Frame(master, width=370, height=200, bd=5, relief="raise")
        TopsDireitaBaixo.place(x=960, y=490)

        #Label caixa direita de Baixo
        self.procurarItem = Label(TopsDireitaBaixo, text='F3 - Procurar Itens', font='arial 15 bold')
        self.procurarItem.place(x=5, y=10)
        self.cancelarItem = Label(TopsDireitaBaixo, text='F4 - Cancelar Item Vendido', font='arial 15 bold')
        self.cancelarItem.place(x=5, y=40)
        self.cancelarVendaAtual = Label(TopsDireitaBaixo, text='F5 - Cancelar Venda Atual', font='arial 15 bold')
        self.cancelarVendaAtual.place(x=5, y=70)
        self.esc = Label(TopsDireitaBaixo, text='ESC - Limpa', font='arial 15 bold')
        self.esc.place(x=5, y=110)
        
        self.total_1 = Label(self.TopsDireitaSuperior, text='Total', font='arial 40 bold')
        self.total_1.place(x=50, y=50)



        #Entry para o frame do meio Entrar codigo barras ou Id
        self.entrada = Entry(self.TopsDireitaMeio, width=15, font='arial 20 bold', bg='lime green', fg='white')
        self.entrada.place(x=10, y=10)
        self.entrada.bind("<Return>", self.quantify)
        self.entrada.focus()

        #Botão sair da tela de pdv
        self.botaoSair = Button(TopsDireitaBaixo, text='SAIR', font=('arial 10 bold'), width=10, height=1, bg='blue',
                            fg='white', command=self.exit)
        self.botaoSair.place(x=250, y=150)
        self.botaoSair.bind("<Return>", self.exit)

        #Botão para os item ckicaveis
        #self.n1 = Button(master, text='XIS-SALADA', font=('arial 10 bold'), width=20, height=2, bg='red', fg='white')
        #conteudo = 'xxx'
        #self.n1.configure(text=conteudo)
        #self.n1.place(x=550, y=50)

        #self.n2 = Button(master, text='XIS-BACON', font=('arial 10 bold'), width=20, height=2, bg='red', fg='white')
        #self.n2.place(x=750, y=50)

        #self.n3 = Button(master, text='BATATA-FRITA', font=('arial 10 bold'), width=20, height=2, bg='red', fg='white')
        #self.n3.place(x=550, y=110)



            # Iniciando as Funções

    linha1=75 # Variavel criada para pular a linha no recibo da venda, no final do for ele pula + 25 linhas
    linha2=95
    count = 1
    multi = 1
    def pegarItVendido(self, *args, **kwargs):
        self.get_id = self.entrada.get()
        query = "SELECT * FROM cadastro WHERE id=?"
        result = cursor.execute(query, (self.get_id, ))


       # get_precoFinal = []
        for self.r in result:
            self.get_resh = self.count
            self.get_id = self.r[0]
            self.get_nome = self.r[1]
            self.get_multi = self.multi
            self.get_precoVenda = self.r[3]
           # self.get_precoFinal = 0


            # Criando as variaveis
            # posicionando cada variavel dentro do Frame
            self.resh_n = Label(self.Tops, text='', font='arial 12 bold ', fg='black')
            self.resh_n.place(x=2, y=self.linha1)

            self.produtoNome = Label(self.Tops, text='', font='arial 12 bold', fg='black')
            self.produtoNome.place(x=50, y=self.linha1)

            self.id_da_Venda = Label(self.Tops, text='', font='arial 12 bold', fg='blue')
            self.id_da_Venda.place(x=70, y=self.linha2)

            self.xis = Label(self.Tops, text='X', font='arial 12 bold', fg='blue')
            self.xis.place(x=270, y=self.linha2)

            self.multipli = Label(self.Tops, text='', font='arial 12 bold', fg='blue')
            self.multipli.place(x=28, y=self.linha2)#####################

            self.produtoPrecoVenda = Label(self.Tops, text='', font='arial 12 bold', fg='blue')
            self.produtoPrecoVenda.place(x=300, y=self.linha2)

            #self.preco_final = Label(self.Tops, text='', font='arial 12 bold', fg='blue')
            #self.preco_final.place(x=400, y=self.linha2)
            get_precoFinal = Label(self.Tops, text='', font='arial 12 bold', fg='black')
            get_precoFinal.place(x=400, y=self.linha2)


            self.total = Label(self.TopsDireitaSuperior , font='arial 40 bold', fg='blue')
            self.total.place(x=5, y=5)

            self.linha1 += 50
            self.linha2 += 50
            self.count += 1

# tambem em 20-05
        
        self.r_n = '{:0>3d}'.format(int(self.get_resh))
        self.resh_n.configure(text=" + " +self.r_n)

        self.idV = '{:0>13d}'.format(int(self.get_id))
        self.id_da_Venda.configure(text=self.idV)

        self.pN = '{:<30s}'.format(str(self.get_nome)).upper()
        self.produtoNome.configure(text=self.pN)

        self.pV = '{:>7.2f}'.format(float(self.get_precoVenda))
        self.produtoPrecoVenda.configure(text=self.pV)# + str(self.get_precoVenda))

        self.pF = '{:7.2f}'.format(float(self.multi) * (self.get_precoVenda))
        #self.preco_final.configure(text=self.pF)
        get_precoFinal.configure(text=self.pF)


        #self.total2 = '{:7.2f}'.format
        #self.total2 = '{:7.2f}'.format(float(self.somarItens()))
        self.total.configure(text="Total : " + str(sum(get_precoFinal)))

        self.multi += 1

    # pega a quantidade de produtos para multiplicar
    def quantify(self, *args):
        # Entrada de quantos itens
        self.quantity_e = 0
        self.quantity_e = Entry(self.TopsDireitaMeio, text='', width=3, font='arial 40 bold', bg='lightblue', fg='purple')
        self.quantity_e.place(x=10, y=90)
        self.quantity_e.bind("<Return>", self.pegarItVendido)
        self.quantity_e.focus()
        # self.quantity_e.insert(END, 1)

        self.quantity = Label(self.TopsDireitaMeio, text='Quantidade', font='arial 15 bold', fg='black')
        self.quantity.place(x=10, y=180)
        return self.quantity_e

    def somarItens(self, *args):
        self.a = 0
        self.b = float(self.a) + float(self.pF)

        print(self.b)
        return self.b




    def limpar(self, *args, **kwargs):
        self.entrada.delete(0, END)

    def exit(self, *args, **kwargs):
        self.master.destroy()




root = Tk()

d = telaPdv(root)

root.geometry("1350x750+0+0")
root.title("SISTEMA  DE  VENDAS")
root.configure(background='orange')

root.mainloop()