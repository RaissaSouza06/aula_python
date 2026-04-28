from tkinter import *
import pymongo
import sys 
from tkinter import ttk

class CadastroProdutos:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Exemplo MongoDB")
        self.tela.geometry("800x600")
        self.tela.configure(background="#fff")

        #CRIAR BANCO DE DADOS MONGO
        self.conexao = pymongo.MongoClient("mongodb://localhost:27017/")
        #CRIA BASE DE DADOS
        self.db = self.conexao["exemplo_produtos"]
        #CRIA COLEÇÃO
        self.collection = self.db["produtos"]

        self.criar_componentes()

    def criar_componentes(self):

        Label(self.tela, text="Cadastro de Produtos",font=("Arial", 30, "bold"),bg="#ffffff").place(x=200, y=50)

        Label(self.tela, text="Código:", bg="#ffffff").place(x=130, y=140)
        self.txt_codigo = Entry(self.tela, width=20)
        self.txt_codigo.place(x=190, y=140)

        Label(self.tela, text="Nome:", bg="#ffffff").place(x=130, y=170)
        self.txt_nome = Entry(self.tela, width=40)
        self.txt_nome.place(x=190, y=170)

        Label(self.tela, text="Quantidade:", bg="#ffffff").place(x=450, y=170)
        self.txt_quantidade = Entry(self.tela, width=20)
        self.txt_quantidade.place(x=480, y=170)

        Label(self.tela, text="Preço:", bg="#ffffff").place(x=130, y=200)
        self.txt_preco = Entry(self.tela, width=20)
        self.txt_preco.place(x=190, y=200)

        Label(self.tela, text="Total:", bg="#ffffff").place(x=450, y=200)
        self.txt_total = Entry(self.tela, width=25)
        self.txt_total.place(x=480, y=200)

        self.lbl_resultado = Label(self.tela, text="", bg="#ffffff")
        self.lbl_resultado.place(x=490, y=410)

        #CRIANDO OS BOTÕES
              
        self.foto_salvar = PhotoImage(file="icones/salvar.png")
        self.foto_excluir = PhotoImage(file="icones/excluir.png")
        self.foto_alterar = PhotoImage(file="icones/alterar.png")
        self.foto_consultar = PhotoImage(file="icones/consultar.png")
        self.foto_sair = PhotoImage(file="icones/sair.png")

   
        self.btn_salvar = Button(self.tela, text="Salvar",image=self.foto_salvar,compound=TOP,command=self.salvar)
        self.btn_salvar.place(x=130, y=280)

        self.btn_excluir = Button(self.tela, text="Excluir",image=self.foto_excluir,compound=TOP,command=self.excluir)
        self.btn_excluir.place(x=220, y=280)
        
        self.btn_alterar = Button(self.tela, text="Alterar",image=self.foto_alterar,compound=TOP,command=self.atualizar)
        self.btn_alterar.place(x=310, y=280)

        self.btn_consultar = Button(self.tela, text="Consultar",image=self.foto_consultar,compound=TOP,command=self.consultar)        
        self.btn_consultar.place(x=400, y=280)

        self.btn_sair = Button(self.tela, text="Sair",image=self.foto_sair,compound=RIGHT,command=self.sair)  
        self.btn_sair.place(x=490, y=280)

    def salvar(self):
        try:
            produto = {
                "código": self.txt_codigo.get(),
                "nome": self.txt_nome.get(),
                "quantidade": int(self.txt_quantidade.get()),
                "preço": float(self.txt_preco.get()),
                "total": float(self.txt_total.get()),
            }

            self.collection.insert_one(produto)
            self.limpar()
            self.lbl_resultado.config(text="Salvo com sucesso!")

        except:
            self.lbl_resultado.config(text="Erro ao salvar")

    def sair(self):
        self.tela.destroy()
        self.conn.close()
        self.tela.destroy()
        sys.exit()

    def atualizar(self):
        codigo = self.txt_codigo.get()

        self.collection.update_one(
            {"código": codigo},
            {"$set": {
                "código": self.txt_codigo.get(),
                "nome": self.txt_nome.get(),
                "quantidade": int(self.txt_quantidade.get()),
                "preço": float(self.txt_preco.get()),
                "total": float(self.txt_total.get()),
            }}
        )

        self.limpar()
        self.lbl_resultado.config(text="Atualizado!")

    def excluir(self):
        codigo = self.txt_codigo.get()
        self.collection.delete_one({"código": codigo})
        self.limpar()
        self.lbl_resultado.config(text="Excluído!")
    
    def consultar(self):
        codigo = self.txt_codigo.get()
        resultado = self.collection.find_one({"código": codigo})

        if resultado:
            self.txt_nome.insert(END, resultado["nome"])
            self.txt_quantidade.insert(END, resultado["quantidade"])
            self.txt_preco.insert(END, resultado["preço"])
            self.txt_total.insert(END, resultado["total"])
        else:
            self.lbl_resultado.config(text="Não encontrado")

    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_quantidade.delete(0, END)
        self.txt_preco.delete(0, END)
        self.txt_total.delete(0, END)
    
    def executar(self):
        self.tela.mainloop()

