import tkinter as tk
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect("BancoDados.db")
c = conn.cursor()

def Cadastro():
    root = tk.Tk()
    root.geometry("700x450+135+192")
    root.title("""Cadastrar Produtos""")
    root.config(bg='lightblue')

    def exit():
        root.destroy()

    def get_Cadastro():
        id = id_e.get()
        nome = nome_e.get()
        precoCu = precoCusto_e.get()
        precoVe = precoVenda_e.get()
        estoque = estoque_e.get()

        # aqui grava no BD já com o nome em Maiusculo
        nomeMaiu = '{:30s}'.format(str(nome)).upper()
        precoCusto = '{:7.2f}'.format(float(precoCu))
        precoVenda = '{:7.2f}'.format(float(precoVe))

        if id == '' or nome == '' or precoCu == '' or precoVe == '':
            tkinter.messagebox.showinfo("ATENÇÃO!!!", "Preencher todos os campos!!!!")
        else:
            sql = """INSERT INTO cadastro(id, nome, precoCusto, precoVenda, estoque) VALUES (?,?,?,?,?)"""
            c.execute(sql, (id, nomeMaiu, precoCusto, precoVenda, estoque))
            conn.commit()

    def alterar():
        sql = "SELECT * FROM cadastro WHERE id=?"
        result = c.execute(sql, (id_e.get(),))
        for r in result:
            n2 = r[2]
            n3 = r[3]
            n4 = r[4]
            n5 = r[5]
        conn.commit()
        nome_e.insert(0, str(n2))

    def clear_all():
        # self.id_e.delete(0, END)
        nome_e.delete(0, tk.END)
        precoCusto_e.delete(0, tk.END)
        precoVenda_e.delete(0, tk.END)
        estoque_e.delete(0, tk.END)


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
    limpar = tk.Button(root, text="LIMPAR", font=('arial 10 bold'), width=10, height=2, bg='green',
                         fg='white', command=clear_all)
    limpar.place(x=110, y=300)

    salvar = tk.Button(root, text="SALVAR", font=('arial 10 bold'), width=10, height=2, bg='green',
                         fg='white', command=get_Cadastro)
    salvar.place(x=220, y=300)

    sair = tk.Button(root, text='FECHAR/SAIR', font=('arial 10 bold'), width=12, height=2, bg='green',
                       fg='white', command=exit)
    sair.place(x=330, y=300)





if __name__ == "__main__":
    root = tk.Tk()
    Cadastro(root)
    root.mainloop()