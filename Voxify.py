import os
from moviepy.editor import VideoFileClip

def convert_video_to_audio(video_path, output_path, format="mp3"):
    """Converte um vídeo em áudio no formato especificado."""
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(output_path, codec=format)
        print(f"Conversão concluída: {output_path}")
    except Exception as e:
        print(f"Erro durante a conversão: {e}")
    finally:
        if 'video' in locals():
            video.close()
        if 'audio' in locals():
            audio.close()

def validate_format(format):
    """Valida se o formato de saída é suportado."""
    supported_formats = ["mp3", "wav", "aac", "flac"]
    return format if format in supported_formats else "mp3"

if __name__ == "__main__":
    print("Bem-vindo ao Voxify - Conversor de Vídeo para Áudio!")
    print("Formatos suportados: mp3, wav, aac, flac")
    
    # Entrada do usuário
    video_file = input("Digite o caminho do vídeo (ex.: video.mp4): ").strip()
    if not os.path.exists(video_file):
        print("Erro: O arquivo de vídeo não foi encontrado.")
        exit(1)
    
    output_file = input("Digite o nome do arquivo de saída (ex.: audio.mp3): ").strip() or "output.mp3"
    format_choice = input("Escolha o formato (mp3, wav, aac, flac) [padrão: mp3]: ").lower().strip()
    format_choice = validate_format(format_choice or "mp3")
    
    # Executa a conversão
    convert_video_to_audio(video_file, output_file, format_choice)
    cd Downloads
python Voxify.py
