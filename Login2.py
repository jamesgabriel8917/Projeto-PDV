# Tudo começa aqui, tela de LOGIN

from tkinter import *
import sqlite3
import JanelaPrincipal
import PDV2

conn = sqlite3.connect("BancoDados.db")
c = conn.cursor()


class Logar:
    def __init__(self, master, *args, **kwargs):
        self.master = master

        self.heading = Label(master, text='LOGIN', font=('arial 40 bold'), fg='blue', bg='lightblue')
        self.heading.place(x=600, y=150)

        self.user = Label(master, text='Usuario :', font=('arial 20 bold'), bg='lightblue')
        self.user.place(x=350, y=300)

        self.senha = Label(master, text='SENHA: ', font=('arial 20 bold'), bg='lightblue')
        self.senha.place(x=350, y=350)

        self.frase = Label(master, text='Digite seu nome de Usuario   -  E sua Senha para Logar no Sistema',
                           font=('arial 15 bold'), fg='red', bg='lightblue')
        self.frase.place(x=300, y=500)

        # Criando campo para pegar os dados do usuarioa
        self.user_e = Entry(master, width=25, font=('arial 18 bold'))
        self.user_e.place(x=550, y=300)

        # Criando campo para pegar os dados da senha
        self.senha_e = Entry(master, width=25, font=('arial 18 bold'))
        self.senha_e.place(x=550, y=350)

        # criar o botar para pegar o get da senha
        self.botaoEntar = Button(master, text="ENTRAR", font=('arial 10 bold'), width=18, height=2, bg='green',
                                 fg='white', command=self.getSenha)
        self.botaoEntar.place(x=700, y=400)
        self.botaoEntar.bind("<Return>", self.getSenha)

        self.botaoSair = Button(master, text="SAIR", font=('arial 10 bold'), width=18, height=2, bg='orange',
                                fg='white', command=self.sairTelaLogin)
        self.botaoSair.place(x=500, y=400)
        self.botaoSair.bind("<Return>", self.sairTelaLogin)

    # criando método para pegar os gets da senha
    def getSenha(self, *args, **kwargs):
        self.userP1 = int(self.user_e.get())
        self.senhaP2 = int(self.senha_e.get())

        if self.userP1 == 15 & self.senhaP2 == 15:
            self.call_Janela()
        elif self.userP1 == 22 & self.senhaP2 == 22:
            self.call_PDV()
        else:
            self.fraseErro = Label(root, text='Senha Invalida', font=('arial 15 bold'), fg='black', bg='lightblue')
            self.fraseErro.place(x=600, y=250)

    # Destroi a tela
    def sairTelaLogin(self, *args, **kwargs):
        root.destroy()

    # Chama o programa ADMIM.py tela principal para o administrador
   # def chamarAdmim(self):
    #    root.destroy()
     #   from Admim import Administrador

    def call_Janela(self):
        root.destroy()
        JanelaPrincipal.winPrincipal()

    def call_PDV(self):
        root.destroy()
        PDV2.PDV()

    #def chamarPDV(self, *args, **kwargs):
     #   root.destroy()
      #  from PDV import Aplication


root = Tk()

b = Logar(root)

root.geometry("1366x768+0+0")
root.title("Fazer Login!!!!!")
root.config(bg='lightblue')

root.mainloop()
