import tkinter as tk
from tkinter import Menu, Label, Button, messagebox
import subprocess
import sys
import os

try:
    from PIL import Image, ImageTk
except:
    os.system(f'"{sys.executable}" -m pip install pillow')
    from PIL import Image, ImageTk


class TelaMenuSistema:

    def __init__(self):
        self.tela = tk.Tk()
        self.tela.title("TELA MENU HOSPITAL")

        self.largura = 1000
        self.altura = 700
        self.centralizar_tela()
        
        self.carregar_icones()
        self.carregar_imagem_fundo()
        self.criar_menu()
        self.criar_botoes()

        self.tela.mainloop()


    # CENTRALIZAR TELA   
    def centralizar_tela(self):
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        posx = largura_screen/2 - self.largura/2
        posy = altura_screen/2 - self.altura/2
        print(largura_screen, altura_screen)
        self.tela.geometry("%dx%d+%d+%d" % (self.largura,self.altura, posx,posy))
        self.tela.resizable(False,False)

 
    # IMAGEM FUNDO   
    def carregar_imagem_fundo(self):
        diretorio = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(diretorio, "icones", "escola.jpg")
        if os.path.exists(caminho):
            img = Image.open(caminho).resize((1000, 700))
            self.img_fundo_tk = ImageTk.PhotoImage(img)
            Label(self.tela, image=self.img_fundo_tk).place(x=0, y=0)


    # CRIAR MENU   
    def criar_menu(self):
        barra_menus = Menu(self.tela)
        opcoes_menus_arquivos = Menu(barra_menus)
        opçoes_menus_gestao = Menu(barra_menus)
        opcoes_novo = Menu(opcoes_menus_arquivos)

        barra_menus.add_cascade(label="Arquivo", menu=opcoes_menus_arquivos)
        opcoes_menus_arquivos.add_cascade(label="Novo", menu=opcoes_novo )

        opcoes_novo.add_command(label="Cadastrar")

        opcoes_menus_arquivos.add_command(label="Abrir")
        opcoes_menus_arquivos.add_command(label="Salvar")

        opcoes_menus_arquivos.add_separator()
        opcoes_menus_arquivos.add_command(label="Sair", command=self.tela.quit)

        barra_menus.add_cascade(label="Gestão", menu=opçoes_menus_gestao)
        opçoes_menus_gestao.add_command(label="Alunos", command=self.abrir_alunos)
        opçoes_menus_gestao.add_command(label="Professores",command=self.abrir_professores)
        opçoes_menus_gestao.add_command(label="Notas",command=self.abrir_notas)
        self.tela.config(menu=barra_menus)

    # ÍCONES
    def carregar_icones(self):
        self.ic_notas = self.carregar_png("consultar.png", 50, 50)
        self.ic_alunos= self.carregar_png("logo_usuarios.png", 50, 50)
        self.ic_professores = self.carregar_png("logo_servicos.png", 50, 50)
        self.ic_logout = self.carregar_png("logout.png", 50, 50)
        self.ic_sistema = self.carregar_png("logo.png", 40, 40)

    def carregar_png(self, caminho, largura, altura):
        if os.path.exists(caminho):
            img = Image.open(caminho)
            img = img.resize((largura, altura))
            return ImageTk.PhotoImage(img)
        return None


    # BOTÕES   
    def criar_botoes(self):
        estilo = {"bg": "white", "compound": "top", "relief": "flat", "pady": 5}
        Button(self.tela, text="Notas", image=self.ic_notas, command=self.abrir_notas, bg="#cddeea").place(x=150, y=40)
        Button(self.tela, text="Alunos", image=self.ic_alunos, command=self.abrir_alunos, bg="#cddeea").place(x=380, y=40)
        Button(self.tela, text="Professores", image=self.ic_professores, command=self.abrir_professores, bg="#cddeea").place(x=610, y=40)
        Button(self.tela, text="Logout", image=self.ic_logout, command=self.logout, bg="#cddeea").place(x=840, y=40)

        Label(self.tela, text="SISTEMA ESCOLA", image=self.ic_sistema, compound="top", 
              font=("Arial", 8, "bold"), bg="white").place(x=880, y=620)

 
    # MÉTODOS PARA CHAMAR TELAS
    def abrir_alunos(self):
        subprocess.run([sys.executable, "alunos.py"])

    def abrir_professores(self):
        subprocess.run([sys.executable, "professores.py"])

    def abrir_notas(self):
        subprocess.run([sys.executable, "notas.py"])

    def logout(self):
        self.tela.destroy()
        subprocess.run([sys.executable, "login.py"])

    def servicos_msg(self):
        messagebox.showinfo("Serviços", "Tela em desenvolvimento.")


# EXECUTAR

if __name__ == "__main__":
    TelaMenuSistema()