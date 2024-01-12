import tkinter as tk
from pytube import YouTube
from pytube.cli import on_progress

def baixar_audio(link):
    try:
        yt = YouTube(link, on_progress_callback=on_progress)
        audio_stream = yt.streams.filter(only_audio=True).first()
        output_path = r"C:\Users\EA\Desktop\projetoMP3\MP3extraidos"
        audio_stream.download(output_path)
        label_status.config(text="Concluído!")
    except Exception as e:
        label_status.config(text=f"Erro: {str(e)}")

def converter():
    link = entry_link.get()
    if link:
        baixar_audio(link)
    else:
        label_status.config(text="Digite um link válido!")

root = tk.Tk()
root.title("Conversor YouTube MP4 para MP3")

label_instrucao = tk.Label(root, text="Digite o link do vídeo do YouTube:")
label_instrucao.pack(pady=12)

entry_link = tk.Entry(root, width=40)
entry_link.pack(pady=15)

button_converter = tk.Button(root, text="Converter", command=converter)
button_converter.pack(pady=10)

label_status = tk.Label(root, text="")
label_status.pack(pady=15)

root.mainloop()

