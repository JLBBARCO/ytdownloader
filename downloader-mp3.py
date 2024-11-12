import os
import subprocess
import yt_dlp

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("FFmpeg já está instalado.")
    except subprocess.CalledProcessError:
        print("FFmpeg não encontrado. Instalando...")
        install_ffmpeg()

def install_ffmpeg():
    if os.name == 'nt':
        url = 'https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n5.0-latest-win64-gpl.zip'
        os.system(f"curl -L {url} -o ffmpeg.zip")
        os.system("tar -xf ffmpeg.zip -C C:\\ffmpeg")
        os.system("setx PATH \"%PATH%;C:\\ffmpeg\\bin\"")
        print("FFmpeg instalado com sucesso.")
    else:
        print("Por favor, instale o FFmpeg manualmente.")

def baixar_audio(url):
    check_ffmpeg()
    caminho_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(caminho_downloads, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f'Download concluído! O áudio foi salvo em: {caminho_downloads}')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

if __name__ == "__main__":
    while True:
        url = input('Cole aqui sua URL para baixar em MP3: ')
        baixar_audio(url)
        repeat = input('Deseja baixar outro áudio? (s/n): ')
        if repeat.lower() != 's':
            break
