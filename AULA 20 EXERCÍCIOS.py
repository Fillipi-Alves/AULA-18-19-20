import tkinter as tk

janela  =  tk.Tk()
# janela('500x500')
janela.title('Isso é uma Janela')

def soma():
    n1 = float(input_entry1.get())
    n2 = float(input_entry2.get())
    soma  =  n1  + n2
    resultado.config(text=f'Resultado {int(soma)}')


def sub():
    n1 = float(input_entry1.get())
    n2 = float(input_entry2.get())
    sub  =  n1  - n2
    resultado.config(text=f'Resultado {int(sub)}')

def div():
    n1 = float(input_entry1.get())
    n2 = float(input_entry2.get())
    div  =  n1  // n2
    resultado.config(text=f'Resultado {div}')

def mult():
    n1 = float(input_entry1.get())
    n2 = float(input_entry2.get())
    mult  =  n1  * n2
    resultado.config(text=f'Resultado {mult}')


text_label =  tk.Label(janela, text='CALCULADORA', fg = 'black', bg='white')
text_label.grid(row = 0, column = 1)
# text_label.pack()


input_entry1 = tk.Entry(janela, width = 5)
input_entry1.grid(row = 2, column = 2 , padx = 10)
# input_entry1.pack()

input_entry2 = tk.Entry(janela, width = 5)
input_entry2.grid(row = 2, column = 4, padx = 10 )
# input_entry2.pack()


btn_soma  = tk.Button(janela, text= '+', command = soma, fg='white', bg='black')
btn_soma.grid(row = 3, column = 3, padx = 10, pady=10)
# btn_soma.pack()  

btn_sub  = tk.Button(janela, text= '-', command = sub, fg='white', bg='black')
btn_sub.grid(row = 3, column = 2, padx = 10, pady=10)
# btn_sub.pack()  

btn_div  = tk.Button(janela, text= '/', command = div, fg='white', bg='black')
btn_div.grid(row = 3, column = 4, padx = 10, pady=10)
# btn_div.pack()  

btn_mult  = tk.Button(janela, text= '*', command = mult, fg='white', bg='black')
btn_mult.grid(row = 3, column = 5, padx = 10, pady=10)
# btn_mult.pack()  

resultado =  tk.Label(janela, text='Resultado')
resultado.grid(row = 2, column = 6, padx = 5, pady=5)
# resultado.pack()

janela.mainloop()



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


import tkinter as tk
from tkinter import messagebox

# Função para calcular o IMC
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        if altura <= 0:
            messagebox.showerror("Erro", "A altura deve ser maior que zero.")
            return
        imc = peso / (altura ** 2)
        resultado.set(f"IMC: {imc:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("500x500")

tk.Label(root, text="Peso (kg):").pack(pady=10)
entry_peso = tk.Entry(root)
entry_peso.pack(pady=10)

tk.Label(root, text="Altura (m):").pack(pady=10)
entry_altura = tk.Entry(root)
entry_altura.pack(pady=10)

# Criar o botão para calcular o IMC
btn_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc)
btn_calcular.pack(pady=20)

# Rótulo para mostrar o resultado
resultado = tk.StringVar()
resultado.set("IMC: ")
label_resultado = tk.Label(root, textvariable=resultado)
label_resultado.pack(pady=20)

# Adicionar botões adicionais para operações
btn_clear = tk.Button(root, text="Limpar", command=lambda: (entry_peso.delete(0, tk.END), entry_altura.delete(0, tk.END), resultado.set("IMC: ")))
btn_clear.pack(pady=10)


# Iniciar o loop principal da interface gráfica
root.mainloop()