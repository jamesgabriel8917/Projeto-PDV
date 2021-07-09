import tkinter as tk
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("BancoDados.db")
c = conn.cursor()

def RelatorioMercadorias():
    root = tk.Tk()
    root.geometry("900x450+135+192")
    root.title("""Relatório de Mercadorias""")
    root.config(bg='lightgray')

    # Label para os nomes
    id = tk.Label(root, text='ID                |', font='arial 10 bold', bg='lightgray')
    id.place(x=50, y=5)
    nome = tk.Label(root, text='NOME', font='arial 10 bold', bg='lightgray')
    nome.place(x=300, y=5)
    precoCusto = tk.Label(root, text='|    Preço Custo   |', font='arial 10 bold', bg='lightgray')
    precoCusto.place(x=585, y=5)
    precoVenda = tk.Label(root, text=' Preço Venda', font='arial 10 bold', bg='lightgray')
    precoVenda.place(x=700, y=5)
    estoque = tk.Label(root, text='|  Estoque', font='arial 10 bold', bg='lightgray')
    estoque.place(x=800, y=5)

    # Pro ID
    scrollbar = tk.Scrollbar(root)
    lstProdutos = tk.Listbox(root, font=('arial', 12), width=99, height=21)
    lstProdutos.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lstProdutos.yview)
    lstProdutos.place(x=1, y=30)

    # Pro Nome
    lstProdutos1 = tk.Listbox(root, font=('arial', 12), width=99, height=21)
    lstProdutos1.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lstProdutos.yview)
    lstProdutos1.place(x=130, y=30)

    # Pro preço de custo
    lstProdutos2 = tk.Listbox(root, font=('arial', 12), width=99, height=21)
    lstProdutos2.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lstProdutos.yview)
    lstProdutos2.place(x=590, y=30)

    # Pro preço de venda
    lstProdutos3 = tk.Listbox(root, font=('arial', 12), width=99, height=21)
    lstProdutos3.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lstProdutos.yview)
    lstProdutos3.place(x=700, y=30)

    # Pro quantidade
    lstProdutos4 = tk.Listbox(root, font=('arial', 12), width=99, height=21)
    lstProdutos4.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lstProdutos.yview)
    lstProdutos4.place(x=800, y=30)

    scrollbar.place()

    lista = c.execute("SELECT * FROM cadastro")

    listaFormatada = list(lista)
    print("Número de linhas: " + str(len(listaFormatada)))
    for linha in listaFormatada:
        # {6.2f} no lugar do {:6s}
        try:
            # aux = '{:_^10d}   {:_^30s}   {:_^15.2f}    {:_^20.2f}    {:_^20d}'\ Exemplo do prof
            #    .format(int(linha[0]),str(linha[1]), float(linha[2]), float(linha[3]), int(linha[4]))
            # lstProdutos.insert(END, aux)
            aux1 = '{:_>13d}'.format(int(linha[0]))
            aux2 = '{:_<55s}'.format(str(linha[1]))  # .upper()
            aux3 = '{:_>10.2f}'.format(float(linha[2]))
            aux4 = '{:_>10.2f}'.format(float(linha[3]))
            aux5 = '{:_>6d}'.format(int(linha[4]))

            lstProdutos.insert(tk.END, aux1)
            lstProdutos1.insert(tk.END, aux2)
            lstProdutos2.insert(tk.END, aux3)
            lstProdutos3.insert(tk.END, aux4)
            lstProdutos4.insert(tk.END, aux5)

        except ValueError:
            print("Problema na conversão de valor")

    return

if __name__ == "__main__":
    root = tk.Tk()
    RelatorioMercadorias(root)
    root.mainloop()