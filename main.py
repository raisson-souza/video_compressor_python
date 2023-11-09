from subprocess import Popen
from os import walk, system, path
from datetime import datetime
from time import sleep

class Video:
    Name : str
    SizeBefore : float
    SizeAfter : float

    def __init__(self, name, size):
        self.Name = name
        self.SizeBefore = round(size / 1024, 2)
        self.SizeAfter = None

    def set_size_after(self, size):
        self.SizeAfter = round(size / 1024, 2)

    def generate_log(self, inital_time):
        return f"{ datetime.today() } | { self.Name } | { self.SizeBefore }kb -> { self.SizeAfter }kb | { datetime.now() - inital_time }"

def compress_video(video : Video):
    ffmpeg_params = [
        "ffmpeg",
        "-i",
        f"input/{ video.Name }",
        "-crf",
        "22",
        "-threads",
        "8",
        "-c:v",
        "libx264",
        "-vf",
        "scale=-2:720",
        f"output/{ video.Name }"
    ]

    process = Popen(ffmpeg_params)
    process.wait()

def extract_videos(source : str):
    videos = []

    for _, _, file in walk(f"./{ source }"):
        for file_name in file:
            if ".mp4" in file_name or ".mkv" in file_name:
                videos.append(file_name)
        break

    return videos

def get_videos():
    input_videos  = extract_videos("input")
    output_videos = extract_videos("output")
    videos = []

    for video_name in input_videos:
        if video_name not in output_videos:
            video = Video(video_name, path.getsize((f"./input/{ video_name }")))
            videos.append(video)

    return videos

def save_logs(logs : list):
    log_file = open("logs.txt", "a")

    for log in logs:
        log_file.write(f"{ log }\n")
        print(log)

    log_file.close()

def main():
    videos = get_videos()
    videos_logs = []

    if len(videos) == 0:
        print("Nenhum vídeo a ser comprimido.")
        return

    for video in videos:
        initial = datetime.now()
        compress_video(video)
        video.set_size_after(path.getsize((f"./output/{ video.Name }")))
        videos_logs.append(video.generate_log(initial))

    system("clear")
    system("cls")
    save_logs(videos_logs)
    sleep(8)


if __name__ == "__main__":
    main()
