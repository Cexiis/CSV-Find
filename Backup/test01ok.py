import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import csv

def escolher_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        entry_pasta.delete(0, "end")
        entry_pasta.insert(0, pasta)

def buscar_dado():
    dado = entry_dado.get().strip()
    pasta = entry_pasta.get().strip()

    if not dado:
        messagebox.showwarning("Aviso", "Digite um dado para buscar.")
        return

    if not pasta or not os.path.isdir(pasta):
        messagebox.showwarning("Aviso", "Selecione uma pasta válida.")
        return

    resultado_text.delete("0.0", "end")
    encontrado = False

    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".csv"):
            caminho = os.path.join(pasta, arquivo)

            try:
                with open(caminho, newline='', encoding="utf-8") as csvfile:
                    leitor = csv.reader(csvfile)
                    for linha_num, linha in enumerate(leitor, start=1):
                        if any(dado.lower() in str(campo).lower() for campo in linha):
                            resultado_text.insert("end", f"Encontrado no arquivo: {arquivo}\n")
                            resultado_text.insert("end", f"Linha {linha_num}: {linha}\n\n")
                            encontrado = True

            except Exception as e:
                resultado_text.insert("end", f"Erro ao ler {arquivo}: {e}\n\n")

    if not encontrado:
        resultado_text.insert("end", "Nenhum resultado encontrado.")

# ---------------- INTERFACE ----------------

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Buscador em CSV")
app.geometry("650x500")

# Frame principal
frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True, padx=20, pady=20)

# ----- Entrada do dado -----
label_dado = ctk.CTkLabel(frame, text="Digite o dado para buscar:")
label_dado.pack(anchor="w")

entry_dado = ctk.CTkEntry(frame, width=350)
entry_dado.pack(pady=5)

# ----- Seleção da pasta -----
label_pasta = ctk.CTkLabel(frame, text="Selecione a pasta com arquivos CSV:")
label_pasta.pack(anchor="w", pady=(20, 0))

entry_pasta = ctk.CTkEntry(frame, width=350)
entry_pasta.pack(pady=5)

btn_pasta = ctk.CTkButton(frame, text="Escolher pasta", command=escolher_pasta)
btn_pasta.pack()

# ----- Botão de busca -----
btn_buscar = ctk.CTkButton(frame, text="Buscar", command=buscar_dado)
btn_buscar.pack(pady=20)

# ----- Resultado -----
resultado_text = ctk.CTkTextbox(frame, width=580, height=220)
resultado_text.pack()

app.mainloop()
