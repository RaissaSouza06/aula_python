from tkinter import *
import pymongo
import sys 
from tkinter import ttk

class CadastroPassagens:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Exemplo MongoDB")
        self.tela.geometry("800x600")
        self.tela.configure(background="#fff")

        #CRIAR BANCO DE DADOS MONGO
        self.conexao = pymongo.MongoClient("mongodb://localhost:27017/")
        #CRIA BASE DE DADOS
        self.db = self.conexao["exemplo_passagens"]
        #CRIA COLEÇÃO
        self.collection = self.db["passagens"]

        self.criar_componentes()

    def criar_componentes(self):

        Label(self.tela, text="Cadastro de Passagens",font=("Arial", 30, "bold"),bg="#ffffff").place(x=200, y=50)

        Label(self.tela, text="Nome:", bg="#ffffff").place(x=130, y=140)
        self.txt_nome = Entry(self.tela, width=20)
        self.txt_nome.place(x=190, y=140)

        Label(self.tela, text="Telefone:", bg="#ffffff").place(x=130, y=170)
        self.txt_telefone = Entry(self.tela, width=40)
        self.txt_telefone.place(x=190, y=170)

        Label(self.tela, text="RG:", bg="#ffffff").place(x=450, y=170)
        self.txt_rg = Entry(self.tela, width=20)
        self.txt_rg.place(x=480, y=170)

        Label(self.tela, text="Local de viagem:", bg="#ffffff").place(x=130, y=200)
        self.txt_local = Entry(self.tela, width=20)
        self.txt_local.place(x=190, y=200)

        Label(self.tela, text="Data:", bg="#ffffff").place(x=450, y=200)
        self.txt_data = Entry(self.tela, width=25)
        self.txt_data.place(x=480, y=200)

        Label(self.tela, text="Horário:", bg="#ffffff").place(x=130, y=230)
        self.txt_horario = Entry(self.tela, width=20)
        self.txt_horario.place(x=190, y=230)

        Label(self.tela, text="Número de poltronas:", bg="#ffffff").place(x=520, y=230)
        self.txt_numero = Entry(self.tela, width=20)
        self.txt_numero.place(x=570, y=230)

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
            passagem = {
                "nome": self.txt_nome.get(),
                "telefone": self.txt_telefone.get(),
                "RG": self.txt_rg.get(),
                "local": self.txt_local.get(),
                "data": self.txt_data.get(),
                "horario": self.txt_horario.get(),
                "numero": self.txt_numero.get(),
            }

            self.collection.insert_one(passagem)
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
                "nome": self.txt_nome.get(),
                "telefone": self.txt_telefone.get(),
                "RG": self.txt_rg.get(),
                "local": self.txt_local.get(),
                "data": self.txt_data.get(),
                "horario": self.txt_horario.get(),
                "numero": self.txt_numero.get(),
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
            self.txt_telefone.insert(END, resultado["telefone"])
            self.txt_rg.insert(END, resultado["rg"])
            self.txt_local.insert(END, resultado["local"])
            self.txt_data.insert(END, resultado["data"])
            self.txt_horario.insert(END, resultado["horario"])
            self.txt_numero.insert(END, resultado["numero"])
        else:
            self.lbl_resultado.config(text="Não encontrado")

    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_telefone.delete(0, END)
        self.txt_rg.delete(0, END)
        self.txt_local.delete(0, END)
        self.txt_data.delete(0, END)
        self.txt_horario.delete(0, END)
        self.txt_numero.delete(0, END)
    
    def executar(self):
        self.tela.mainloop()

