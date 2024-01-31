import subprocess

command = 'start cmd /c scenedetect -i "D:/Videos/test/Landmine with Sign.mp4" -o "D:/Videos/test" split-video'

try:
    subprocess.Popen(command, shell=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")