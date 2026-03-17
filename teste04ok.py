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
    # Pega o texto do textbox, remove espaços vazios e cria uma lista de termos
    texto_busca = entry_dado.get("0.0", "end").strip()
    termos = [linha.strip() for linha in texto_busca.split('\n') if linha.strip()]
    pasta = entry_pasta.get().strip()

    if not termos:
        messagebox.showwarning("Aviso", "Insira ao menos um termo para buscar.")
        return

    if not pasta or not os.path.isdir(pasta):
        messagebox.showwarning("Aviso", "Selecione uma pasta válida.")
        return

    resultado_text.delete("0.0", "end")
    btn_buscar.configure(state="disabled")

    try:
        for item in termos:
            encontrado_este_item = False
            termo_lower = item.lower()
            
            # Informa qual item está sendo processado agora
            label_status.configure(text=f"Buscando: {item}", text_color="yellow")
            resultado_text.insert("end", f"--- Buscando por: {item} ---\n")
            resultado_text.see("end")

            # Inicia a varredura de pastas para o item atual
            for root, dirs, files in os.walk(pasta):
                if encontrado_este_item:
                    break # Para de andar nas pastas se já achou o item

                for arquivo in files:
                    if arquivo.endswith(".csv"):
                        caminho = os.path.join(root, arquivo)
                        
                        try:
                            with open(caminho, newline='', encoding="utf-8") as csvfile:
                                leitor = csv.reader(csvfile)
                                for linha_num, linha in enumerate(leitor, start=1):
                                    if any(termo_lower in str(campo).lower() for campo in linha):
                                        resultado_text.insert("end", f"✅ ACHOU: {item}\n📄 {arquivo} (Linha {linha_num})\n📍 {caminho}\n\n")
                                        resultado_text.see("end")
                                        encontrado_este_item = True
                                        break # Sai do arquivo
                        except:
                            continue
                
                if encontrado_este_item:
                    break # Sai do os.walk e vai para o próximo item da lista principal

            if not encontrado_este_item:
                resultado_text.insert("end", f"❌ NÃO ENCONTRADO: {item}\n\n")
                resultado_text.see("end")

        label_status.configure(text="Busca em lote concluída!", text_color="#00FF00")
        
    finally:
        btn_buscar.configure(state="normal")

def iniciar_busca():
    threading.Thread(target=thread_busca, daemon=True).start()

# ---------------- INTERFACE ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Scanner CSV em Lote")
app.geometry("600x750")

frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True, padx=20, pady=20)

# Campo para lista de termos
ctk.CTkLabel(frame, text="Lista de itens (um por linha):", font=("Arial", 12, "bold")).pack(anchor="w")
entry_dado = ctk.CTkTextbox(frame, width=540, height=120, border_width=1)
entry_dado.pack(pady=5)
entry_dado.insert("0.0", "Inserir Serial") # Exemplo inicial

# Campo para pasta
ctk.CTkLabel(frame, text="Pasta raiz para busca:", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10,0))
entry_pasta = ctk.CTkEntry(frame, width=540)
entry_pasta.pack(pady=5)

btn_pasta = ctk.CTkButton(frame, text="Selecionar Pasta", fg_color="transparent", border_width=1, command=escolher_pasta)
btn_pasta.pack(pady=5)

btn_buscar = ctk.CTkButton(frame, text="INICIAR BUSCA", font=("Arial", 13, "bold"), command=iniciar_busca)
btn_buscar.pack(pady=15)

# Status e Resultados
label_status = ctk.CTkLabel(frame, text="Aguardando lista...", font=("Arial", 11, "italic"))
label_status.pack(pady=(0, 5))

resultado_text = ctk.CTkTextbox(frame, width=540, height=300, font=("Consolas", 11), fg_color="#1a1a1a")
resultado_text.pack(fill="both", expand=True)

app.mainloop()