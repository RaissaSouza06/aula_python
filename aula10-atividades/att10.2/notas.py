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



class CadastroNotas:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Cadastro de notas")
        self.tela.configure(bg="#246942")


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
            self.db = self.cliente["escola"] 
            self.collection = self.db["notas"]
        except Exception as e:
            print(f"Erro ao conectar no MongoDB: {e}")

  
    # COMPONENTES
    def criar_componentes(self):
        self.criar_labels()
        self.criar_campos()
        self.criar_botoes()
   

    def criar_labels(self):
        Label(self.tela, text="Cadastro de Notas", font=("Arial", 16, "bold"), bg="#6daed1").place(x=130, y=15)
        Label(self.tela, text="Código:", bg="#6daed1").place(x=130, y=70)
        Label(self.tela, text="Nome do Aluno:", bg="#6daed1").place(x=130, y=110)
        Label(self.tela, text="Nota 1:", bg="#6daed1").place(x=130, y=110)
        Label(self.tela, text="Nota 2:", bg="#6daed1").place(x=130, y=150)
        Label(self.tela, text="Nota 3:", bg="#6daed1").place(x=130, y=190)
        Label(self.tela, text="Nota 4:", bg="#6daed1").place(x=130, y=190)
        Label(self.tela, text="Média:", bg="#6daed1").place(x=130, y=190)

    def criar_campos(self):
        self.txt_codigo = Entry(self.tela, width=10)
        self.txt_nome = Entry(self.tela, width=50)
        self.txt_n1 = Entry(self.tela, width=50)
        self.txt_n2 = Entry(self.tela, width=15)
        self.txt_n3 = Entry(self.tela, width=15)
        self.txt_n4 = Entry(self.tela, width=15)
        self.txt_media = Entry(self.tela, width=15)

        self.txt_codigo.place(x=240, y=70)
        self.txt_nome.place(x=240, y=110)
        self.txt_n1.place(x=240, y=150)
        self.txt_n2.place(x=240, y=190)
        self.txt_n3.place(x=240, y=190)
        self.txt_n4.place(x=240, y=190)
        self.txt_media.place(x=240, y=190)


    def criar_botoes(self):
        diretorio = os.path.dirname(os.path.abspath(__file__))
        pasta_icones = os.path.join(diretorio, "icones")

        def ajustar_icone(nome_arquivo):
            caminho = os.path.join(pasta_icones, nome_arquivo)
            if os.path.exists(caminho):
                img = Image.open(caminho).resize((32, 32))
                return ImageTk.PhotoImage(img)
            return None

        self.foto_calcular = ajustar_icone("calcular.png")
        self.foto_ver = ajustar_icone("ver.png")
        self.foto_sair = ajustar_icone("logout.png")

        self.btn_calcular = Button(self.tela, text="Calcular", image=self.foto_calcular, compound=TOP, command=self.salvar)
        self.btn_ver= Button(self.tela, text="Ver", image=self.foto_ver, compound=TOP, command=self.apagar)
        self.btn_sair = Button(self.tela, text="Sair", image=self.foto_sair, compound=RIGHT, command=self.tela.destroy)

        self.btn_calcular.place(x=130, y=310)
        self.btn_ver.place(x=210, y=310)
        self.btn_sair.place(x=300, y=310)
    
    # # FUNÇÕES
    # def escolher_imagem(self):
    #     caminho = filedialog.askopenfilename(
    #         initialdir=self.pasta_inicial,
    #         title="Escolha uma imagem",
    #         filetypes=(
    #             ("Arquivos de imagem", "*.jpg;*.jpeg;*.png"),
    #             ("Todos os arquivos", "*.*")
    #         )
    #     )

        # if caminho:
        #     imagem = Image.open(caminho)
        #     largura, altura = imagem.size

        #     if largura > 150:
        #         proporcao = largura / 150
        #         nova_altura = int(altura / proporcao)
        #         imagem = imagem.resize((110, nova_altura))

        #     imagem_tk = ImageTk.PhotoImage(imagem)

        #     self.lbl_imagem = Label(self.tela, image=imagem_tk)
        #     self.lbl_imagem.image = imagem_tk
        #     self.lbl_imagem.place(x=10, y=50)

  

    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_n1.delete(0, END)
        self.txt_n2.delete(0, END)
        self.txt_n3.delete(0, END)
        self.txt_n4.delete(0, END)
        self.txt_media.delete(0, END)

    def dados(self):
        return {
            "codigo": self.txt_codigo.get(),
            "nomeAluno": self.txt_nome.get(),
            "nota1": self.txt_n1.get(),
            "nota2": self.txt_n2.get(),
            "nota3": self.txt_n3.get(),
            "nota4": self.txt_n4.get(),
            "media": self.txt_media.get(),
        }

    def salvar(self):
        if not self.txt_codigo.get():
            messagebox.showerror("Erro", "O código é obrigatório!")
            return
        
        self.collection.insert_one(self.dados())
        self.limpar()
        messagebox.showinfo("Sucesso", "Nota salva com sucesso!")

    def atualizar(self):
        codigo = self.txt_codigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código da nota que deseja alterar.")
            return

        resultado = self.collection.update_one({"codigo": codigo}, {"$set": self.dados()})
        
        if resultado.matched_count > 0:
            messagebox.showinfo("Sucesso", "Nota atualizada com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Código não encontrado para atualizar.")

    def apagar(self):
        codigo = self.txt_codigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código da nota que deseja excluir.")
            return

        resultado = self.collection.delete_one({"codigo": codigo})
        
        if resultado.deleted_count > 0:
            self.limpar()
            messagebox.showinfo("Sucesso", "Nota excluída com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Nota não encontrada para exclusão.")

    def consultar(self):
        codigo = self.txt_codigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código para buscar.")
            return

        resultado = self.collection.find_one({"codigo": codigo})
        
        if resultado:
            self.limpar()
            self.txt_codigo.insert(0, resultado.get("codigo", ""))
            self.txt_nome.insert(0, resultado.get("nomeAluno", ""))
            self.txt_n1.insert(0, resultado.get("n1", ""))
            self.txt_n2.insert(0, resultado.get("n2", ""))
            self.txt_n3.insert(0, resultado.get("n3", ""))
            self.txt_24.insert(0, resultado.get("n4", ""))
            self.txt_media.insert(0, resultado.get("media", ""))
        else:
            messagebox.showwarning("Aviso", "Nota não encontrado.")


# EXECUTAR
if __name__ == "__main__":
    CadastroNotas()