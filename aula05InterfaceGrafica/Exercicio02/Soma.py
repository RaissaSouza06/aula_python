from tkinter import *

class Soma:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        self.__n1 = 0
        self.__n2 = 0
        self.__soma = 0

    @property
    def _soma(self):
        return self.__soma

    @_soma.setter
    def _soma(self, value):
        self.__soma = value

    @property
    def _n1(self):
        return self.__n1

    @_n1.setter
    def _n1(self, value):
        self.__n1 = value

    @property
    def _n2(self):
        return self.__n2

    @_n2.setter
    def _n2(self, value):
        self.__n2 = value

    def configurar_tela(self):
        self.tela.title("Calculo Soma")
        self.tela.configure(background="#527ec9")

        largura = 800
        altura = 500

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2

        self.tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))

    def criar_componentes(self):
        self.frame = Frame (self.tela, bg="#0e254c", padx=20, pady=20)
        self.frame.pack(expand=True)

        self.titulo = Label(self.frame, text="Calculo soma")
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        #n1
        Label(self.frame, text="Digite um número: ").grid(row=1,column=0,sticky="w",pady=5)
        self.txt_n1 = Entry(self.frame)
        self.txt_n1.grid(row=1,column=1,pady=5)

        #n2
        Label(self.frame, text="Digite o 2º número: ").grid(row=3,column=0,sticky="w",pady=5, padx=2)
        self.txt_n2 = Entry(self.frame)
        self.txt_n2.grid(row=3,column=1,pady=5)

        #resultado
        Label(self.frame, text="Resultado: ").grid(row=4,column=0,sticky="w",pady=5)
        self.txt_resul = Entry(self.frame)
        self.txt_resul.grid(row=4,column=1,pady=5)

        #botão
        self.btn_botao = Button(self.frame, text="Calcular Soma", command=self.calcular)
        self.btn_botao.grid(row=5,column=0,columnspan=2,pady=15)

    def calcular(self):
        self.__n1 = float(self.txt_n1.get())
        self.__n2 = float(self.txt_n2.get())
        self.__soma = self.__n1 + self.__n2

        self.txt_resul.insert(0, self.__soma)

    def executar(self):
        self.tela.mainloop()