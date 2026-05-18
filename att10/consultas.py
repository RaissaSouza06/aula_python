from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os 
import sys 

try:
    import pymongo
except:
    os.system(f'"{sys.executable}" -m pip install pymongo')
    import pymongo



class CadastroConsultas:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Cadastro de consultas")
        self.tela.configure(bg="#6daed1")


        self.largura = 700
        self.altura = 400
        self.pasta_inicial = ""

        self.centralizar_tela()
        self.conectar_banco()
        self.criar_componentes()


        self.tela.mainloop()

   
    # CONFIGURAÇÕES DA TELA

    def centralizar_tela(self):
      
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        posx = largura_screen/2 - self.largura/2
        posy = altura_screen/2 - self.altura/2
        print(largura_screen, altura_screen)
        self.tela.geometry("%dx%d+%d+%d" % (self.largura,self.altura, posx,posy))
        self.tela.resizable(False,False)

    def conectar_banco(self):
        try:
            self.cliente = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.cliente["hospital"] 
            self.collection = self.db["consultas"]
        except Exception as e:
            print(f"Erro ao conectar no MongoDB: {e}")

  
    # COMPONENTES

    def criar_componentes(self):
        self.criar_labels()
        self.criar_campos()
        self.criar_botoes()
   

    def criar_labels(self):
        Label(self.tela, text="Cadastro de Consultas", font=("Arial", 16, "bold"), bg="#6daed1").place(x=130, y=15)
        
        Label(self.tela, text="Código:", bg="#6daed1").place(x=130, y=70)
        Label(self.tela, text="Nome Médico:", bg="#6daed1").place(x=130, y=110)
        Label(self.tela, text="Nome Paciente:", bg="#6daed1").place(x=130, y=150)
        Label(self.tela, text="Data Consulta:", bg="#6daed1").place(x=130, y=190)

    def criar_campos(self):
        self.txt_codigo = Entry(self.tela, width=10)
        self.txt_nomeM = Entry(self.tela, width=50)
        self.txt_nomeP = Entry(self.tela, width=50)
        self.txt_data = Entry(self.tela, width=15)

        self.txt_codigo.place(x=240, y=70)
        self.txt_nomeM.place(x=240, y=110)
        self.txt_nomeP.place(x=240, y=150)
        self.txt_data.place(x=240, y=190)
      

    def criar_botoes(self):
        diretorio = os.path.dirname(os.path.abspath(__file__))
        pasta_icones = os.path.join(diretorio, "icones")

        def ajustar_icone(nome_arquivo):
            caminho = os.path.join(pasta_icones, nome_arquivo)
            if os.path.exists(caminho):
                img = Image.open(caminho).resize((32, 32))
                return ImageTk.PhotoImage(img)
            return None

        self.foto_salvar = ajustar_icone("salvar.png")
        self.foto_excluir = ajustar_icone("excluir.png")
        self.foto_alterar = ajustar_icone("alterar.png")
        self.foto_consultar = ajustar_icone("consultar.png")
        self.foto_sair = ajustar_icone("sair.png")

        self.btn_salvar = Button(self.tela, text="Salvar", image=self.foto_salvar, compound=TOP, command=self.salvar)
        self.btn_excluir = Button(self.tela, text="Excluir", image=self.foto_excluir, compound=TOP, command=self.apagar)
        self.btn_alterar = Button(self.tela, text="Alterar", image=self.foto_alterar, compound=TOP, command=self.atualizar)
        self.btn_consultar = Button(self.tela, text="Consultar", image=self.foto_consultar, compound=TOP, command=self.consultar)
        self.btn_sair = Button(self.tela, text="Sair", image=self.foto_sair, compound=RIGHT, command=self.tela.destroy)

        self.btn_salvar.place(x=130, y=310)
        self.btn_excluir.place(x=210, y=310)
        self.btn_alterar.place(x=290, y=310)
        self.btn_consultar.place(x=370, y=310)
        self.btn_sair.place(x=600, y=310)
    
    # FUNÇÕES

    def escolher_imagem(self):
        caminho = filedialog.askopenfilename(
            initialdir=self.pasta_inicial,
            title="Escolha uma imagem",
            filetypes=(
                ("Arquivos de imagem", "*.jpg;*.jpeg;*.png"),
                ("Todos os arquivos", "*.*")
            )
        )

        if caminho:
            imagem = Image.open(caminho)
            largura, altura = imagem.size

            if largura > 150:
                proporcao = largura / 150
                nova_altura = int(altura / proporcao)
                imagem = imagem.resize((110, nova_altura))

            imagem_tk = ImageTk.PhotoImage(imagem)

            self.lbl_imagem = Label(self.tela, image=imagem_tk)
            self.lbl_imagem.image = imagem_tk
            self.lbl_imagem.place(x=10, y=50)

  

    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_nomeM.delete(0, END)
        self.txt_nomeP.delete(0, END)
        self.txt_data.delete(0, END)

    def dados(self):
        return {
            "codigo": self.txt_codigo.get(),
            "nome": self.txt_nomeM.get(),
            "pasciente": self.txt_nomeP.get(),
            "data": self.txt_data.get(),
        }

    def salvar(self):
        if not self.txt_codigo.get():
            messagebox.showerror("Erro", "O código é obrigatório!")
            return
        
        self.collection.insert_one(self.dados())
        self.limpar()
        messagebox.showinfo("Sucesso", "Consulta salva com sucesso!")

    def atualizar(self):
        codigo = self.txt_codigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código da consulta que deseja alterar.")
            return

        resultado = self.collection.update_one({"codigo": codigo}, {"$set": self.dados()})
        
        if resultado.matched_count > 0:
            messagebox.showinfo("Sucesso", "Consulta atualizada com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Código não encontrado para atualizar.")

    def apagar(self):
        codigo = self.txt_codigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código da consulta que deseja excluir.")
            return

        resultado = self.collection.delete_one({"codigo": codigo})
        
        if resultado.deleted_count > 0:
            self.limpar()
            messagebox.showinfo("Sucesso", "Consulta excluída com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Consulta não encontrada para exclusão.")

    def consultar(self):
        codigo = self.txt_codigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código para buscar.")
            return

        resultado = self.collection.find_one({"codigo": codigo})
        
        if resultado:
            self.limpar()
            self.txt_codigo.insert(0, resultado.get("codigo", ""))
            self.txt_nomeM.insert(0, resultado.get("medico", ""))
            self.txt_nomeP.insert(0, resultado.get("paciente", ""))
            self.txt_data.insert(0, resultado.get("data", ""))
        else:
            messagebox.showwarning("Aviso", "Consulta não encontrada.")


# EXECUTAR
if __name__ == "__main__":
    CadastroConsultas()