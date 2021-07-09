import tkinter as tk
#import RelatorioMercadoria2
#import RelatorioVendas2
import RelatorioTabela
import RelatorioVendaTabela


def call_Vendas():
    #RelatorioVendas2.RelatorioVendas()
    RelatorioVendaTabela.RelatorioMercadorias()

def call_Mercadorias():
    #RelatorioMercadoria2.RelatorioMercadorias()
    RelatorioTabela.RelatorioMercadorias()

def Relatorio():
    Frame = tk.Tk()
    Frame.geometry("450x250+240+240")
    Frame.title("Qual sua Opção!")
    Frame.config(bg='purple')

    def ext():
        Frame.destroy()

    orientar = tk.Label(Frame, text='Que tipo de Relatório deseja !!!', font='arial 15 bold', bg='purple', fg='white')
    orientar.place(x=5, y=25)

    cad = tk.Button(Frame, text="Relatorio de MERCADORIA", font=('arial 10 bold'), width=23, height=2, bd=4, bg='green',
                      fg='white', command=call_Mercadorias)
    cad.place(x=25, y=100)

    alt = tk.Button(Frame, text="Relatorio de VENDAS", font=('arial 10 bold'), width=21, height=2, bd=4, bg='green',
                      fg='white', command=call_Vendas)
    alt.place(x=250, y=100)

    sair = tk.Button(Frame, text="FECHAR", font=('arial 8 bold'), width=12, height=2, bd=4, bg='orange', fg='black', command=ext)
    sair.place(x=170, y=200)



    #label = tk.Label(Frame, text="Olá eu vim da janela ")
    #label.pack(padx=20, pady=20)
    return


if __name__ == "__main__":
    root = tk.Tk()
    Relatorio(root)
    root.mainloop()