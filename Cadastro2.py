import tkinter as tk
import Cadastro_Produto3
import Alterar_Produto3

def call_Cadastrar():
    Cadastro_Produto3.Cadastro()

def call_Alterar():
    Alterar_Produto3.Alterar()



def Cadastro():
    root = tk.Tk()
    root.geometry("450x250+240+240")
    root.title("Qual sua Opção!")
    root.config(bg='purple')

    def ext():
        root.destroy()

    orientar = tk.Label(root, text='Escolha uma Opção para continuar !!', font='arial 15 bold', bg='purple', fg='white')
    orientar.place(x=5, y=25)

    cad = tk.Button(root, text="CADASTRAR", font=('arial 10 bold'), width=15, height=2, bd=4, bg='green',
                  fg='white', command=call_Cadastrar)
    cad.place(x=25, y=100)

    alt = tk.Button(root, text="ALTERAR", font=('arial 10 bold'), width=15, height=2, bd=4, bg='green',
                  fg='white', command=call_Alterar)
    alt.place(x=250, y=100)

    sair = tk.Button(root, text="FECHAR", font=('arial 8 bold'), width=12, height=2, bd=4, bg='orange',
                   fg='black', command=ext)
    sair.place(x=150, y=200)

    return


if __name__ == "__main__":
    root = tk.Tk()
    Cadastro(root)
    root.mainloop()