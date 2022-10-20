from tkinter import *

# cores

cor1 = "#66CDAA"

principal = Tk()  # cria a tela
principal.title("Conversor de medidas") #adiciona título
principal.configure(background=cor1)  # definindo cor de fundo
principal.geometry("300x300") # definindo tamanho

label1 = Label(principal, text = 'Insira o valor em centrímetros:', background=cor1) #definindo label
label1.place(x=50, y=70) #definindo posição label

entrada = Entry(principal) #definindo entrada
entrada.place(x=50,y=100) #definindo posição da entrada

def bt_click(): #função para conversão de valores
  num1 = int(entrada.get())
  label2["text"] = round(num1/ 2.54)
  
botao = Button(principal, text="Calcular", command=bt_click) #botão para chamar função de conversão
botao.place(x=50,y=130) #localização do botão

label2 = Label(principal, text="Valor em polegadas:", background=cor1) #label para receber o valor convertido
label2.place(x=50,y=170) #localização do label

principal.mainloop() #manter janela aberta