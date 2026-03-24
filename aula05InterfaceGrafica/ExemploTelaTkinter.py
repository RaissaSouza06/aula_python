from tkinter import * 
# criando tela do Tkinter - Interafec
tela = Tk()

#titulo
tela.title("Fatec Registro")

#cor de fundo
tela.configure(background="#3dd44c")

#tamanho da tela
tela.geometry("700x500")

#redimensionar tela true=habilitada / falsa=desabilitada
tela.resizable(True,True)

#tamanho maximo e minimo para redimensionar
tela.minsize(width=400, height=600)
tela.maxsize(width=700, height=800)

#CRIANDO LABEL
Lbl_nome = Label(tela, text="Digite seu nome: " , background="#3dd44c", foreground="#000000", font="Arial 10 bold italic").place(x=20,y=20)
lbl_telefone = Label(tela, text="Digite  o telefone: ", bg="#3dd44c", fg="#000000", font=("Ariel","10", "bold", "italic")).place(x=20,y=60)

#CRIANDO CAIXA DE TEXTO
txt_nome = Entry(tela, width=50, borderwidth=3, bg="#297ce1", fg="white")
txt_nome.place(x=140, y=20)
txt_telefone = Entry(tela, width=20, borderwidth=3, bg="#297ce1", fg="white")
txt_telefone.place(x=140, y=60)

#CRIANDO BOTÃO - primeiro criar a função
def mostradados():
    lbl_mostra = Label(tela, text="Bem vindo: " + txt_nome.get() + "\nTelefone: " + txt_telefone.get())
    lbl_mostra.place(x=100,y=150)
btn_botao = Button(tela, text="Mostrar Dados", command=mostradados)
btn_botao.place(x = 160, y = 100) 
#pack define que o botão deve estar colado no seu componente pai -  tela


#executando a tela
tela.mainloop()
