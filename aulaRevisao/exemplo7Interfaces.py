from tkinter import * 

# definições da tela
tela = Tk()
tela.title("Título")
tela.configure(background="#a9f")
tela.geometry("700x600")

# definições componentes
# base
lbl_base = Label(tela, text="Digite a base: ", font="Arial 15", fg="#f0ffff")
lbl_base.place(x=10, y=15)

txt_base = Entry(tela, width=20, fg="blue")
txt_base.place(x=150, y = 15)

#altura
lbl_altura = Label(tela, text="Digite a altura: ", font="Arial 15", fg="#f0ffff")
lbl_altura.place(x=10, y=45)

txt_altura = Entry(tela, width=20, fg="blue")
txt_altura.place(x=150, y = 45)

#resultado
lbl_resultado = Label(tela, text="Resultado: ", font="Arial 15", fg="#f0ffff")
lbl_resultado.place(x=10, y=115)

txt_resultado = Entry(tela, width=20, fg="blue")
txt_resultado.place(x=125, y = 115)

#botão
btn_botao = Button(tela, text="Calcular Area", bg="red", command=calcularArea, width=30)
btn_botao.place(x=25, y=200)

def calcularArea():
    area = float(txt_base.get()) * float(txt_altura.get())/2
    txt_resultado.insert(0,f"A area é {area:.2f}")