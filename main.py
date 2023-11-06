from subprocess import Popen
from os import walk

def compress_video(file_name : str):
    ffmpeg_params = [
        "ffmpeg",
        "-i",
        f"input/{ file_name }",
        "-crf",
        "30",
        "-c:v",
        "libvpx-vp9",
        "-vf",
        "scale=-2:720",
        f"output/{ file_name }"
    ]

    process = Popen(ffmpeg_params)
    process.wait()

def extract_files():
    i = 0
    files = []

    for _, _, file in walk("./input"):
        if i == 0:
            files.append(file)
        i += 1

    return files[0]

def extract_video_files_names(files_list : list):
    videos_names = []

    for file_name in files_list:
        if ".mp4" in file_name:
            videos_names.append(file_name)
    
    return videos_names

if __name__ == "__main__":
    videos_names = extract_video_files_names(extract_files())

    for video in videos_names:
        compress_video(video)
