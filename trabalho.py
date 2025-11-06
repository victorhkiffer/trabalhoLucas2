import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import re
from PyPDF2 import PdfReader  


def escolher_pdf():
    caminho = filedialog.askopenfilename(
        title="Selecionar um arquivo PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )

    if caminho:
        label_arquivo.config(text=f"Arquivo selecionado: {caminho}")
        verificar_feriados_no_pdf(caminho)
    else:
        messagebox.showinfo("Aviso", "Nenhum arquivo foi selecionado.")


def buscar_feriados():
    try:
        response = requests.get("https://date.nager.at/api/v3/PublicHolidays/2025/BR")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Não foi possível buscar os feriados: {e}")
        return []


def verificar_feriados_no_pdf(caminho_pdf):
    try:
        # Lendo o conteúdo do PDF
        leitor = PdfReader(caminho_pdf)
        texto_pdf = ""
        for pagina in leitor.pages:
            texto_pdf += pagina.extract_text()

        
        datas_no_pdf = re.findall(r"\d{4}-\d{2}-\d{2}", texto_pdf)

        
        feriados = buscar_feriados()
        datas_feriados = {feriado["date"]: feriado["localName"] for feriado in feriados}

        
        resultado = "Verificação de Feriados:\n"
        for data in datas_no_pdf:
           
            data_formatada = f"{data[8:10]}/{data[5:7]}/{data[0:4]}"
            if data in datas_feriados:
                resultado += f"A data {data_formatada} encontrada no PDF é feriado: {datas_feriados[data]}.\n"
            else:
                resultado += f"A data {data_formatada} encontrada no PDF não é feriado.\n"

        
        label_feriados.config(text=resultado)

    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível processar o PDF: {e}")


janela = tk.Tk()
janela.title("Leitor PDF - Verificar Feriados")
janela.geometry("500x500")

label_instrucao = tk.Label(janela, text="Escolha um arquivo PDF para verificar feriados:")
label_instrucao.pack(pady=10)

botao_escolher = tk.Button(janela, text="Selecionar PDF", command=escolher_pdf)
botao_escolher.pack(pady=10)

label_arquivo = tk.Label(janela, text="")
label_arquivo.pack(pady=10)

label_feriados = tk.Label(janela, text="", justify="left", wraplength=400)
label_feriados.pack(pady=10)

janela.mainloop()