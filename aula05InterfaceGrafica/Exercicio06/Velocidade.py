from tkinter import *

class Velocidade:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        self.__nome = ""
        self.__distancia = 0.0
        self.__tempo = 0.0
        self.__velocidade = 0.0

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _distancia(self):
        return self.__distancia

    @_distancia.setter
    def _distancia(self, value):
        self.__distancia = value

    @property
    def _tempo(self):
        return self.__tempo

    @_tempo.setter
    def _tempo(self, value):
        self.__tempo = value

    @property
    def _velocidade(self):
        return self.__velocidade

    @_velocidade.setter
    def _velocidade(self, value):
        self.__velocidade = value


    def configurar_tela(self):
        self.tela.title("Calculo Velocidade")
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

        self.titulo = Label(self.frame, text="Calculo Velocidade")
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        #n1
        Label(self.frame, text="Nome do carro: ").grid(row=1,column=0,sticky="w",pady=5)
        self.txt_nome = Entry(self.frame)
        self.txt_nome.grid(row=1,column=1,pady=5)

        #n2
        Label(self.frame, text="Distância Percorrida em Km: ").grid(row=3,column=0,sticky="w",pady=5, padx=2)
        self.txt_distancia = Entry(self.frame)
        self.txt_distancia.grid(row=3,column=1,pady=5)

        #n3
        Label(self.frame, text="Tempo em Minutos: ").grid(row=5,column=0,sticky="w",pady=5, padx=2)
        self.txt_tempo = Entry(self.frame)
        self.txt_tempo.grid(row=5,column=1,pady=5)

        #resultado
        Label(self.frame, text="Velocidade do Carro: ").grid(row=7,column=0,sticky="w",pady=5)
        self.txt_velocidade = Entry(self.frame)
        self.txt_velocidade.grid(row=7,column=1,pady=5)

        self.lbl_dados = Label(self.frame, text="", bg="#02473b", fg="white", font=("Arial", 10), width=40, height=5, pady=10)
        self.lbl_dados.grid(row=8, column=0, columnspan=2, pady=10)

        #botão
        self.btn_botao = Button(self.frame, text="Calcular Velocidade", command=self.calcularVelocidade)
        self.btn_botao.grid(row=9,column=0,columnspan=2,pady=15)

    def calcularVelocidade(self):
        self.__nome= self.txt_nome.get()
        self.__distancia = float(self.txt_distancia.get())
        self.__tempo = float(self.txt_tempo.get())
        self.__velocidade = (self.__distancia * 1000) / (self.__tempo * 60)

        self.txt_velocidade.insert(0, self.__velocidade)
        self.mostrarResultado()

    def mostrarResultado(self):
        texto = (f"O carro: {self.__nome}\n"
                 f"Percorreu: {self._distancia} metros\n"
                 f"Em um tempo de: {self.__tempo} segundos\n"
                 f"Velocidade: {self.__velocidade} m/s")
        
        self.lbl_dados.config(text=texto)

    def executar(self):
        self.tela.mainloop()

