import os.path
from tkinter import *
import datetime
import tkinter as tk
import customtkinter
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo
import pygame
from pygame import mixer
from moviepy.video.io.VideoFileClip import VideoFileClip

pygame.init()

def start_welcome_sound():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Assets/Close.mp3")
    pygame.mixer.music.play()

class MP4Player(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller


        lower_frame = customtkinter.CTkFrame(self)
        lower_frame.pack(fill="both", side=BOTTOM)


        video_player = TkinterVideo(self, scaled=True)
        video_player.pack(expand=True, fill="both")

        # functions

        # update_duration
        def update_duration(event):
            duration = video_player.video_info()["duration"]
            end_time["text"] = str(datetime.timedelta(seconds=duration))
            progress_slider["to"] = duration
            pygame.mixer.music.play(loops=0, start=int(progress_slider.get()))

        # update scale
        def update_scale(event):
            progress_value.set(video_player.current_duration())

        # load_video
        def load_video():
            file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3"), ("Video Files", "*.mp4")])
            mp3_path = file_path.replace(".mp4", ".mp3")
            clip = VideoFileClip(file_path)
            if file_path:
                video_player.load(file_path)
                progress_slider.configure(to=clip.duration, from_=0)
                play_pause_button["text"] = "Play"
                progress_value.set(0)
                play_file(mp3_path)

        # load audio
        def play_file(file_path):
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play(loops=0)

        # seek
        def seek(value):
            video_player.seek(int(value))

        # skip
        def skip(value: int):
            video_player.seek(int(progress_slider.get()) + value)
            progress_value.set(progress_slider.get() + value)

        # play_pause
        def play_pause():
            if video_player.is_paused():
                video_player.play()
                pygame.mixer.music.unpause()
                play_pause_button.configure(text="Pause")
            else:
                video_player.pause()
                pygame.mixer.music.pause()
                play_pause_button.configure(text="Play")

        # video_ended
        def video_ended(event):
            progress_slider.set(progress_slider["to"])
            play_pause_button["text"] = "Play"
            progress_slider.set(0)

        # Create Volume Function
        def volume(x):
            pygame.mixer.music.set_volume(volume_slider.get())
            # Get Current Volume
            current_volume = pygame.mixer.music.get_volume()
            # slider_label.config(text=current_volume * 100)


        # variables

        start_time = customtkinter.CTkLabel(self, text=str(datetime.timedelta(seconds=0)))
        start_time.pack(side="left")

        progress_value = tk.IntVar(self)

        progress_slider = customtkinter.CTkSlider(self, variable=progress_value, from_=0, to=100, command=seek)
        progress_slider.pack(side="left", fill="x", expand=True)

        end_time = tk.Label(self, text=str(datetime.timedelta(seconds=0)))
        end_time.pack(side="left")


        # buttons
        back_button = customtkinter.CTkButton(lower_frame,
                                              text="<-",
                                              width=50,
                                              command=lambda: [controller.show_frame("SelectionPage"),
                                                               start_welcome_sound()])
        back_button.pack(fill="both", side="right", padx=10, pady=5)

        load_button = customtkinter.CTkButton(lower_frame, text="Browse", command=lambda: [load_video()])
        load_button.pack(fill="both", side="right", padx=10, pady=5)

        # Create volume slider
        volume_slider = customtkinter.CTkSlider(lower_frame, from_=0, to=1, command=volume)
        volume_slider.pack(fill="both", side="right", padx=10, pady=5)

        # video_player = TkinterVideo(self, scaled=True)
        # video_player.pack(expand=True, fill="both")

        play_pause_button = customtkinter.CTkButton(lower_frame, text="Play", width=50, command=lambda: [play_pause()])
        play_pause_button.pack(fill="both", side="left", padx=10, pady=5)

        back_button = customtkinter.CTkButton(lower_frame, text="<<", width=50, command=lambda : [skip(-5)]).pack(side="left", padx=10, pady=5)
        forward_button = customtkinter.CTkButton(lower_frame, text=">>", width=50, command=lambda : [skip(+5)]).pack(side="left", padx=10, pady=5)


        video_player.bind("<<Duration>>", update_duration)
        video_player.bind("<<SecondChanged>>", update_scale)
        video_player.bind("<<Ended>>", video_ended)