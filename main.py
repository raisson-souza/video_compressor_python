from subprocess import Popen
from os import walk, system
from datetime import datetime

def compress_video(file_name : str):
    ffmpeg_params = [
        "ffmpeg",
        "-i",
        f"input/{ file_name }",
        "-crf",
        "22",
        "-threads",
        "8",
        "-c:v",
        "libx264",
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

def save_logs(logs : list):
    log_file = open("logs.txt", "a")

    for log in logs:
        log_file.write(log)

    log_file.close()

if __name__ == "__main__":
    videos_names = extract_video_files_names(extract_files())
    videos_logs = []

    for video in videos_names:
        initial = datetime.now()
        compress_video(video)
        videos_logs.append(f"{ datetime.today() } | { video }: { datetime.now() - initial }\n")
        system("clear")

    save_logs(videos_logs)
