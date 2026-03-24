from tkinter import *

class Cadastro:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        #ATRIBUTOS PRIVADOS
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

        #DEFINE O TAMANHO PADRÃO DA SUA TELA 
        largura = 800
        altura = 300

        #PEGA A LARGURA E ALTURA DA TELA DO WINDOWS
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        #DEFINE O POSICIONAMENTO CENTRALIZADO
        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2

        #CONSTROI A TELA DE ACORDO COM AS DIMENSÕES DA TELA DO WINDOWS
        # %D - SUBSTITUI CADA NÚMERO - % CONCATENA CADA VARIAVEL LARGURA, ALTURA
        self.tela.geometry("%dx%d+%d+%d"  % (largura,altura , posx,posy))

    def criar_componentes(self):
        #CRIAR FRAME 
        self.frame = Frame(self.tela, bg="#0e254c", padx=20, pady=20)
        #pack posiciona de acordo com a tela expand => ocupa espaço na tela ao redimensionar 
        self.frame.pack(expand=True)

        #TITULO
        self.titulo = Label(self.frame, text="Cadastro de Clientes")
        # grid => cria grade 
        # row => linha
        # column = coluna
        # columnspan = espaço interno da coluna
        # pady => espaçamento parte de cima e de baixo de 10px
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        #NOME
        #sticky => posicionamento do texto lado esquerdo (oeste)
        Label(self.frame, text="Digite o nome: ").grid(row=1, column=0, sticky="w", pady=5)
        
        self.txt_nome = Entry(self.frame)
        self.txt_nome.grid(row=1, column=1, pady=5)

        #EMAIL
        #sticky => posicionamento do texto lado esquerdo (oeste)
        Label(self.frame, text="DIgite o email: ").grid(row=3, column=0, sticky="w", pady=5)
        
        self.txt_email = Entry(self.frame)
        self.txt_email.grid(row=3, column=1, pady=5)

        #ENDERECO
        #sticky => posicionamento do texto lado esquerdo (oeste)
        Label(self.frame, text="DIgite o endereço: ").grid(row=5, column=0, sticky="w", pady=5)
        
        self.txt_endereco = Entry(self.frame)
        self.txt_endereco.grid(row=5, column=1, pady=5)

        #TELEFONE
        #sticky => posicionamento do texto lado esquerdo (oeste)
        Label(self.frame, text="DIgite o telefone: ").grid(row=6, column=0, sticky="w", pady=5)
        
        self.txt_telefone = Entry(self.frame)
        self.txt_telefone.grid(row=6, column=1, pady=5)

        #BOTÃO 
        self.btn_botao = Button(self.frame, text="Cadastrar Cliente", command=self.cadastrar)
        self.btn_botao.grid(row=8, column=0, columnspan=2, pady=15)

    def cadastrar(self):
        self.__nome = self.txt_nome.get()

        self.mostrarDados(self)

    def mostrarDados(self):
        self.txt_result.insert(0, "Nome: "+self.__nome, )

    def executar(self):
        self.tela.mainloop()