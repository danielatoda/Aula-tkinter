from tkinter import *

# cores
cor1 = "#66CDAA"

principal = Tk()  # cria a tela
principal.title("Conversor de medidas")
principal.configure(background=cor1)  # definindo cor de fundo
#principal.iconbitmap("calculadora.ico")
altura = 300
largura = 300

# dimensões do formulário
largura_formulario = principal.winfo_screenwidth()
altura_formulario = principal.winfo_screenheight()

# posição do formulário
posx = largura_formulario/2 - largura/2
posy = altura_formulario/2- altura/2

# geometry
principal.geometry("%dx%d+%d+%d" %(largura, altura, posx, posy))

# botões
botao_calcular = Button(principal, text = "Calcular")
botao_calcular.pack()

#loop infinito para a janela permanecer on
principal.mainloop()