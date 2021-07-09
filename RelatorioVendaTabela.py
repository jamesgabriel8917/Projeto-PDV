import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("BancoDados.db")
c = conn.cursor()

def RelatorioMercadorias():
    root = tk.Tk()
    root.geometry("600x450+135+192")
    root.title("""Relatório de Vendas""")
    root.config(bg='lightgray')

    # cria Treeview com 3 colunas
    cols = ('ID VENDA', 'VALOR', 'DATA')
    listBox = ttk.Treeview(root, columns=cols, height=21, show='headings')

    # seta os cabeçalhos de cada coluna
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)

    tempList = c.execute("SELECT * FROM vendas")
    listaformatada = list(tempList)
    for linha in listaformatada:
        aux1 = int(linha[0])
        aux2 = '{:>7.2f}'.format(float(linha[1]))
        aux3 = str(linha[2])

        #print(aux1, aux2, aux3)
        listBox.insert("", "end", values=(aux1, aux2, aux3))

    root.mainloop()
