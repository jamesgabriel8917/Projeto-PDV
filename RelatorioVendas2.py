import tkinter as tk
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("BancoDados.db")
c = conn.cursor()

def RelatorioVendas():
    root = tk.Tk()
    root.geometry("600x450+135+192")
    root.title("""Relatório de Vendas""")
    root.config(bg='lightgray')

    # Label para os nomes
    id = tk.Label(root, text='ID    ', font='arial 10 bold', bg='lightgray')
    id.place(x=50, y=5)
    nome = tk.Label(root, text='VALOR', font='arial 10 bold', bg='lightgray')
    nome.place(x=150, y=5)
    precoCusto = tk.Label(root, text='Data Venda', font='arial 10 bold', bg='lightgray')
    precoCusto.place(x=300, y=5)

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
    lstProdutos1.place(x=100, y=30)

    # Pro preço de custo
    lstProdutos2 = tk.Listbox(root, font=('arial', 12), width=99, height=21)
    lstProdutos2.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lstProdutos.yview)
    lstProdutos2.place(x=300, y=30)

    scrollbar.place()

    lista = c.execute("SELECT * FROM vendas")

    listaFormatada = list(lista)
    ##print("Número de linhas: " + str(len(listaFormatada)))
    for linha in listaFormatada:
        # {6.2f} no lugar do {:6s}
        try:
            # aux = '{:_^10d}   {:_^30s}   {:_^15.2f}    {:_^20.2f}    {:_^20d}'\ Exemplo do prof
            #    .format(int(linha[0]),str(linha[1]), float(linha[2]), float(linha[3]), int(linha[4]))
            # lstProdutos.insert(END, aux)
            aux1 = '{:_>10d}'.format(int(linha[0]))
            aux2 = '{:_>7.2f}'.format(float(linha[1]))  # .upper()
            aux3 = '{:_>15}'.format(str(linha[2]))

            lstProdutos.insert(tk.END, aux1)
            lstProdutos1.insert(tk.END, aux2)
            lstProdutos2.insert(tk.END, aux3)

        except ValueError:
            print("Problema na conversão de valor")

    return

if __name__ == "__main__":
    root = tk.Tk()
    RelatorioVendas(root)
    root.mainloop()