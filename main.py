from datetime import datetime
from os import walk, system, path, mkdir, makedirs
from subprocess import Popen
from time import sleep
from shutil import copyfile

class Video:
    Name : str
    SizeBefore : float
    SizeAfter : float
    InputPath : str
    OutputPath : str
    CompressionPercentage : int

    def __init__(self, name, size, path : str):
        self.Name = name
        self.SizeBefore = Video.parse_mb_size(size)
        self.SizeAfter = None
        self.CompressionPercentage = None
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
                if self.OutputPath.count("/") > 2:
                    makedirs(self.OutputPath)
                else:
                    mkdir(self.OutputPath)
            except FileExistsError or OSError:
                pass
            except Exception as ex:
                Log.error_log(f"Houve um erro ao criar a pasta de destino. Erro: { ex }", self.Name)

    def set_size_after(self, size):
        parsed_size = Video.parse_mb_size(size)
        self.SizeAfter = parsed_size
        self.CompressionPercentage = 100 - int((parsed_size * 100) / self.SizeBefore)

    def generate_log(self, inital_time):
        return Log(self.Name, self.SizeBefore, self.SizeAfter, inital_time, self.CompressionPercentage)

    @staticmethod
    def parse_mb_size(byte_size):
        return round((byte_size / 1024) / 1000, 2)

class VideoFile:
    Name : str
    Path : str

    def __init__(self, name, path):
        self.Name = name
        self.Path = path

def compress_video(video : Video):
    '''Realiza a compressão de um vídeo.'''

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
    '''
    Extrai vídeos de algum local, seja ele de entrada ou de saída.\n
    Realiza o tratamento para somente capturar vídeos MP4 ou MKV.
    '''

    videos = []

    for path, _, file in walk(f"./{ source }"):
        for file_name in file:
            if ".mp4" in file_name or ".mkv" in file_name:
                path_formatted = path.replace("\\", "/")
                videos.append(VideoFile(file_name, path_formatted))

    return videos

def get_videos(minumum_video_size_compression : int):
    '''Captura e mapeia vídeos válidos para compressão em INPUT.'''

    def perform_copy(input_path : str, output_path : str, video_name : str):
        try:
            if output_path.count("/") > 2:
                makedirs(output_path)
            else:
                mkdir(output_path)
            copyfile(f"{ input_path }/{ video_name }", f"{ output_path }/{ video_name }")
        except FileExistsError or OSError:
            try:
                copyfile(f"{ input_path }/{ video_name }", f"{ output_path }/{ video_name }")
            except Exception as ex:
                Log.error_log(f"Não foi possível copiar um vídeo mais leve que a compressão mínima. Erro: { ex }", video_name)
        except Exception as ex:
            Log.error_log(f"Não foi possível copiar um vídeo mais leve que a compressão mínima. Erro: { ex }", video_name)

    input_videos  = extract_videos("input")
    output_videos = extract_videos("output")
    videos = []

    output_videos_list = [ output_video.Name for output_video in output_videos ]

    for input_video in input_videos:
        if input_video.Name not in output_videos_list:
            video_size = path.getsize(f"{ input_video.Path }/{ input_video.Name }")
            output_video_path = str(input_video.Path).replace('input', 'output')
            if video_size > minumum_video_size_compression and minumum_video_size_compression != 0:
                videos.append(
                    Video(
                        input_video.Name,
                        video_size,
                        input_video.Path
                    )
                )
            else:
                perform_copy(input_video.Path, output_video_path, input_video.Name)

    return videos

class Log:
    Name : str
    SizeBefore : float
    SizeAfter : float
    CompressionTime : datetime
    CompressionPercentage : int

    def __init__(self, name, size_before, size_after, initial_time, compression_percentage):
        self.Name = name
        self.SizeBefore = size_before
        self.SizeAfter = size_after
        self.CompressionTime = datetime.today() - initial_time
        self.CompressionPercentage = compression_percentage

    def generate_log(self):
        def parse_compression_time(compression_time : datetime):
            def render(time):
                time = str(time)
                return time if len(time) == 2 else f"0{ time }"

            minutes = int(compression_time.seconds / 60)
            seconds = compression_time.seconds
            for _ in range(0, minutes):
                seconds -= 60
            seconds = render(seconds)
            minutes = render(minutes)
            microseconds = render(str(compression_time.microseconds)[0:2])

            return f"{ minutes }:{ seconds }:{ microseconds }"

        now = Log.parse_time(datetime.today())
        parsed_compression_time = parse_compression_time(self.CompressionTime)
        return f"{ now } | { self.Name } | { self.SizeBefore }mb -> { self.SizeAfter }mb | ({ self.CompressionPercentage }%) | { parsed_compression_time }"

    @staticmethod
    def parse_time(time : datetime):
        return f"{ str(time).split(' ')[0] } { str(time).split(' ')[1][0:8] }"

    @staticmethod
    def error_log(error, video_name="vídeo desconhecido"):
        error_msg = f"!ERRO! { Log.parse_time(datetime.today()) } ( { video_name } ) -> { error }"
        Log.save_log(error_msg)

    @staticmethod
    def save_log(log_msg):
        log_file = open("logs.txt", "a")

        log_file.write(f"{ log_msg }\n")
        print(log_msg)

        log_file.close()

def save_logs(logs : list):
    for log in logs:
        log_msg = log.generate_log()
        Log.save_log(log_msg)

def get_minimum_video_size_compression():
    '''
    Captura o tamanho mínimo de compressão de vídeo configurado pelo usuário.\n
    Valor em bytes.
    '''

    def wrong_config_log():
        Log.error_log("Tamanho mínimo de compressão mal configurado.")

    try:
        file = open("CONFIG.txt", "r")
        lines = file.readlines()
        minimum_video_size_compression = lines[0].split("=")[1]
        if lines[0].split("=")[0] == "MINIMUM_VIDEO_SIZE_COMPRESSION":
            return int(minimum_video_size_compression) * (10 ** 6)
        wrong_config_log()
        return 0
    except:
        wrong_config_log()
        return 0
    finally:
        file.close()

def main():
    minimum_video_size_compression = get_minimum_video_size_compression()
    videos = get_videos(minimum_video_size_compression)
    videos_logs = []

    if len(videos) == 0:
        print("Nenhum vídeo a ser comprimido.")
        return

    for video in videos:
        try:
            initial = datetime.now()
            compress_video(video)
            video.set_size_after(path.getsize(video.get_output_path()))
            videos_logs.append(video.generate_log(initial))
        except Exception as ex:
            Log.error_log(ex, video.Name)

    system("clear")
    system("cls")
    save_logs(videos_logs)
    sleep(8)

if __name__ == "__main__":
    main()