from tkinter import *
from tkinter import messagebox
import subprocess
import sys
import os


class TelaLogin:

    def __init__(self):
        self.tela = Tk()
        self.tela.title("Acesso ao Sistema")
        self.tela.configure(background="#195c56")

        self.largura = 400
        self.altura = 200

        self.centralizar_tela()
        self.tela.resizable(False, False)

        self.criar_componentes()

        self.tela.mainloop()

    
    # CONFIGURAÇÃO DA TELA
    
    def centralizar_tela(self):
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        posx = largura_screen/2 - self.largura/2
        posy = altura_screen/2 - self.altura/2
        print(largura_screen, altura_screen)
        self.tela.geometry("%dx%d+%d+%d" % (self.largura,self.altura, posx,posy))
        self.tela.resizable(False,False)


 
    # COMPONENTES   
# Certifique-se de que está exatamente assim, com a indentação correta:
    def carregar_icones(self):
        diretorio = os.path.dirname(os.path.abspath(__file__))
        caminho_login = os.path.join(diretorio, "icones", "login.png")
        caminho_sair = os.path.join(diretorio, "icones", "exit.png")
        
        # O print PRECISA ficar aqui dentro, após as variáveis serem criadas
        print("Buscando login em:", caminho_login) 
        
        try:
            self.foto_acesso = PhotoImage(file=caminho_login)
            self.foto_sair = PhotoImage(file=caminho_sair)
        except Exception as e:
            print(f"Erro real ao carregar os ícones: {e}")
            self.foto_acesso = self.foto_sair = None
            
    def criar_componentes(self):
        Label(self.tela, text="Usuário").place(x=50, y=60)
        Label(self.tela, text="Senha").place(x=50, y=100)

        self.txt_usuario = Entry(self.tela, width=20)
        self.txt_usuario.place(x=100, y=60)

        self.txt_senha = Entry(self.tela, width=20, show="*")
        self.txt_senha.place(x=100, y=100)

        self.carregar_icones()
        self.criar_botoes()


    def criar_botoes(self):
        Button(self.tela,text="Acessar", image=self.foto_acesso,compound=TOP,command=self.validar_acesso).place(x=250, y=50)

        Button(self.tela,text="Sair",image=self.foto_sair,compound=TOP,command=self.sair).place(x=320, y=50)

    
    # FUNÇÕES
    def validar_acesso(self):
        usuario = self.txt_usuario.get()
        senha = self.txt_senha.get()

        if usuario == "admin" and senha == "123":
            self.abrir_menu()
        else:
            messagebox.showerror(
                "Erro de Login",
                "Usuário ou senha incorretos"
            )

    def abrir_menu(self):
        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        caminho_menu = os.path.join(diretorio_script, "Menu.py")
        
        self.tela.destroy()
        subprocess.run([sys.executable, caminho_menu])

    def sair(self):
        resposta = messagebox.askquestion(
            "Sair do Sistema?",
            "Você tem certeza que deseja sair?"
        )

        if resposta == "yes":
            self.tela.destroy()
    
    def executar(self):
        self.tela.mainloop()
