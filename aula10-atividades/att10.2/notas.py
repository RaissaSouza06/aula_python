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
        Label(self.tela, text="Cadastro de Notas", font=("Arial", 16, "bold"), bg="#246942", fg="white").place(x=130, y=15)
        Label(self.tela, text="Código:", bg="#246942", fg="white", font=("Arial", 10, "bold")).place(x=130, y=70)
        Label(self.tela, text="Nome do Aluno:", bg="#246942", fg="white", font=("Arial", 10, "bold")).place(x=130, y=110)
        Label(self.tela, text="Nota 1:", bg="#246942", fg="white", font=("Arial", 10, "bold")).place(x=130, y=150)
        Label(self.tela, text="Nota 2:", bg="#246942", fg="white", font=("Arial", 10, "bold")).place(x=130, y=190)
        Label(self.tela, text="Nota 3:", bg="#246942", fg="white", font=("Arial", 10, "bold")).place(x=380, y=150)
        Label(self.tela, text="Nota 4:", bg="#246942", fg="white", font=("Arial", 10, "bold")).place(x=380, y=190)
        Label(self.tela, text="Média Calculada:", bg="#246942", fg="white", font=("Arial", 10, "bold")).place(x=130, y=240)

    def criar_campos(self):
        self.txt_codigo = Entry(self.tela, width=15, font=("Arial", 10))
        self.txt_nome = Entry(self.tela, width=45, font=("Arial", 10))
        self.txt_n1 = Entry(self.tela, width=10, font=("Arial", 10))
        self.txt_n2 = Entry(self.tela, width=10, font=("Arial", 10))
        self.txt_n3 = Entry(self.tela, width=10, font=("Arial", 10))
        self.txt_n4 = Entry(self.tela, width=10, font=("Arial", 10))
        
        self.txt_media = Entry(self.tela, width=10, font=("Arial", 10, "bold"), state="readonly")

        self.txt_codigo.place(x=260, y=70)
        self.txt_nome.place(x=260, y=110)
        self.txt_n1.place(x=260, y=150)
        self.txt_n2.place(x=260, y=190)
        self.txt_n3.place(x=450, y=150)
        self.txt_n4.place(x=450, y=190)
        self.txt_media.place(x=260, y=240)


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
        self.foto_sair = ajustar_icone("exitt.png")

        self.btn_calcular = Button(self.tela, text="Calcular Média", image=self.foto_calcular, compound=TOP, command=self.calcularMedia)
        self.btn_ver= Button(self.tela, text="Ver Média", image=self.foto_ver, compound=TOP, command=self.mostrarMedia)
        self.btn_sair = Button(self.tela, text="Sair", image=self.foto_sair, compound=TOP, command=self.tela.destroy)
        
        self.btn_calcular.place(x=130, y=310)
        self.btn_ver.place(x=280, y=310)
        self.btn_sair.place(x=410, y=310)

    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_n1.delete(0, END)
        self.txt_n2.delete(0, END)
        self.txt_n3.delete(0, END)
        self.txt_n4.delete(0, END)
        
        self.txt_media.config(state="normal")
        self.txt_media.delete(0, END)
        self.txt_media.config(state="readonly")


    def calcularMedia(self):
        if not self.txt_codigo.get():
            messagebox.showerror("Erro", "O código é obrigatório!")
            return

        try:
            codigo = int(self.txt_codigo.get())
            nome = str(self.txt_nome.get())
            n1 = float(self.txt_n1.get())
            n2 = float(self.txt_n2.get())
            n3 = float(self.txt_n3.get())
            n4 = float(self.txt_n4.get())
        except ValueError:
            messagebox.showerror("Erro", "Código deve ser Inteiro e Notas devem ser Decimais (Use ponto ex: 7.5).")
            return

        media_final = (n1 + n2 + n3 + n4) / 4

        self.txt_media.config(state="normal")
        self.txt_media.delete(0, END)
        self.txt_media.insert(0, f"{media_final:.2f}")
        self.txt_media.config(state="readonly")

        dados_notas = {
            "codigo": codigo,
            "nomeAluno": nome,
            "nota1": n1,
            "nota2": n2,
            "nota3": n3,
            "nota4": n4,
            "media": media_final
        }

        self.collection.update_one({"codigo": codigo}, {"$set": dados_notas}, upsert=True)
        messagebox.showinfo("Sucesso", f"Média calculada e salva para {nome}!")
        self.limpar()


    def mostrarMedia(self):
        try:
            codigo = int(self.txt_codigo.get())
        except ValueError:
            messagebox.showwarning("Aviso", "Digite um código numérico válido para buscar.")
            return

        resultado = self.collection.find_one({"codigo": codigo})
        
        if resultado:
            self.limpar()
            
            self.txt_codigo.insert(0, str(resultado.get("codigo", "")))
            self.txt_nome.insert(0, str(resultado.get("nomeAluno", "")))
            self.txt_n1.insert(0, str(resultado.get("nota1", "")))
            self.txt_n2.insert(0, str(resultado.get("nota2", "")))
            self.txt_n3.insert(0, str(resultado.get("nota3", "")))
            self.txt_n4.insert(0, str(resultado.get("nota4", "")))
            
            self.txt_media.config(state="normal")
            self.txt_media.insert(0, f"{resultado.get('media', 0.0):.2f}")
            self.txt_media.config(state="readonly")
        else:
            messagebox.showwarning("Aviso", "Registro de notas não encontrado.")

# EXECUTAR
if __name__ == "__main__":
    CadastroNotas()