from tkinter import *
import pymongo
import sys 
from tkinter import ttk

class CadastroMecanica:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Exemplo MongoDB")
        self.tela.geometry("800x600")
        self.tela.configure(background="#ae7cd6")

        #CRIAR BANCO DE DADOS MONGO
        self.conexao = pymongo.MongoClient("mongodb://localhost:27017/")
        #CRIA BASE DE DADOS
        self.db = self.conexao["exemplo_mecanica"]
        #CRIA COLEÇÃO
        self.collection = self.db["mecanica"]

        self.criar_componentes()

    def criar_componentes(self):

        Label(self.tela, text="Cadastro de Carros na mecânica",font=("Arial", 30, "bold"),bg="#ae7cd6").place(x=120, y=40)

       # Campos de Entrada
        Label(self.tela, text="Marca do carro:", bg="#ae7cd6").place(x=130, y=140)
        self.txt_marca = Entry(self.tela, width=40)
        self.txt_marca.place(x=240, y=140)

        Label(self.tela, text="Modelo do carro:", bg="#ae7cd6").place(x=130, y=180)
        self.txt_modelo = Entry(self.tela, width=20)
        self.txt_modelo.place(x=250, y=180)

        Label(self.tela, text="Chassi:", bg="#ae7cd6").place(x=450, y=180)
        self.txt_chassi = Entry(self.tela, width=20)
        self.txt_chassi.place(x=510, y=180)

        Label(self.tela, text="Renavam:", bg="#ae7cd6").place(x=130, y=220)
        self.txt_renavam = Entry(self.tela, width=20)
        self.txt_renavam.place(x=210, y=220)

        Label(self.tela, text="Problema:", bg="#ae7cd6").place(x=450, y=220)
        self.txt_problema = Entry(self.tela, width=20)
        self.txt_problema.place(x=530, y=220)

        self.lbl_resultado = Label(self.tela, text="", bg="#ae7cd6", font=("Arial", 10, "bold"))
        self.lbl_resultado.place(x=130, y=420)

        #CRIANDO OS BOTÕES
              
        self.foto_salvar = PhotoImage(file="icones/salvar.png")
        self.foto_excluir = PhotoImage(file="icones/excluir.png")
        self.foto_alterar = PhotoImage(file="icones/alterar.png")
        self.foto_consultar = PhotoImage(file="icones/consultar.png")
        self.foto_sair = PhotoImage(file="icones/sair.png")

   
        self.btn_salvar = Button(self.tela, text="Salvar",image=self.foto_salvar,compound=TOP,command=self.salvar)
        self.btn_salvar.place(x=130, y=300)

        self.btn_excluir = Button(self.tela, text="Excluir",image=self.foto_excluir,compound=TOP,command=self.excluir)
        self.btn_excluir.place(x=230, y=300)
        
        self.btn_alterar = Button(self.tela, text="Alterar",image=self.foto_alterar,compound=TOP,command=self.atualizar)
        self.btn_alterar.place(x=330, y=300)

        self.btn_consultar = Button(self.tela, text="Consultar",image=self.foto_consultar,compound=TOP,command=self.consultar)        
        self.btn_consultar.place(x=430, y=300)

        self.btn_sair = Button(self.tela, text="Sair",image=self.foto_sair,compound=RIGHT,command=self.sair)  
        self.btn_sair.place(x=550, y=300)

    def salvar(self):
        try:
            carro = {
                "marca": self.txt_marca.get(),
                "modelo": self.txt_modelo.get(),
                "chassi": self.txt_chassi.get(),
                "renavam": self.txt_renavam.get(),
                "problema": self.txt_problema.get(),
            }

            self.collection.insert_one(carro)
            self.limpar()
            self.lbl_resultado.config(text="Salvo com sucesso!")

        except:
            self.lbl_resultado.config(text="Erro ao salvar")

    def sair(self):
        self.conexao.close()
        self.tela.destroy()
        sys.exit()

    def atualizar(self):
        renavam = self.txt_renavam.get()

        self.collection.update_one(
            {"renavam": renavam},
            {"$set": {
                "marca": self.txt_marca.get(),
                "modelo": self.txt_modelo.get(),
                "chassi": self.txt_chassi.get(),
                "problema": self.txt_problema.get(),
            }}
        )

        self.limpar()
        self.lbl_resultado.config(text="Atualizado!")

    def excluir(self):
        renavam = self.txt_renavam.get()
        self.collection.delete_one({"renavam": renavam})
        self.limpar()
        self.lbl_resultado.config(text="Excluído!")
    
    def consultar(self):
        renavam = self.txt_renavam.get()
        resultado = self.collection.find_one({"renavam": renavam})

        if resultado:
            self.limpar()
            self.txt_marca.insert(END, resultado["marca"])
            self.txt_modelo.insert(END, resultado["modelo"])
            self.txt_chassi.insert(END, resultado["chassi"])
            self.txt_renavam.insert(END, resultado["renavam"])
            self.txt_problema.insert(END, resultado["problema"])
            self.lbl_resultado.config(text="Veículo encontrado!", fg="#2ECC71")
        else:
            self.lbl_resultado.config(text="Não encontrado")

    def limpar(self):
        self.txt_marca.delete(0, END)
        self.txt_modelo.delete(0, END)
        self.txt_chassi.delete(0, END)
        self.txt_renavam.delete(0, END)
        self.txt_problema.delete(0, END)
    
    def executar(self):
        self.tela.mainloop()

