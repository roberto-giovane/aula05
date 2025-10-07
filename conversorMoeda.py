import tkinter as tk
from moeda import apidolar

# fução que consome uma api publica

def dolar():
    cotacao = float(apidolar())
    reais = float(valor.get())
    conta = round(reais / cotacao,2)
    mensagem = f'Com R$ {reais:.2f} reais compra-se $ {conta} dólares'
    resposta.config(text=mensagem)
    #return mensagem

janela = tk.Tk()
janela.geometry('500x300')
janela.title('Aula 04 - Tkinter')
janela.configure(bg='#042940')

titulo = tk.Label(janela, text='converson de reais para dolar', font=('verdana', 16), fg='#D6D58E', bg='#042940')
titulo.pack(pady=10)

rotulo = tk.Label(janela, text='Digite o valor em reais para converter: ', font=('verdana',12), fg='#D6D58E', bg='#042940')
rotulo.pack(pady=10)

valor = tk.Entry(janela, bg='#D6D58E', fg='#042940')
valor.pack(pady=10)

botao = tk.Button(janela, text='converter', command=dolar, bg='#9FC131', fg='#005C53')
botao.pack(pady=10)

resposta = tk.Label(janela, text=' ', font=('verdana',12), fg='#D6D58E', bg='#042940')
resposta.pack(pady=10)

janela.mainloop()