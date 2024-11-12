import yt_dlp
import os

def baixar_video(url):
    # Obtém o caminho para a pasta de Downloads do usuário
    caminho_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(caminho_downloads, '%(title)s.%(ext)s'),
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f'Download concluído! O vídeo foi salvo em: {caminho_downloads}')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

if __name__ == "__main__":
    while True:
        url = input('Cole aqui sua URL para baixar em MP4: ')
        baixar_video(url)
        repeat = input('Deseja baixar outro vídeo? (s/n): ')
        if repeat.lower() != 's':
            break
