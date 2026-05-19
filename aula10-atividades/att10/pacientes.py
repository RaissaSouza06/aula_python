from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import sys
import os


try:
    import pymongo
except:
    os.system(f'"{sys.executable}" -m pip install pymongo')
    import pymongo

from PIL import Image, ImageTk


class CadastroPacientes:

    def __init__(self):
        self.tela = Tk()
        self.tela.title("Exemplo Mongo DB")
        self.tela.configure(bg="#6daed1")

        self.largura = 700
        self.altura = 400

        self.centralizar_tela()
        self.conectar_banco()
        self.criar_componentes()

        self.tela.mainloop()

  
    # CRIANDO TELA
   
    def centralizar_tela(self):
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = int(largura_screen / 2 - self.largura / 2)
        posy = int(altura_screen / 2 - self.altura / 2)

        self.tela.geometry(f"{self.largura}x{self.altura}+{posx}+{posy}")
        self.tela.resizable(True, True)

    
    # CRIAR BANCO
  
    def conectar_banco(self):
        self.cliente = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.cliente["hospital"]
        self.collection = self.db["pacientes"]

    
    # COMPONENTES    
    def criar_componentes(self):
        self.criar_labels()
        self.criar_campos()
        self.criar_icones()
        self.criar_botoes()

    def criar_labels(self):
        Label(self.tela,text="Cadastro de Pacientes", font=("Arial", 22, "bold"), bg="#6daed1").place(x=180, y=30)

        Label(self.tela, text="Código:", bg="#6daed1").place(x=130, y=100)
        Label(self.tela, text="Nome:", bg="#6daed1").place(x=130, y=130)
        Label(self.tela, text="CPF:", bg="#6daed1").place(x=450, y=130)
        Label(self.tela, text="Idade:", bg="#6daed1").place(x=130, y=160)
        Label(self.tela, text="Rua:", bg="#6daed1").place(x=450, y=160)
        Label(self.tela, text="Bairro:", bg="#6daed1").place(x=130, y=190)
        Label(self.tela, text="Estado:", bg="#6daed1").place(x=330, y=190)
        Label(self.tela, text="Cidade:", bg="#6daed1").place(x=520, y=190)

        self.lbl_resultado = Label(self.tela, text="", bg="#6daed1")
        self.lbl_resultado.place(x=450, y=300)

    def criar_campos(self):
        self.txt_codigo = Entry(self.tela, width=20)
        self.txt_nome = Entry(self.tela, width=35)
        self.txt_cpf = Entry(self.tela, width=20)
        self.txt_idade = Entry(self.tela, width=20)
        self.txt_end = Entry(self.tela, width=20)
        self.txt_bairro = Entry(self.tela, width=18)
        self.txt_cidade = Entry(self.tela, width=15)

        self.comboestado = ttk.Combobox(
            self.tela,
            values=[
                "São Paulo",
                "Rio de Janeiro",
                "Minas Gerais",
                "Espírito Santo"
            ],
            width=15
        )

        self.txt_codigo.place(x=190, y=100)
        self.txt_nome.place(x=190, y=130)
        self.txt_cpf.place(x=480, y=130)
        self.txt_idade.place(x=190, y=160)
        self.txt_end.place(x=480, y=160)
        self.txt_bairro.place(x=190, y=190)
        self.comboestado.place(x=380, y=190)
        self.txt_cidade.place(x=570, y=190)

    # ICONES
    
    def criar_icones(self):
        diretorio = os.path.dirname(os.path.abspath(__file__))
        pasta_icones = os.path.join(diretorio, "icones")

        def ajustar_icone(nome_arquivo):
            caminho = os.path.join(pasta_icones, nome_arquivo)
            if os.path.exists(caminho):
                img = Image.open(caminho).resize((32, 32)) # Redimensiona para 32x32 pixels
                return ImageTk.PhotoImage(img)
            else:
                print(f"Erro: Não encontrei {nome_arquivo}")
                return None

        self.foto_salvar = ajustar_icone("salvar.png")
        self.foto_alterar = ajustar_icone("alterar.png")
        self.foto_excluir = ajustar_icone("excluir.png")
        self.foto_consultar = ajustar_icone("consultar.png")
        self.foto_sair = ajustar_icone("sair.png")

    
    # BOTOES
   
    def criar_botoes(self):

        Button(
            self.tela,
            text="Salvar",
            image=self.foto_salvar,
            compound=TOP,
            command=self.salvar
        ).place(x=130, y=250)

        Button(
            self.tela,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP,
            command=self.atualizar
        ).place(x=220, y=250)

        Button(
            self.tela,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP,
            command=self.apagar
        ).place(x=310, y=250)

        Button(
            self.tela,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP,
            command=self.consultar
        ).place(x=400, y=250)

        Button(
            self.tela,
            text="Sair",
            image=self.foto_sair,
            compound=TOP,
            command=self.tela.quit
        ).place(x=510, y=250)

    
    # MÉTODOS

    
    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_cpf.delete(0, END)
        self.txt_idade.delete(0, END)
        self.txt_end.delete(0, END)
        self.txt_bairro.delete(0, END)
        self.txt_cidade.delete(0, END)
        self.comboestado.set("")

    def dados(self):
        idade_texto = self.txt_idade.get()
        idade_final = int(idade_texto) if idade_texto.isdigit() else 0

        return {
            "código": self.txt_codigo.get(),
            "nome": self.txt_nome.get(),
            "idade": idade_final,
            "cpf": self.txt_cpf.get(),
            "endereço": self.txt_end.get(),
            "bairro": self.txt_bairro.get(),
            "cidade": self.txt_cidade.get(),
            "estado": self.comboestado.get()
        }

    def salvar(self):
        if not self.txt_codigo.get():
            messagebox.showerror("Erro", "O campo Código é obrigatório!")
            return
            
        self.collection.insert_one(self.dados())
        self.limpar()
        messagebox.showinfo("Sucesso", "Paciente salvo!")

    def atualizar(self):
        codigo = self.txt_codigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código do paciente para alterar.")
            return

        resultado = self.collection.update_one(
            {"código": codigo},
            {"$set": self.dados()}
        )

        if resultado.matched_count > 0:
            messagebox.showinfo("Sucesso", "Paciente atualizado!")
        else:
            messagebox.showwarning("Aviso", "Código não encontrado para atualizar.")

    def apagar(self):
        codigo = self.txt_codigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código do paciente para excluir.")
            return

        resultado = self.collection.delete_one({"código": codigo})

        if resultado.deleted_count > 0:
            self.limpar()
            messagebox.showinfo("Sucesso", "Paciente excluído!")
        else:
            messagebox.showwarning("Aviso", "Paciente não encontrado para exclusão.")

    def consultar(self):
        codigo = self.txt_codigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código para buscar.")
            return

        resultado = self.collection.find_one({"código": codigo})

        if resultado:
            self.limpar()

            self.txt_codigo.insert(0, resultado.get("código", ""))
            self.txt_nome.insert(0, resultado.get("nome", ""))
            self.txt_cpf.insert(0, resultado.get("cpf", ""))
            self.txt_idade.insert(0, resultado.get("idade", ""))
            self.txt_end.insert(0, resultado.get("endereço", ""))
            self.txt_bairro.insert(0, resultado.get("bairro", ""))
            self.txt_cidade.insert(0, resultado.get("cidade", ""))
            self.comboestado.set(resultado.get("estado", ""))
        else:
            messagebox.showwarning("Aviso", "Paciente não encontrado.") # Corrigido para Paciente


# EXECUTAR
if __name__ == "__main__":
    CadastroPacientes()