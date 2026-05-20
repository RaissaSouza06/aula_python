from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os 
import sys 

try:
    import pymongo
except:
    os.system(f'"{sys.executable}" -m pip install pymongo')
    import pymongo


class CadastroProfessores:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Cadastro de Professores")
        self.tela.configure(bg="#7a1717")

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
        self.tela.geometry("%dx%d+%d+%d" % (self.largura, self.altura, posx, posy))
        self.tela.resizable(False, False)

    def conectar_banco(self):
        try:
            self.conexao = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.conexao["escola"] 
            self.collection = self.db["professores"]
        except Exception as e:
            print(f"Erro ao conectar no MongoDB: {e}")

  
    # COMPONENTES
    def criar_componentes(self):
        self.criar_labels()
        self.criar_campos()
        self.criar_botoes()
   

    def criar_labels(self):
        Label(self.tela, text="Cadastro de Professores", font=("Arial", 18, "bold"), bg="#7a1717", fg="white").place(x=200, y=15)
        
        Label(self.tela, text="Código:", bg="#7a1717", fg="white", font=("Arial", 10, "bold")).place(x=130, y=70)
        Label(self.tela, text="Nome do Professor:", bg="#7a1717", fg="white", font=("Arial", 10, "bold")).place(x=130, y=110)
        Label(self.tela, text="Disciplina Lecionada:", bg="#7a1717", fg="white", font=("Arial", 10, "bold")).place(x=130, y=150)
        Label(self.tela, text="Qtd. Aulas/Semana:", bg="#7a1717", fg="white", font=("Arial", 10, "bold")).place(x=130, y=190)
        Label(self.tela, text="Formação:", bg="#7a1717", fg="white", font=("Arial", 10, "bold")).place(x=130, y=230)

    def criar_campos(self):
        self.txt_codigo = Entry(self.tela, width=10, font=("Arial", 10))
        self.txt_nome = Entry(self.tela, width=42, font=("Arial", 10))
        self.txt_disciplina = Entry(self.tela, width=42, font=("Arial", 10))
        self.txt_qtd = Entry(self.tela, width=15, font=("Arial", 10))
        self.txt_form = Entry(self.tela, width=25, font=("Arial", 10))

        self.txt_codigo.place(x=320, y=70)
        self.txt_nome.place(x=320, y=110)
        self.txt_disciplina.place(x=320, y=150)
        self.txt_qtd.place(x=320, y=190)
        self.txt_form.place(x=320, y=230)


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
        self.foto_sair = ajustar_icone("exitt.png")

        self.btn_salvar = Button(self.tela, text="Salvar", image=self.foto_salvar, compound=TOP, command=self.salvar)
        self.btn_alterar = Button(self.tela, text="Alterar", image=self.foto_alterar, compound=TOP, command=self.atualizar)
        self.btn_excluir = Button(self.tela, text="Excluir", image=self.foto_excluir, compound=TOP, command=self.apagar)
        self.btn_consultar = Button(self.tela, text="Consultar", image=self.foto_consultar, compound=TOP, command=self.consultar)
        self.btn_sair = Button(self.tela, text="Sair", image=self.foto_sair, compound=TOP, command=self.tela.destroy)

        self.btn_salvar.place(x=130, y=310)
        self.btn_alterar.place(x=210, y=310)
        self.btn_excluir.place(x=290, y=310)
        self.btn_consultar.place(x=370, y=310)
        self.btn_sair.place(x=470, y=310)
    
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
        self.txt_nome.delete(0, END)
        self.txt_disciplina.delete(0, END)
        self.txt_qtd.delete(0, END)
        self.txt_form.delete(0, END)


    def dados(self):
        try:
            codigo_limpo = int(self.txt_codigo.get())
        except ValueError:
            codigo_limpo = self.txt_codigo.get()

        try:
            qtd_limpa = int(self.txt_qtd.get())
        except ValueError:
            qtd_limpa = self.txt_qtd.get()

        return {
            "codigo": codigo_limpo,
            "nome": str(self.txt_nome.get()),
            "disciplina": str(self.txt_disciplina.get()),
            "quantidade": qtd_limpa,
            "formacao": str(self.txt_form.get()),
        }

    def salvar(self):
        if not self.txt_codigo.get():
            messagebox.showerror("Erro", "O código é obrigatório!")
            return
        
        try:
            cod = int(self.txt_codigo.get())
            self.collection.delete_many({"codigo": cod})
            self.collection.delete_many({"codigo": str(cod)})
        except:
            pass
        
        self.collection.insert_one(self.dados())
        self.limpar()
        messagebox.showinfo("Sucesso", "Professor salvo com sucesso!")

    def atualizar(self):
        try:
            codigo = int(self.txt_codigo.get())
        except ValueError:
            codigo = self.txt_codigo.get()

        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código do professor que deseja alterar.")
            return

        resultado = self.collection.update_one({"codigo": codigo}, {"$set": self.dados()})
        
        if resultado.matched_count > 0:
            messagebox.showinfo("Sucesso", "Professor atualizado com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Código não encontrado para atualizar.")

    def apagar(self):
        try:
            codigo = int(self.txt_codigo.get())
        except ValueError:
            codigo = self.txt_codigo.get()

        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código do professor que deseja excluir.")
            return

        resultado = self.collection.delete_one({"codigo": codigo})
        
        if resultado.deleted_count > 0:
            self.limpar()
            messagebox.showinfo("Sucesso", "Professor excluído com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Professor não encontrado para exclusão.")

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
            self.txt_nome.insert(0, str(resultado.get("nome", "")))
            self.txt_disciplina.insert(0, str(resultado.get("disciplina", "")))
            self.txt_qtd.insert(0, str(resultado.get("quantidade", "")))
            self.txt_form.insert(0, str(resultado.get("formacao", "")))
        else:
            messagebox.showwarning("Aviso", "Professor não encontrado.")


# EXECUTAR
if __name__ == "__main__":
    CadastroProfessores()