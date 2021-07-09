# Tela onde o usuário fara as vendas, pode ser logado como o usuário ou o administrador

from tkinter import *
import sqlite3
import tkinter.messagebox
from datetime import datetime
import math
# from tkinter.scrolledtext import ScrolledText #Biblioteca para fazer barra de rolagem ainda não usada
import PDV2

# lista de IDs
lId = []
# lista de quantidades de produtos
lPd = []


def PDV():
    conn = sqlite3.connect("BancoDados.db")
    cursor = conn.cursor()

    # variavel para a data corrente
    date1 = datetime.now()
    date = date1.strftime('%d/%m /%y    %H:%M')

    # variaveis para salvar o produto da venda
    labels_list = []
    products_list = []
    products_price = []
    products_quantity = []
    products_id = []

    # pega o último id da tabela vendas
    ordem = cursor.execute("SELECT id FROM vendas")
    ordemServico = list(ordem)
    prt = ("0" + str(len(ordemServico)))
    print(prt)

    class Aplication:
        def __init__(self, master, *args, **kwargs):

            self.master = master

            # criação dos frames da direita e esquerda
            self.left = Frame(master, width=700, height=768, bg='white')
            self.left.pack(side=LEFT)

            self.right = Frame(master, width=666, height=768, bg='lightblue')
            self.right.pack(side=RIGHT)

            self.heading = Label(self.left, text="   Lanchonete Burguer Crazy DOG     ", font=('arial 30 bold'),
                                 bg='lightblue')
            self.heading.place(x=0, y=0)

            self.date_1 = Label(self.right, text="Data de Hoje : " + str(date), font=('arial 16 bold'), bg='lightblue')
            self.date_1.place(x=0, y=0)

            # nome que aparece no cupom da venda na tela
            self.tproduct = Label(self.right, text="Produto :", font=('arial 18 bold'), bg='lightblue', fg='white')
            self.tproduct.place(x=0, y=40)

            self.tquantity = Label(self.right, text="Quantidade :", font=('arial 18 bold'), bg='lightblue', fg='white')
            self.tquantity.place(x=300, y=40)

            self.tamount = Label(self.right, text="Valor:", font=('arial 18 bold'), bg='lightblue', fg='white')
            self.tamount.place(x=500, y=40)

            # criado label para armazenar o id da venda para puxar pro banco
            self.tid_venda = Label(self.right, text="" + str(prt), font=('arial 18 bold'), bg='lightblue')
            self.tid_venda.place(x=450, y=0)

            self.enterid = Label(self.left, text="Produto ID :", font=('arial 18 bold'), bg='white')
            self.enterid.place(x=0, y=80)

            self.enteride = Entry(self.left, width=25, bd="0", font='arial 18 bold', bg='lemonchiffon')
            self.enteride.place(x=190, y=80)
            self.enteride.focus()
            self.enteride.bind("<Return>", self.jx)

            self.seacher_btn = Button(self.left, text='Pesquisar', width=15, height=2, bg='royalblue', fg='white',
                                      command=self.jx)
            self.seacher_btn.place(x=400, y=120)

            self.productname = Label(self.left, text="", font=('arial 17 bold'), bg='white', fg='green')
            self.productname.place(x=0, y=250)

            self.pprice = Label(self.left, text="", font=('arial 17 bold'), bg='white', fg='green')
            self.pprice.place(x=0, y=290)

            self.total_1 = Label(self.right, text="Total Preço R$ : ", font=('arial 40 bold'), bg='lightblue',
                                 fg='red')  # fg='lightsalmon')
            self.total_1.place(x=0, y=600)

        def jx(self, *args, **kwargs):
            self.get_id = self.enteride.get()
            query = "SELECT * FROM cadastro WHERE id=?"

            result = conn.execute(query, (self.get_id,))
            for self.r in result:
                self.get_id = self.r[0]
                self.get_name = self.r[1]
                self.get_Custo = self.r[2]
                self.get_price = self.r[3]
                self.get_estoque = self.r[4]

            # grava o nome do produto com letra maiuscula
            self.nomeUper = '{:30s}'.format(str(self.get_name)).upper()
            self.productname.configure(text=self.nomeUper)

            self.productname.configure(text="NOME PRODUTO :  " + str(self.nomeUper))

            self.precoFor = '{:7.2f}'.format(float(self.get_price))
            self.pprice.configure(text="PREÇO : R$  " + str(self.precoFor))

            self.quantity_1 = Label(self.left, text="Quantidade", font=('arial 18 bold'), bg='white')
            self.quantity_1.place(x=0, y=370)

            self.quantity_e = Entry(self.left, width=25, bd="0", font='arial 18 bold', bg='lightgray')
            self.quantity_e.place(x=190, y=370)

            self.quantity_e.focus()
            self.quantity_e.bind("<Return>", self.Car)

            self.discunt_1 = Label(self.left, text="Desconto", font=('arial 18 bold'), bg='white')
            self.discunt_1.place(x=0, y=410)

            self.discunt_e = Entry(self.left, width=25, bd="0", font='arial 18 bold', bg='lightgray')
            self.discunt_e.place(x=190, y=410)
            self.discunt_e.insert(END, 0)

            self.add_to_cart_btn = Button(self.left, text='Carrinho', width=22, height=2, bg='royalblue', fg='white',
                                          command=self.Car)
            self.add_to_cart_btn.place(x=350, y=450)

            self.change_1 = Label(self.left, text="Total Pago", font=('arial 18 bold'), bg='white')
            self.change_1.place(x=0, y=550)

            self.change_e = Entry(self.left, width=25, bd="0", font='arial 18 bold', bg='bisque')
            self.change_e.place(x=190, y=550)
            self.change_e.bind("<Return>", self.change_func)

            self.change_btn = Button(self.left, text='Calcular Troco', width=22, height=2, bg='tomato', fg='white',
                                     command=self.change_func)
            self.change_btn.place(x=350, y=590)

            self.bill_btn = Button(self.left, text='Finalizar Venda', font='arial 12', command=self.salvarVenda,
                                   width=17, height=2, bg='yellow')
            self.bill_btn.place(x=350, y=640)

            self.sair_btn = Button(self.left, text='EXIT', font='arial 12 bold', command=self.exit, width=12, height=1,
                                   bg='purple', fg='white')
            self.sair_btn.place(x=550, y=640)

        # função que é invocada para jogar os dados na tela, cupom da venda
        def Car(self, *args, **kwargs):
            self.quantity_value = int(self.quantity_e.get())
            if self.quantity_value > int(self.get_estoque):
                tkinter.messagebox.showinfo("ERRO.!""Quantidade superior ao estoque.!")
            else:

                self.final_price = (float(self.quantity_value) * float(self.get_price)) - (float(self.discunt_e.get()))
                products_list.append(self.get_name)
                products_price.append(self.final_price)
                products_quantity.append(self.quantity_value)
                products_id.append(self.get_id)
                # adiciona o produto na lista
                lPd.append(self.quantity_value)
                lId.append(self.get_id)

                print('lista de ID atualizada: {0}'.format(lId))
                print('lista de quantidade atualizada {0}'.format(lPd))

                self.x_index = 0
                self.y_index = 80
                self.x_counter = 0  # ainda não usei, mas conta os itens vendidos

                for self.p in products_list:
                    self.tempname = Label(self.right, text=str(products_list[self.x_counter]), font='arial 15',
                                          bg='lightblue', fg='darkviolet')
                    self.tempname.place(x=0, y=self.y_index)
                    labels_list.append(self.tempname)

                    self.tempqt = Label(self.right, text="X " + str(products_quantity[self.x_counter]), font='arial 15',
                                        bg='lightblue', fg='darkviolet')
                    self.tempqt.place(x=400, y=self.y_index)
                    labels_list.append(self.tempqt)

                    self.tempprice = Label(self.right, text="R$ " + str(products_price[self.x_counter]),
                                           font='arial 15', bg='lightblue', fg='darkviolet')
                    self.tempprice.place(x=500, y=self.y_index)
                    labels_list.append(self.tempprice)

                    self.y_index += 40
                    self.x_counter += 1

                    self.total_1.configure(text="Total: R$ " + str(sum(products_price)))

                    self.quantity_1.place_forget()
                    self.quantity_e.place_forget()
                    self.discunt_1.place_forget()
                    self.discunt_e.place_forget()
                    self.productname.configure(text="")
                    self.pprice.configure(text="")
                    self.add_to_cart_btn.destroy()

                    self.enteride.focus()
                    self.enteride.delete(0, END)

        # função para fazer o troco do dinheiro da venda
        def change_func(self, *args, **kwargs):
            self.amount_given = float(self.change_e.get())
            self.our_total = float(sum(products_price))

            self.to_give = self.amount_given - self.our_total

            self.trocoFormatado = '{:7.2f}'.format(float(self.to_give))
            self.c_amount = Label(self.left, text="Troco : R$ " + str(self.trocoFormatado), font='arial 30 bold',
                                  bg='white', fg='red')
            self.c_amount.place(x=0, y=640)

        def exit(self):
            root.destroy()

        # Salva no BD o id da venda
        def salvarVenda(self):

            get_id_venda = str(prt)
            dataHora = str(date)
            valor_Venda = float(sum(products_price))
            sql = """INSERT INTO vendas(id, valor, dia) VALUES(?,?,?)"""
            cursor = conn.execute(sql, (get_id_venda, valor_Venda, dataHora))
            conn.commit()

            print(get_id_venda)
            print(valor_Venda)
            print(dataHora)
            self.baixaEstoque()
            lId.clear()
            lPd.clear()
            root.destroy()
            PDV2.PDV()

        def retornaQtd(self, idl):
            cursor.execute("SELECT estoque FROM cadastro WHERE id == (\"%s\");" % (idl))
            result = cursor.fetchall()
            print(result)
            result = int(result[0][0])
            print('id selecionado quantidade = ({0})'.format(result))
            return result

        def baixaEstoque(self):
            j = 0
            for i in lId:
                idL = int(i)
                # recupera a quantitdade do banco e decrementa de acordo com o id da lista
                try:
                    qtd = (self.retornaQtd(idL) - lPd[j])
                except:
                    print('[ERRO] lista de produtos fora do range')
                else:
                    print('[DENTRO DO RANGE] lista OK')

                cursor.execute("UPDATE cadastro SET estoque  = (\"%s\") WHERE id == (\"%s\") ;" % (qtd, idL))
                conn.commit()
                j = j+1
                print('baixa id:{0} baixado em estoque: {1}un OK'.format(i, j))

    root = Tk()

    d = Aplication(root)

    root.geometry("1350x690+0+2")
    root.title("SISTEMA  DE  VENDAS")
    root.configure(background='orange')

    root.mainloop()


"""
    return

if __name__ == "__main__":
    root = tk.Tk()
    PDV(root)
    root.mainloop()
"""
