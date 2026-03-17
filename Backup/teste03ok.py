import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import csv
import threading

def escolher_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        entry_pasta.delete(0, "end")
        entry_pasta.insert(0, pasta)

def thread_busca():
    dado = entry_dado.get().strip().lower()
    pasta = entry_pasta.get().strip()

    if not dado:
        messagebox.showwarning("Aviso", "Digite um dado para buscar.")
        return

    if not pasta or not os.path.isdir(pasta):
        messagebox.showwarning("Aviso", "Selecione uma pasta válida.")
        return

    resultado_text.delete("0.0", "end")
    btn_buscar.configure(state="disabled")
    encontrado = False

    try:
        for root, dirs, files in os.walk(pasta):
            # Atualiza qual pasta está sendo verificada em tempo real
            label_status.configure(text=f"Verificando: ...{root[-30:]}", text_color="yellow")
            app.update_idletasks()

            for arquivo in files:
                if arquivo.endswith(".csv"):
                    caminho = os.path.join(root, arquivo)

                    try:
                        with open(caminho, newline='', encoding="utf-8") as csvfile:
                            leitor = csv.reader(csvfile)
                            for linha_num, linha in enumerate(leitor, start=1):
                                if any(dado in str(campo).lower() for campo in linha):
                                    # EXIBE O RESULTADO
                                    resultado_text.insert("end", f"✅ ENCONTRADO!\n")
                                    resultado_text.insert("end", f"Arquivo: {arquivo}\n")
                                    resultado_text.insert("end", f"Caminho: {caminho}\n")
                                    resultado_text.insert("end", f"Linha {linha_num}: {linha}\n")
                                    
                                    label_status.configure(text="Busca finalizada: Item encontrado", text_color="#00FF00")
                                    encontrado = True
                                    return # <--- PARA A EXECUÇÃO DE TUDO ASSIM QUE ENCONTRA
                                    
                    except Exception as e:
                        # Erros de leitura individuais não param a busca total, apenas pulam o arquivo
                        continue

        if not encontrado:
            label_status.configure(text="Concluído: Nada encontrado", text_color="red")
            resultado_text.insert("end", "Nenhum resultado correspondente foi localizado.")
    
    finally:
        # Reativa o botão independentemente de ter encontrado ou não
        btn_buscar.configure(state="normal")

def iniciar_busca():
    busca_thread = threading.Thread(target=thread_busca)
    busca_thread.daemon = True
    busca_thread.start()

# ---------------- INTERFACE ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Busca Rápida CSV")
app.geometry("500x550")

frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True, padx=20, pady=20)

ctk.CTkLabel(frame, text="Termo de Busca:", font=("Arial", 12, "bold")).pack(anchor="w")
entry_dado = ctk.CTkEntry(frame, width=440)
entry_dado.pack(pady=5)

ctk.CTkLabel(frame, text="Diretório Raiz:", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10,0))
entry_pasta = ctk.CTkEntry(frame, width=440)
entry_pasta.pack(pady=5)

btn_pasta = ctk.CTkButton(frame, text="Selecionar Pasta", fg_color="transparent", border_width=1, command=escolher_pasta)
btn_pasta.pack(pady=5)

btn_buscar = ctk.CTkButton(frame, text="INICIAR BUSCA", font=("Arial", 13, "bold"), command=iniciar_busca)
btn_buscar.pack(pady=20)

# Label de Status em tempo real
label_status = ctk.CTkLabel(frame, text="Aguardando...", font=("Arial", 11, "italic"))
label_status.pack(pady=(0, 5))

resultado_text = ctk.CTkTextbox(frame, width=440, height=200, font=("Consolas", 11))
resultado_text.pack(fill="both", expand=True)

app.mainloop()