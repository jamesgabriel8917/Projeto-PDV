import tkinter as tk
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect("BancoDados.db")
c = conn.cursor()


def Alterar():
    root = tk.Tk()
    root.geometry("700x450+135+192")
    root.title("""ATUALIZAR PRODUSTOS""")
    root.config(bg='lightblue')

    def exit():
        root.destroy()

    def clear_all():
        #id_leb.delete(0, tk.END)
        id_e.delete(0, tk.END)
        nome_e.delete(0, tk.END)
        precoCusto_e.delete(0, tk.END)
        precoVenda_e.delete(0, tk.END)
        estoque_e.delete(0, tk.END)


    # faz a buscar no B.D.
    def search():
        sql = "SELECT * FROM cadastro WHERE id=?"
        result = c.execute(sql, (id_e.get(),))
        for r in result:
            n1 = r[1]
            n2 = r[2]
            n3 = r[3]
            n4 = r[4]
            # self.n5 = r[5]
        conn.commit()

        # limpa o campo antes de começar a imprimir os dados do id solicitado
        nome_e.delete(0, tk.END)
        nome_e.insert(0, str(n1))

        precoCusto_e.delete(0, tk.END)
        precoCusto_e.insert(0, str(n2))

        precoVenda_e.delete(0, tk.END)
        precoVenda_e.insert(0, str(n3))

        estoque_e.delete(0, tk.END)
        estoque_e.insert(0, str(n4))

    # para excluir o produto pelo id desejado
    def excluir():
        query2 = "DELETE  FROM cadastro WHERE id=?"
        result = c.execute(query2, (id_e.get(),))
        for r in result:
            n1 = r[1]
            n2 = r[2]
            n3 = r[3]
            n4 = r[4]
            conn.commit()

        # Criando função para pegar os gets, fazendo o Update

    def update():
        up1 = nome_e.get()
        up2 = precoCusto_e.get()
        up3 = precoVenda_e.get()
        up4 = estoque_e.get()

        query = "UPDATE cadastro SET nome=?, precoCusto=?, precoVenda=?, estoque=? WHERE id=?"
        c.execute(query, (up1, up2, up3, up4, id_e.get()))
        conn.commit()

        tkinter.messagebox.showinfo("Burgueria Carzy Dog", "Atualizado com Sucesso!!")

    # Label para os nomes
    id = tk.Label(root, text='ID', font='arial 15 bold')
    id.place(x=5, y=50)
    nome = tk.Label(root, text='NOME', font='arial 15 bold')
    nome.place(x=5, y=100)
    precoCusto = tk.Label(root, text='Preço de Custo', font='arial 15 bold')
    precoCusto.place(x=5, y=150)
    precoVenda = tk.Label(root, text='Preço de Venda', font='arial 15 bold')
    precoVenda.place(x=5, y=200)
    estoque = tk.Label(root, text='Estoque', font='arial 15 bold')
    estoque.place(x=5, y=250)

    # Entry para os labels
    id_e = tk.Entry(root, width=10, font='arial 15 bold')
    id_e.place(x=200, y=50)

    nome_e = tk.Entry(root, width=35, font='arial 15 bold')
    nome_e.place(x=200, y=100)

    precoCusto_e = tk.Entry(root, width=10, font='arial 15 bold')
    precoCusto_e.place(x=200, y=150)

    precoVenda_e = tk.Entry(root, width=10, font='arial 15 bold')
    precoVenda_e.place(x=200, y=200)

    estoque_e = tk.Entry(root, width=10, font='arial 15 bold')
    estoque_e.place(x=200, y=250)

    # criar o botar para pegar o get da senha
    pesquisar = tk.Button(root, text='PESQUISAR', font=('arial 10 bold'), width=10, height=1, bg='orange',
                            fg='black', command=search)
    pesquisar.place(x=330, y=50)

    atualizar = tk.Button(root, text="ATUALIZAR", font=('arial 10 bold'), width=10, height=2, bg='green',
                            fg='white', command=update)
    atualizar.place(x=5, y=300)

    limpar = tk.Button(root, text="LIMPAR", font=('arial 10 bold'), width=10, height=2, bg='green',
                         fg='white', command=clear_all)
    limpar.place(x=110, y=300)

    deletar = tk.Button(root, text="EXCLUIR", font=('arial 10 bold'), width=10, height=2, bg='red',
                          fg='white', command=excluir)
    deletar.place(x=220, y=300)

    sair = tk.Button(root, text='FECHAR/SAIR', font=('arial 10 bold'), width=12, height=2, bg='green',
                       fg='white', command=exit)
    sair.place(x=320, y=300)





if __name__ == "__main__":
    root = tk.Tk()
    Alterar(root)
    root.mainloop()