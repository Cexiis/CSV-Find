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

    # Agora usa os.walk() para percorrer TUDO (pasta + subpastas)
    for root, dirs, files in os.walk(pasta):
        for arquivo in files:
            if arquivo.endswith(".csv"):
                caminho = os.path.join(root, arquivo)

                try:
                    with open(caminho, newline='', encoding="utf-8") as csvfile:
                        leitor = csv.reader(csvfile)
                        for linha_num, linha in enumerate(leitor, start=1):
                            if any(dado.lower() in str(campo).lower() for campo in linha):
                                resultado_text.insert("end", f"Encontrado no arquivo: {caminho}\n")
                                resultado_text.insert("end", f"Linha {linha_num}: {linha}\n\n")
                                encontrado = True

                except Exception as e:
                    resultado_text.insert("end", f"Erro ao ler {caminho}: {e}\n\n")

    if not encontrado:
        resultado_text.insert("end", "Nenhum resultado encontrado.")

# ---------------- INTERFACE ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Buscador em CSV")
app.geometry("450x500")

frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True, padx=20, pady=20)

label_dado = ctk.CTkLabel(frame, text="Digite o dado para buscar:")
label_dado.pack(anchor="w")

entry_dado = ctk.CTkEntry(frame, width=350)
entry_dado.pack(pady=5)

label_pasta = ctk.CTkLabel(frame, text="Selecione a pasta com arquivos CSV:")
label_pasta.pack(anchor="w", pady=(20, 0))

entry_pasta = ctk.CTkEntry(frame, width=350)
entry_pasta.pack(pady=5)

btn_pasta = ctk.CTkButton(frame, text="Escolher pasta", command=escolher_pasta)
btn_pasta.pack()

btn_buscar = ctk.CTkButton(frame, text="Buscar", command=buscar_dado)
btn_buscar.pack(pady=20)

resultado_text = ctk.CTkTextbox(frame, width=580, height=220)
resultado_text.pack()

app.mainloop()
