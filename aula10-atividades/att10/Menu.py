import tkinter as tk
from tkinter import Menu, Label, Button, messagebox
import subprocess
import sys
import os

# Instale a biblioteca Pillow caso de erro
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
        caminho = os.path.join(diretorio, "icones", "hospital.jpg")
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
        opçoes_menus_gestao.add_command(label="Pacientes", command=self.abrir_pacientes)
        opçoes_menus_gestao.add_command(label="Consultas", command=self.abrir_consultas)
        opçoes_menus_gestao.add_command(label="Tratamentos",command=self.abrir_tratamentos)
        self.tela.config(menu=barra_menus)

    # ÍCONES
    def carregar_icones(self):
        self.ic_consultas = self.carregar_png("consultas.png", 50, 50)
        self.ic_pacientes = self.carregar_png("pacientes.png", 50, 50)
        self.ic_tratamentos = self.carregar_png("tratamentos.png", 50, 50)
        self.ic_logout = self.carregar_png("logout.png", 50, 50)
        # self.ic_sistema = self.carregar_png("logo.png", 40, 40)

    def carregar_png(self, nome_arquivo, largura, altura):
        diretorio = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(diretorio, "icones", nome_arquivo)
        
        if os.path.exists(caminho):
            img = Image.open(caminho)
            img = img.resize((largura, altura))
            return ImageTk.PhotoImage(img)
        else:
            print(f"Aviso: O ícone {nome_arquivo} não foi encontrado em: {caminho}")
        return None


    # BOTÕES   
    def criar_botoes(self):
        estilo = {"bg": "white", "compound": "top", "relief": "flat", "pady": 5}

        Button(self.tela, text="Consultas", image=self.ic_consultas, command=self.abrir_consultas, **estilo).place(x=150, y=40)
        Button(self.tela, text="Pacientes", image=self.ic_pacientes, command=self.abrir_pacientes, **estilo).place(x=380, y=40)
        Button(self.tela, text="Tratamentos", image=self.ic_tratamentos, command=self.abrir_tratamentos, **estilo).place(x=610, y=40)
        Button(self.tela, text="Logout", image=self.ic_logout, command=self.logout, **estilo).place(x=840, y=40)

 
    # MÉTODOS PARA CHAMAR TELAS
    def abrir_pacientes(self):
        subprocess.run([sys.executable, "pacientes.py"])

    def abrir_consultas(self):
        subprocess.run([sys.executable, "consultas.py"])

    def abrir_tratamentos(self):
        subprocess.run([sys.executable, "tratamentos.py"])

    def logout(self):
        self.tela.destroy()
        subprocess.run([sys.executable, "login.py"])


# EXECUTAR

if __name__ == "__main__":
    TelaMenuSistema()