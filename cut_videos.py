#from scenedetect import detect, ContentDetector, split_video_ffmpeg
import subprocess

def cut(directory, output_dir, video_name):
    if type(video_name) == list:
        full_directory = []
        for vid in video_name:
            full_directory.append(f"{directory}/{vid}")
    else:
        full_directory = video_name
    
    for vid in full_directory:
        command = f'start /wait cmd /c scenedetect -i "{vid}" -o "{output_dir}" split-video'
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print("Error:", e.stderr)