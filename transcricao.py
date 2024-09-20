import whisper
from tkinter import filedialog

def transcricao():
    arquivo_de_audio = filedialog.askopenfilename(filetypes=[("Arquivos de Áudio", "*.mp3 *.wav")])

    if not arquivo_de_audio:
        print("Nenhum arquivo selecionado")
        return
    
    modelo = whisper.load_model("small")
    texto = modelo.transcribe(f"{arquivo_de_audio}")
    print(texto["text"])