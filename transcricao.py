import whisper
from tkinter import filedialog

def transcricao():
    """
    Função que realiza a transcrição de um arquivo de áudio (MP3 ou WAV) utilizando o modelo Whisper.

    Esta função utiliza a biblioteca `tkinter` para abrir uma caixa de diálogo que permite ao usuário selecionar
    um arquivo de áudio. Após a seleção do arquivo, a função carrega o modelo pré-treinado do Whisper 
    (tamanho "small") para realizar a transcrição do áudio.

    Retorno:
    - Não há retorno explícito. O texto transcrito é impresso no console.
    """
    arquivo_de_audio = filedialog.askopenfilename(filetypes=[("Arquivos de Áudio", "*.mp3 *.wav")])

    if not arquivo_de_audio:
        print("Nenhum arquivo selecionado")
        return
    
    modelo = whisper.load_model("small")
    texto = modelo.transcribe(f"{arquivo_de_audio}")
    print(texto["text"])

def main():
    """
    Faz a chamada da função transcricao
    """
    transcricao()

if __name__ == "__main__":
    main()