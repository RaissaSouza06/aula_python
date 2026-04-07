from tkinter import *

class Produto:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        self.__nome = ""
        self.__qtd = 0
        self.__preco = 0.0
        self.__total = 0.0

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _qtd(self):
        return self.__qtd

    @_qtd.setter
    def _qtd(self, value):
        self.__qtd = value

    @property
    def _preco(self):
        return self.__preco

    @_preco.setter
    def _preco(self, value):
        self.__preco = value

    @property
    def _total(self):
        return self.__total

    @_total.setter
    def _total(self, value):
        self.__total = value

    def configurar_tela(self):
        self.tela.title("Calculo Produto")
        self.tela.configure(background="#46002F")

        largura = 800
        altura = 500

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2

        self.tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))

    def criar_componentes(self):
        self.frame = Frame (self.tela, bg="#a43193", padx=20, pady=20)
        self.frame.pack(expand=True)

        Label(self.frame, text="Calculo Total Produto", bg="#a43193", fg="black", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        #nome
        Label(self.frame, text="Digite o nome do produto: ").grid(row=1,column=0,sticky="w",pady=5)
        self.txt_nome = Entry(self.frame)
        self.txt_nome.grid(row=1,column=1,pady=5)

        #qtd
        Label(self.frame, text="Digite a quantidade comprada: ").grid(row=3,column=0,sticky="w",pady=5, padx=2)
        self.txt_qtd = Entry(self.frame)
        self.txt_qtd.grid(row=3,column=1,pady=5)

        #preço
        Label(self.frame, text="Digite o preço do produto: ").grid(row=5,column=0,sticky="w",pady=5, padx=2)
        self.txt_preco = Entry(self.frame)
        self.txt_preco.grid(row=5,column=1,pady=5)

        #total
        Label(self.frame, text="Valor total do produto: ").grid(row=7,column=0,sticky="w",pady=5)
        self.txt_total = Entry(self.frame)
        self.txt_total.grid(row=7,column=1,pady=5)

        self.lbl_resumo = Label(self.frame, text="", bg="#e16cc6", fg="#000000", font=("Courier", 12, "bold"), width=40, height=6, justify=LEFT, anchor="nw", padx=10, pady=10)
        self.lbl_resumo.grid(row=9, column=0, columnspan=2, pady=20)

        #botão
        self.btn_botao = Button(self.frame, text="Total", command=self.calcular)
        self.btn_botao.grid(row=11,column=0,columnspan=2,pady=15)

    def calcular(self):
        self.__qtd = int(self.txt_qtd.get())
        self.__preco = float(self.txt_preco.get())
        self.__total = self.__qtd * self.__preco

        self.txt_total.insert(0, self.__total)
        self.__nome = self.txt_nome.get()
        self.mostrarDadosProduto()

    def mostrarDadosProduto(self):
        texto_resumo = (
            f"Nome do produto: {self.__nome}\n"
            f"Preço R${self.__preco:.2f}\n"
            f"Quantidade: {self.__qtd}\n\n"
            f"Valor total R${self.__total:.2f}"
        )
        self.lbl_resumo.config(text=texto_resumo)

    def executar(self):
        self.tela.mainloop()
