from tkinter import *
from tkinter import filedialog, messagebox
import sys
import os

try:
    import pymongo
except:
    os.system(f'"{sys.executable}" -m pip install pymongo')
    import pymongo

from PIL import Image, ImageTk


class CadastroAlunos:

    def __init__(self):
        self.tela = Tk()
        self.tela.title("Exemplo Mongo DB")
        self.tela.configure(bg="#590e5e")

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
        self.tela.resizable(False, False)

    # CRIAR BANCO
    def conectar_banco(self):
        try:
            self.conexao = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.conexao["escola"]
            self.collection = self.db["alunos"]
        except Exception as e:
            print(f"Erro ao conectar no MongoDB: {e}")

    # COMPONENTES    
    def criar_componentes(self):
        self.criar_labels()
        self.criar_campos()
        self.criar_icones()
        self.criar_botoes()

    def criar_labels(self):
        Label(self.tela, text="Cadastro de Alunos", font=("Arial", 22, "bold"), bg="#590e5e", fg="white").place(x=190, y=25)
        Label(self.tela, text="Código:", bg="#590e5e", fg="white", font=("Arial", 10, "bold")).place(x=50, y=100)
        Label(self.tela, text="Nome:", bg="#590e5e", fg="white", font=("Arial", 10, "bold")).place(x=50, y=140)
        Label(self.tela, text="Endereço:", bg="#590e5e", fg="white", font=("Arial", 10, "bold")).place(x=50, y=180)
        
        Label(self.tela, text="Data Nasc:", bg="#590e5e", fg="white", font=("Arial", 10, "bold")).place(x=420, y=140)
        Label(self.tela, text="Telefone:", bg="#590e5e", fg="white", font=("Arial", 10, "bold")).place(x=420, y=180)

        self.lbl_resultado = Label(self.tela, text="", bg="#590e5e", fg="white")
        self.lbl_resultado.place(x=50, y=220)

    def criar_campos(self):
        self.txt_codigo = Entry(self.tela, width=15, font=("Arial", 10))
        self.txt_nome = Entry(self.tela, width=30, font=("Arial", 10))
        self.txt_endereco = Entry(self.tela, width=30, font=("Arial", 10))
        
        self.txt_data = Entry(self.tela, width=18, font=("Arial", 10))
        self.txt_tel = Entry(self.tela, width=18, font=("Arial", 10))

        self.txt_codigo.place(x=140, y=100)
        self.txt_nome.place(x=140, y=140)
        self.txt_endereco.place(x=140, y=180)

        self.txt_data.place(x=530, y=140)
        self.txt_tel.place(x=530, y=180)

    # ICONES
    def criar_icones(self):
        diretorio = os.path.dirname(os.path.abspath(__file__))
        pasta_icones = os.path.join(diretorio, "icones")

        def ajustar_icone(nome_arquivo):
            caminho = os.path.join(pasta_icones, nome_arquivo)
            if os.path.exists(caminho):
                img = Image.open(caminho).resize((32, 32))
                return ImageTk.PhotoImage(img)
            return None

        self.foto_salvar = ajustar_icone("salvar.png")
        self.foto_alterar = ajustar_icone("alterar.png")
        self.foto_excluir = ajustar_icone("excluir.png")
        self.foto_consultar = ajustar_icone("consultar.png")
        self.foto_sair = ajustar_icone("exitt.png")

    # BOTOES
    def criar_botoes(self):
        Button(self.tela, text="Salvar", image=self.foto_salvar, compound=TOP, command=self.salvar).place(x=130, y=250)
        Button(self.tela, text="Alterar", image=self.foto_alterar, compound=TOP, command=self.atualizar).place(x=220, y=250)
        Button(self.tela, text="Excluir", image=self.foto_excluir, compound=TOP, command=self.apagar).place(x=310, y=250)
        Button(self.tela, text="Consultar", image=self.foto_consultar, compound=TOP, command=self.consultar).place(x=400, y=250)
        Button(self.tela, text="Sair", image=self.foto_sair, compound=TOP, command=self.tela.destroy).place(x=510, y=250)

    # MÉTODOS
    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_data.delete(0, END)
        self.txt_endereco.delete(0, END)
        self.txt_tel.delete(0, END)

    def dados(self):
        try:
            codigo_val = int(self.txt_codigo.get())
        except ValueError:
            codigo_val = self.txt_codigo.get()

        return {
            "codigo": codigo_val,
            "nomealuno": str(self.txt_nome.get()),
            "dataNascimento": str(self.txt_data.get()),
            "endereco": str(self.txt_endereco.get()),
            "telefone": str(self.txt_tel.get()),
        }

    def salvar(self):
        if not self.txt_codigo.get():
            messagebox.showerror("Erro", "O campo Código é obrigatório!")
            return
            
        try:
            codigo_atual = int(self.txt_codigo.get())
            self.collection.delete_many({"codigo": codigo_atual})
            self.collection.delete_many({"codigo": str(codigo_atual)})
        except:
            pass

        self.collection.insert_one(self.dados())
        self.limpar()
        messagebox.showinfo("Sucesso", "Aluno salvo com sucesso!")

    def atualizar(self):
        try:
            codigo = int(self.txt_codigo.get())
        except ValueError:
            codigo = self.txt_codigo.get()

        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código do aluno para alterar.")
            return

        resultado = self.collection.update_one({"codigo": codigo}, {"$set": self.dados()})

        if resultado.matched_count > 0:
            messagebox.showinfo("Sucesso", "Aluno atualizado!")
        else:
            messagebox.showwarning("Aviso", "Código não encontrado para atualizar.")

    def apagar(self):
        try:
            codigo = int(self.txt_codigo.get())
        except ValueError:
            codigo = self.txt_codigo.get()

        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código do aluno para excluir.")
            return

        resultado = self.collection.delete_one({"codigo": codigo})

        if resultado.deleted_count > 0:
            self.limpar()
            messagebox.showinfo("Sucesso", "Aluno excluído!")
        else:
            messagebox.showwarning("Aviso", "Aluno não encontrado para exclusão.")

    def consultar(self):
        try:
            codigo = int(self.txt_codigo.get())
        except ValueError:
            codigo = self.txt_codigo.get()

        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código para buscar.")
            return

        resultado = self.collection.find_one({"codigo": codigo})
        if not resultado:
            resultado = self.collection.find_one({"codigo": str(codigo)})

        if resultado:
            self.limpar()

            self.txt_codigo.insert(0, str(resultado.get("codigo", "")))
            
            nome = resultado.get("nomealuno", resultado.get("nomeAluno", ""))
            self.txt_nome.insert(0, str(nome))
            
            self.txt_data.insert(0, str(resultado.get("dataNascimento", "")))
            self.txt_endereco.insert(0, str(resultado.get("endereco", "")))
            self.txt_tel.insert(0, str(resultado.get("telefone", "")))
        else:
            messagebox.showwarning("Aviso", "Aluno não encontrado.") 


if __name__ == "__main__":
    CadastroAlunos()