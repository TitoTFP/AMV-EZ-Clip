import scenedetect
import os
import pathlib

def cut(directory: str, output_dir: str, video_name: str, seperate_clips_status: int):    
    if type(video_name) == list:
        full_directory = []
        for vid in video_name:
            full_directory.append(f"{directory}/{vid}")
    else:
        full_directory = video_name
    
    scene_manager = scenedetect.SceneManager()
    scene_manager.add_detector(scenedetect.AdaptiveDetector())
    
    for vid in full_directory:
        if seperate_clips_status == 1:
            output_folder = f"{output_dir}/{os.path.split(vid)[1].split(".")[0]}"
            folder_path = pathlib.Path(output_folder)
            folder_path.mkdir(parents=True, exist_ok=True)
            os.chdir(output_folder)
        else:
            os.chdir(output_dir)
        
        video = scenedetect.open_video(vid)
        scene_manager.detect_scenes(video)
        scene_list = scene_manager.get_scene_list()
        scenedetect.split_video_ffmpeg(vid, scene_list, show_progress=True)
        
        """
        command = f"start /wait cmd /k python ./_internal/split_to.py {output_dir.replace(" ", str(random_number))} {vid.replace(" ", str(random_number))} {seperate_clips_status} {random_number}"
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        """
        