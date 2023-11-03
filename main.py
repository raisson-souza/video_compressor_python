import subprocess
import os

def compress_video(input_file, output_file):
    # Define os parâmetros do ffmpeg para a compressão.
    ffmpeg_params = [
        "ffmpeg",
        "-i",
        input_file,
        "-crf",
        "30",
        "-c:v",
        "libvpx-vp9",
        "-vf",
        "scale=-2:360",
        output_file
    ]

    # Executa o comando ffmpeg.
    process = subprocess.Popen(ffmpeg_params)
    process.wait()

    # Verifica se o comando ffmpeg foi bem-sucedido.
    return process.returncode == 0


if __name__ == "__main__":
    input_file = "teste.mp4"

    compress_video(input_file, "output.mp4")
