from tkinter import *
import Cadastro2
import Relatorio2
import PDV2

def call_Cadastro():
    Cadastro2.Cadastro()
    return

def call_Relatorio():
    Relatorio2.Relatorio()
    return

def call_PDV():
    PDV2.PDV()
    return



# Janela principal
def winPrincipal():
    root = Tk()
    root.geometry("1366x768+0+0")
    root.title(
        """Logado como administrador - Lanchonete BURGUER CRAZY DOG  -   Verção 1.00 -                      data da verção 20/03/20 -  vencimento certificado  19/03/2021""")
    root.config(bg='orange')

    #def call_Exit():
    #    root.destroy()
    #    return

        # Frame do topo
    Tops = Frame(root, width=1350, height=100, bd=9, relief="raise")
    Tops.pack(side=TOP)

    # Frame onde ficarão os botões
    FrameBotao = Frame(root, width=100, height=300, background="blue")
    FrameBotao.pack(side=TOP)

    # Titulo do frame do topo
    lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Burguer Crazy Dog", bd=8, width=32)
    lblInfo.grid(row=0, column=0)


    # Criando botão para CADASTRO e Relatorio e Entrar PDV
    cadastroBotao = Button(FrameBotao, padx=30, pady=1, bg='black', bd=4, fg='green', font=('arial', 12, 'bold',), width=5,
                                text=" CADASTRO ", command=call_Cadastro).grid(row=0, column=0)
    relatorioBotao = Button(FrameBotao, padx=30, pady=1, bg='black', bd=4, fg='green', font=('arial', 12, 'bold'),width=5,
                                 text=" RELATORIO ", command=call_Relatorio).grid(row=0, column=30)
    pdvBotao = Button(FrameBotao, padx=30, pady=1, bg='black', bd=4, fg='green', font=('arial', 12, 'bold'), width=5,
                           text=" PDV ", command=call_PDV).grid(row=0, column=120)
    sair = Button(FrameBotao, padx=30, pady=1, bg='black', bd=4, fg='green', font=('arial', 12, 'bold'), width=5,
                     text=" SAIR ", command=exit).grid(row=0, column=190)

if __name__ == "__main__":
    root = Tk()
    winPrincipal(root)
    root.mainloop()