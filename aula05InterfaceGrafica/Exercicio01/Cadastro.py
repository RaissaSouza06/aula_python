from tkinter import *

class Cadastro:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        self.__nome = ""
        self.__telefone = ""
        self.__endereco = ""
        self.__email = ""

    @property
    def _email(self):
        return self.__email

    @_email.setter
    def _email(self, value):
        self.__email = value

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _telefone(self):
        return self.__telefone

    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value

    @property
    def _endereco(self):
        return self.__endereco

    @_endereco.setter
    def _endereco(self, value):
        self.__endereco = value

    def configurar_tela(self):
        self.tela.title("Aplicação O_O")
        self.tela.configure(background="#09232E")

        largura = 800
        altura = 500

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2

        self.tela.geometry("%dx%d+%d+%d"  % (largura,altura , posx,posy))

    def criar_componentes(self):
        self.frame = Frame(self.tela, bg="#09232E", padx=20, pady=20)
        self.frame.pack(expand=True)

        estilo = {"bg": "#09232E", "fg": "white", "font": ("Arial", 10, "bold")}

        # TITULO
        Label(self.frame, text="CADASTRO DE CLIENTES", bg="#09232E", fg="white", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        Label(self.frame, text="Digite o nome:").grid(row=1, column=0, sticky="w", pady=2)
        self.txt_nome = Entry(self.frame)
        self.txt_nome.grid(row=1, column=1, pady=2)

        Label(self.frame, text="Digite o email:").grid(row=2, column=0, sticky="w", pady=2)
        self.txt_email = Entry(self.frame)
        self.txt_email.grid(row=2, column=1, pady=2)

        Label(self.frame, text="Digite o endereço:").grid(row=3, column=0, sticky="w", pady=2)
        self.txt_endereco = Entry(self.frame)
        self.txt_endereco.grid(row=3, column=1, pady=2)

        Label(self.frame, text="Digite o telefone:").grid(row=4, column=0, sticky="w", pady=2)
        self.txt_telefone = Entry(self.frame)
        self.txt_telefone.grid(row=4, column=1, pady=2)

        self.btn_botao = Button(self.frame, text="Cadastrar Cliente", command=self.cadastrarCliente, bg="#00CED1", fg="black", font=("Arial", 10, "bold"))
        self.btn_botao.grid(row=5, column=0, columnspan=2, pady=15)

        self.lbl_resultado_titulo = Label(self.frame, text="", **estilo)
        self.lbl_resultado_titulo.grid(row=6, column=0, columnspan=2)

        self.lbl_dados = Label(self.frame, text="", bg="white", fg="black", width=40, height=6, relief="sunken", font=("Courier", 9))
        self.lbl_dados.grid(row=7, column=0, columnspan=2, pady=5)

    def cadastrarCliente(self):
        self.__nome = self.txt_nome.get()
        self.__email = self.txt_email.get()
        self.__endereco = self.txt_endereco.get()
        self.__telefone = self.txt_telefone.get()
        
        self.mostrarDados()

    def mostrarDados(self):
        self.lbl_resultado_titulo.config(text="Dados do Cliente")
        
        texto = (f"Nome: {self.__nome}\n"
                 f"E-mail: {self.__email}\n"
                 f"Endereço: {self.__endereco}\n"
                 f"Telefone: {self.__telefone}")
        
        self.lbl_dados.config(text=texto)

    def executar(self):
        self.tela.mainloop()