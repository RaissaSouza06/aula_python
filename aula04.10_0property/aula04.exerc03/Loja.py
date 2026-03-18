class Loja:
    def __init__(self):
        self.__razaoSocial = ""
        self.__cpfCliente = ""
        self.__valorCompra = 0.0
        self.__qtdItensCompra = 0
        self.__valorTotalCompra = 0.0

    @property
    def _razaoSocial(self):
        return self.__razaoSocial

    @_razaoSocial.setter
    def _razaoSocial(self, value):
        self.__razaoSocial = value

    @property
    def _cpfCliente(self):
        return self.__cpfCliente

    @_cpfCliente.setter
    def _cpfCliente(self, value):
        self.__cpfCliente = value

    @property
    def _valorCompra(self):
        return self.__valorCompra

    @_valorCompra.setter
    def _valorCompra(self, value):
        self.__valorCompra = value

    @property
    def _qtdItensCompra(self):
        return self.__qtdItensCompra

    @_qtdItensCompra.setter
    def _qtdItensCompra(self, value):
        self.__qtdItensCompra = value

    @property
    def _valorTotalCompra(self):
        return self.__valorTotalCompra

    @_valorTotalCompra.setter
    def _valorTotalCompra(self, value):
        self.__valorTotalCompra = value

    def inserirDadosLoja(self):
        self.__razaoSocial = input("Digite a razão social: ")
        self.__cpfCliente = input("Digite o CPF do cliente: ")
        self.__valorCompra = float(input("Digite o valor unitário da compra: "))
        self.__qtdItensCompra = int(input("Digite a quantidade de itens comprados: "))
        
    def calcularCompraLoja(self):
        self.__valorTotalCompra = self.__valorCompra * self.__qtdItensCompra
        return self.__valorTotalCompra    
    
    def mostrarDadosLoja(self):
        return (f"\n---Dados da loja---\n"
                f"Razão social da loja: {self.__razaoSocial}\n"
                f"CPF do cliente: {self.__cpfCliente}\n"
                f"Valor unitário do produto: {self.__valorCompra:.2f}\n"
                f"Quantidade de itens comprados: {self.__qtdItensCompra}\n"
                f"Valor total: {self.__valorTotalCompra:.2f}")
