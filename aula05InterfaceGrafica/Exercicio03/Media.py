from tkinter import *

class Media:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        self.__n1 = 0.0
        self.__n2 = 0.0
        self.__n3 = 0.0
        self.__media = 0.0

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

    @property
    def _n3(self):
        return self.__n3

    @_n3.setter
    def _n3(self, value):
        self.__n3 = value

    @property
    def _media(self):
        return self.__media

    @_media.setter
    def _media(self, value):
        self.__media = value

    def configurar_tela(self):
        self.tela.title("Calculo Media")
        self.tela.configure(background="#02473b")

        largura = 800
        altura = 500

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2

        self.tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))

    def criar_componentes(self):
        self.frame = Frame (self.tela, bg="#7ae9ae", padx=20, pady=20)
        self.frame.pack(expand=True)

        Label(self.frame, text="Calculo Media", bg="#7ae9ae", fg="black", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        #n1
        Label(self.frame, text="Digite a primeira nota: ").grid(row=1,column=0,sticky="w",pady=5)
        self.txt_n1 = Entry(self.frame)
        self.txt_n1.grid(row=1,column=1,pady=5)

        #n2
        Label(self.frame, text="Digite a segunda nota: ").grid(row=3,column=0,sticky="w",pady=5, padx=2)
        self.txt_n2 = Entry(self.frame)
        self.txt_n2.grid(row=3,column=1,pady=5)

        #n3
        Label(self.frame, text="Digite a terceira nota: ").grid(row=5,column=0,sticky="w",pady=5, padx=2)
        self.txt_n3 = Entry(self.frame)
        self.txt_n3.grid(row=5,column=1,pady=5)

        #resultado
        Label(self.frame, text="Resultado: ").grid(row=7,column=0,sticky="w",pady=5)
        self.txt_resul = Entry(self.frame)
        self.txt_resul.grid(row=7,column=1,pady=5)

        #botão
        self.btn_botao = Button(self.frame, text="Calcular Media", command=self.calcular)
        self.btn_botao.grid(row=9,column=0,columnspan=2,pady=15)

    def calcular(self):
        self.__n1 = float(self.txt_n1.get())
        self.__n2 = float(self.txt_n2.get())
        self.__n3 = float(self.txt_n3.get())
        self.__media = (self.__n1 + self.__n2 + self.__n3)/3

        self.txt_resul.insert(0, self.__media)

    def executar(self):
        self.tela.mainloop()

