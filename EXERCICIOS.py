import tkinter as tk
from tkinter import messagebox

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

# Criar a janela 
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


resultado = tk.StringVar()
resultado.set("IMC: ")
label_resultado = tk.Label(root, textvariable=resultado)
label_resultado.pack(pady=20)


btn_clear = tk.Button(root, text="Limpar", command=lambda: (entry_peso.delete(0, tk.END), entry_altura.delete(0, tk.END), resultado.set("IMC: ")))
btn_clear.pack(pady=10)

root.mainloop()