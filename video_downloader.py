import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import threading

downloads = {}

def download_video():
    link = link_entry.get()
    save_path = folder_path.get()

    if not link:
        messagebox.showerror("Erro", "Por favor, insira um link de vídeo.")
        return

    if not save_path:
        messagebox.showerror("Erro", "Por favor, selecione um diretório para salvar o vídeo.")
        return

    def run_download(link_id):
        try:
            command = ["yt-dlp", "-o", os.path.join(save_path, "%(title)s.%(ext)s"), link]
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

            for line in process.stdout:
                update_progress(link_id, line.strip())

            process.wait()
            if process.returncode == 0:
                update_progress(link_id, "Download concluído!")
                messagebox.showinfo("Sucesso", "O vídeo foi baixado com sucesso!")
            else:
                raise subprocess.CalledProcessError(process.returncode, command)
        except subprocess.CalledProcessError as e:
            update_progress(link_id, f"Erro: {e}")
            messagebox.showerror("Erro", f"Falha ao baixar o vídeo: {e}")
        except Exception as e:
            update_progress(link_id, f"Erro inesperado: {e}")
            messagebox.showerror("Erro", f"Erro inesperado: {e}")

    link_id = len(downloads)
    downloads[link_id] = {
        "link": link,
        "status": "Iniciando..."
    }
    update_download_list()

    threading.Thread(target=run_download, args=(link_id,)).start()

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

def update_progress(link_id, message):
    downloads[link_id]["status"] = message
    update_download_list()

def update_download_list():
    download_listbox.delete(0, tk.END)
    for link_id, info in downloads.items():
        download_listbox.insert(tk.END, f"{info['link']} - {info['status']}")

# Configuração da janela principal
root = tk.Tk()
root.title("Downloader de Vídeos")
root.geometry("600x400")
root.resizable(False, False)

# Variáveis
folder_path = tk.StringVar()

# Layout
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

link_label = tk.Label(frame, text="Link do vídeo:")
link_label.grid(row=0, column=0, sticky="w")

link_entry = tk.Entry(frame, width=50)
link_entry.grid(row=0, column=1, padx=5, pady=5)

folder_label = tk.Label(frame, text="Salvar em:")
folder_label.grid(row=1, column=0, sticky="w")

folder_entry = tk.Entry(frame, textvariable=folder_path, width=50)
folder_entry.grid(row=1, column=1, padx=5, pady=5)

browse_button = tk.Button(frame, text="Procurar", command=select_folder)
browse_button.grid(row=1, column=2, padx=5, pady=5)

download_button = tk.Button(frame, text="Baixar", command=download_video)
download_button.grid(row=2, column=1, pady=10)

progress_label = tk.Label(frame, text="Downloads em andamento:")
progress_label.grid(row=3, column=0, columnspan=3, pady=10, sticky="w")

download_listbox = tk.Listbox(frame, height=10, width=70)
download_listbox.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Loop principal
root.mainloop()
