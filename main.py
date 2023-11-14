from datetime import datetime
from os import walk, system, path, mkdir
from subprocess import Popen
from time import sleep

class Video:
    Name : str
    SizeBefore : float
    SizeAfter : float
    InputPath : str
    OutputPath : str

    def __init__(self, name, size, path : str):
        self.Name = name
        self.SizeBefore = round(size / 1024, 2)
        self.SizeAfter = None
        self.InputPath = path
        self.OutputPath = path.replace("input", "output")
        self.create_output_dir()

    def get_input_path(self):
        return self.InputPath + "/" + self.Name

    def get_output_path(self):
        return self.OutputPath + "/" + self.Name

    def create_output_dir(self):
        if self.OutputPath != "./output":
            try:
                mkdir(self.OutputPath)
            except:
                pass

    def set_size_after(self, size):
        self.SizeAfter = round(size / 1024, 2)

    def generate_log(self, inital_time):
        return f"{ datetime.today() } | { self.Name } | { self.SizeBefore }kb -> { self.SizeAfter }kb | { datetime.now() - inital_time }"

class VideoFile:
    Name : str
    Path : str

    def __init__(self, name, path):
        self.Name = name
        self.Path = path

def compress_video(video : Video):
    ffmpeg_params = [
        "ffmpeg",
        "-i",
        video.get_input_path(),
        "-crf",
        "22",
        "-threads",
        "8",
        "-c:v",
        "libx264",
        "-vf",
        "scale=-2:720",
        video.get_output_path()
    ]

    process = Popen(ffmpeg_params)
    process.wait()

def extract_videos(source : str):
    videos = []

    for path, _, file in walk(f"./{ source }"):
        for file_name in file:
            if ".mp4" in file_name or ".mkv" in file_name:
                path_formatted = path.replace("\\", "/")
                videos.append(VideoFile(file_name, path_formatted))

    return videos

def get_videos():
    input_videos  = extract_videos("input")
    output_videos = extract_videos("output")
    videos = []

    output_videos_list = [ output_video.Name for output_video in output_videos ]

    for input_video in input_videos:
        if input_video.Name not in output_videos_list:
            video = Video(
                input_video.Name,
                path.getsize(f"{ input_video.Path }/{ input_video.Name }"),
                input_video.Path
            )
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
        video.set_size_after(
            path.getsize(video.get_output_path())
        )
        videos_logs.append(video.generate_log(initial))

    system("clear")
    system("cls")
    save_logs(videos_logs)
    sleep(8)


if __name__ == "__main__":
    main()
