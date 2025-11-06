import tkinter as tk
from tkinter import filedialog, messagebox

def escolher_pdf():
    caminho = filedialog.askopenfilename(
        title="selecionar um arquivo Pdf",
        filetypes=[("arqeuvios pdf", "*.pdf")]
    )

    if caminho :
        label_arquivo.config(text =f"Arquivo selecionado:\{caminho}")
    else:
        messagebox.showinfo("aviso", "nenhum arquivo foi selecionado.")


janela = tk.Tk()
janela.title("leitor PDF - Selecionar Arquivo")
janela.geometry("400x200")


label_instrucao = tk.Label(janela, text="Escolha um arquivo PDF para continuar:")
label_instrucao.pack(pady =10)

botao_escolher = tk.Button(janela, text="Selecionar PDF", command=escolher_pdf)
botao_escolher.pack(pady=10)


label_arquivo = tk.Label(janela, text="")
label_arquivo.pack(pady=10)

janela.mainloop()