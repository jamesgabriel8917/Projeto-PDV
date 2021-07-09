import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("BancoDados.db")
c = conn.cursor()

def RelatorioMercadorias():
    root = tk.Tk()
    root.geometry("1000x449+135+192")
    root.title("""Relatório de Mercadorias""")
    root.config(bg='lightgray')

    #label = tk.Label(root, text="Placar", font=("Arial",10)).grid(row=0, columnspan=3)

    # cria Treeview com 5 colunas
    cols = ('ID', 'NOME', 'PREÇO CUSTO', 'PREÇO VENDA', 'ESTOQUE')
    listBox = ttk.Treeview(root, columns=cols,  height=21, show='headings')

    # seta os cabeçalhos de cada coluna
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)

    tempList = c.execute("SELECT * FROM cadastro")
    listaformatada = list(tempList)
    for linha in listaformatada:
        aux1 = int(linha[0])
        aux2 = str(linha[1])  # .upper()
        aux3 = float(linha[2])
        aux4 = float(linha[3])
        aux5 = int(linha[4])

       # print(aux1, aux2, aux3, aux4, aux5)
        listBox.insert("", "end", values=(aux1, aux2, aux3, aux4, aux5))

    root.mainloop()

#RelatorioMercadorias()



#def show():

#	# cria uma quatro elementos para serem inseridos
#    tempList = [['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5']]

 #   # ordena a lista pelos pontos indice [1]
  #  tempList.sort(key=lambda e: e[1], reverse=True)


   # for i, (name, score) in enumerate(tempList, start=1):
    #    # imprime no console para testar os elementos a serem inseridos em uma linha
     #   print(i, name, score)

      #  # insere os 3 dados de uma linha
       # listBox.insert("", "end", values=(i, name, score))




#scores = tk.Tk()
#label = tk.Label(scores, text="Placar", font=("Arial",30)).grid(row=0, columnspan=3)

## cria Treeview com 3 colunas
#cols = ('Colocação', 'Nome', 'Pontuação')
#listBox = ttk.Treeview(scores, columns=cols, show='headings')

## seta os cabeçalhos de cada coluna
#for col in cols:
#    listBox.heading(col, text=col)
#listBox.grid(row=1, column=0, columnspan=2)

## Botões
#showScores = tk.Button(scores, text="Exibir Placar", width=15, command=RelatorioMercadorias).grid(row=4, column=0)
#closeButton = tk.Button(scores, text="Fechar", width=15, command=exit).grid(row=4, column=1)

#scores.mainloop()