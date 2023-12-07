import tkinter as tk

def calcular_imc():
    altura = float(entry_altura.get())
    peso = float(entry_peso.get())
    imc = peso / (altura ** 2)
    resultado_imc['text'] = f"Seu IMC é: {imc:.2f}"

    if imc > 40:
        resultado_categoria['text'] = "Acima de 40,0 Obesidade grau III Aqui o sinal é vermelho, com forte probabilidade de já existirem doenças muito graves associadas. O tratamento deve ser ainda mais urgente."
    elif 35 < imc <= 40:
        resultado_categoria['text'] = "Entre 35,0 e 39,9 Obesidade grau II Mesmo que seus exames aparentem estar normais, é hora de se cuidar, iniciando mudanças no estilo de vida com o acompanhamento próximo de profissionais de saúde."
    elif 30 < imc <= 35:
        resultado_categoria['text'] = "Entre 30,0 e 34,9 Obesidade grau I Sinal de alerta! Chegou na hora de se cuidar, mesmo que seus exames sejam normais. Vamos dar início a mudanças hoje! Cuide de sua alimentação. Você precisa iniciar um acompanhamento com nutricionista e/ou endocrinologista."
    elif 25 < imc <= 30:
        resultado_categoria['text'] = "Entre 25,0 e 29,9 Sobrepeso Ele é, na verdade, uma pré-obesidade e muitas pessoas nessa faixa já apresentam doenças associadas, como diabetes e hipertensão. Importante rever hábitos e buscar ajuda antes de, por uma série de fatores, entrar na faixa da obesidade pra valer."
    elif 18.6 < imc <= 25:
        resultado_categoria['text'] = "Entre 18,6 e 24,9 Normal Que bom que você está com o peso normal! E o melhor jeito de continuar assim é mantendo um estilo de vida ativo e uma alimentação equilibrada."
    else:
        resultado_categoria['text'] = "18,5 ou menos Abaixo do normal Procure um médico. Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem. Outras podem estar enfrentando problemas, como a desnutrição. É preciso saber qual é o caso."

def reiniciar_programa():
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    resultado_imc['text'] = ""
    resultado_categoria['text'] = ""

root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("400x300")
root.configure(background="cyan1")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)
frame.configure(background='cyan1')

label_altura = tk.Label(frame, text="Digite sua altura (em metros):")
label_altura.configure(background='cyan1')
label_altura.pack()

entry_altura = tk.Entry(frame)
entry_altura.pack()

label_peso = tk.Label(frame, text="Digite seu peso (em kg):")
label_peso.configure(background='cyan1')
label_peso.pack()

entry_peso = tk.Entry(frame)
entry_peso.pack()

botao_calcular = tk.Button(frame, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack(pady=10)

resultado_imc = tk.Label(frame, text="", font=('Arial', 12, 'bold'))
resultado_imc.configure(background='cyan1')
resultado_imc.pack()

resultado_categoria = tk.Label(frame, text="", wraplength=400)
resultado_categoria.configure(background='cyan1')
resultado_categoria.pack()

botao_reiniciar = tk.Button(frame, text="Limpar", command=reiniciar_programa)
botao_reiniciar.pack(pady=10)

root.mainloop()
