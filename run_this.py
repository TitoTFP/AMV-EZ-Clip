import os
import customtkinter
from tkinter import filedialog
from tktooltip import ToolTip
import getpass
import cut_videos

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.video_dir_set = False
        self.output_dir_set = False
        
        # Title, Geometry, and columns
        self.title("AMV Edit EZ")
        self.geometry("500x500")
        self.columnconfigure((0, 1, 2), weight=1)
        
        # Buttons for selecting the uncutted videos
        self.scene_splitter = customtkinter.CTkLabel(self, text="Scene Splitter : ")
        self.scene_splitter.grid(row=0, column=0, sticky='we')
        
        self.scene_splitter_open_folder = customtkinter.CTkButton(self, text="Open File(s)/Folder", command=lambda : self.open_directory())
        self.scene_splitter_open_folder.grid(row=0, column=1, sticky='we', padx="3px")
        
        self.scene_splitter_output_folder = customtkinter.CTkButton(self, text="Output Folder", command=lambda : self.output_directory())
        self.scene_splitter_output_folder.grid(row=0, column=2, sticky='we', padx="3px")
        
        # Checkbox for selecting
        self.file_folder = customtkinter.CTkCheckBox(self, text="Open Folder Instead")
        self.file_folder.grid(row=1, column=1, pady="5px", padx="3px")
        ToolTip(self.file_folder, msg="Check this if you want to select folder instead of file(s)", delay=0.25)
        
        self.seperate_clips_c = customtkinter.CTkCheckBox(self, text="Seperate Cutted Clips")
        self.seperate_clips_c.grid(row=1, column=2, pady="5px", padx="3px")
        ToolTip(self.seperate_clips_c, msg="Check this if you want to seperate cutted videos into different folders", delay=0.25)
        
        # Execute Button
        self.execute_cut = customtkinter.CTkButton(self, text="Execute Cut!", command=lambda : self.video_cutting())
        self.execute_cut.grid(row=2, column=0, columnspan=3, sticky="we", padx="10px", pady="3px")
        
    def to_scene_splitter(self):
        print("Button Clicked!")
        
    def open_directory(self): 
        if self.file_folder.get() == 1:
            if self.video_dir_set == False:
                self.video_dir = filedialog.askdirectory(initialdir=f"C:/Users/{getpass.getuser()}")
                self.video_dir_set = True
            else:
                self.video_dir = filedialog.askdirectory()
            
            self.selected_video_name = os.listdir(self.video_dir)
            
        else:
            if self.video_dir_set == False:
                self.selected_video_name = filedialog.askopenfilenames(initialdir=f"C:/Users/{getpass.getuser()}")
                self.video_dir_set = True
            else:
                self.selected_video_name = filedialog.askopenfilenames()
            
            try:
                self.video_dir = os.path.split(self.selected_video_name[0])[0]
            except IndexError:
                pass
        
        try:
            self.file_label_1.destroy()
        except AttributeError:
            pass
        self.file_label_1 = customtkinter.CTkLabel(self, text=f"input : {self.video_dir}, selected : {len(self.selected_video_name)} file(s)")
        self.file_label_1.grid(row=3, column=0, columnspan=3)
        
    def output_directory(self):
        if self.output_dir_set == False:
            self.output_vid_dir = filedialog.askdirectory(initialdir=f"C:/Users/{getpass.getuser()}")
            self.output_dir_set = True
        else:
            self.output_vid_dir = filedialog.askdirectory()
            
        try:
            self.file_label_output.destroy()
        except AttributeError:
            pass
        self.file_label_output = customtkinter.CTkLabel(self, text=f"output : {self.output_vid_dir}")
        self.file_label_output.grid(row=4, column=0, columnspan=3)
    
    def video_cutting(self):
        cut_videos.cut(self.video_dir, self.output_vid_dir, self.selected_video_name)

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()