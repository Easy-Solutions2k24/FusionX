import tkinter as tk                # python 3
import customtkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pygame
import os

# def play_sound_4():
#     playsound("PS5 Intro Theme Start Page 3.mp3", block=False)
#
# play_sound_4()


def start_welcome_sound():
    pygame.mixer.music.load("Assets/Open.mp3")
    pygame.mixer.music.play()


def start_media_player_sound():
    # pygame.mixer.music.load("./frames/PSP Startup 2.mp3")
    # pygame.mixer.music.play()
    pygame.mixer.music.stop()


def stop_sound():
    pygame.mixer.music.stop()


def stop_welcome_sound():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Assets/Welcome.mp3")
    pygame.mixer.music.play()


class SelectionPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller


        labelframe = customtkinter.CTkFrame(self)
        labelframe.pack(fill="both", expand=True, pady=(0, 0), padx=0)

        sidebar_frame = customtkinter.CTkFrame(master=labelframe, width=30, corner_radius=0, fg_color="gray75")
        sidebar_frame.pack(expand=True, fill="x", pady=(0, 0))

        cd = os.getcwd()
        file_with_path = os.path.join("Assets/Easy Solutions-logos_black_s_r.png")
        easy_solutions_image = Image.open(file_with_path)
        easy_solutions_image.resize(size=(10, 10))
        easy_solutions_photo = ImageTk.PhotoImage(easy_solutions_image)

        easy_solutions_photo_label = customtkinter.CTkLabel(sidebar_frame, image=easy_solutions_photo, text="")
        easy_solutions_photo_label.image = easy_solutions_photo

        # label1.place(x=35, y=10)
        easy_solutions_photo_label.pack(anchor="nw")

        cd = os.getcwd()
        # file_with_path = os.path.join("Assets/3.jpeg")
        # welcome_image = Image.open(file_with_path)
        # welcome_image_resized = welcome_image.resize(size=(500, 180))
        # welcome_photo = ImageTk.PhotoImage(welcome_image_resized)

        # image_label = ttk.Label(labelframe, image=welcome_photo, style="Avatar.TLabel")
        # image_label.pack(expand=True, fill="both")

        welcome_photo_label = customtkinter.CTkLabel(labelframe, text="Easy D", font=("Arial", 80), bg_color="darkgrey", corner_radius=10)
        # welcome_photo_label.image = welcome_photo

        # label1.place(x=35, y=10)
        welcome_photo_label.pack(expand=True, padx=40, pady=(53, 48), ipadx=50, ipady=40)

        # welcome_description = customtkinter.CTkLabel(labelframe,
        #                                 text="Welcome! Click on the buttons below to navigate. Enjoy......!")
        # welcome_description.pack(expand=True, anchor="center")


        # chatapp button calling show_timer function in app.py (lambda function)
        chatapp_button = customtkinter.CTkButton(labelframe,
                                    text="ChatApp",
                                    command=lambda: [controller.show_frame("Chat"), stop_sound()])
        chatapp_button.pack(pady=(10,10), ipadx=20)

        # map button calling show_timer function in app.py (lambda function)
        map_button = customtkinter.CTkButton(labelframe,
                                text="Navigator",
                                command=lambda: [controller.show_frame("MapView"), stop_sound()])
        map_button.pack(pady=(10, 10), ipadx=20)

        # media player button calling show_media_player function in app.py (lambda function)
        media_player_button = customtkinter.CTkButton(labelframe,
                                         text="Music Player",
                                         command=lambda: [controller.show_frame("MediaPlayer"), start_media_player_sound()])
        media_player_button.pack(pady=(10, 10), ipadx=20)

        # MP4_Player button
        mp4_player_button = customtkinter.CTkButton(labelframe,
                                                      text="Video Player",
                                                      command=lambda: [controller.show_frame("MP4Player"),
                                                                       start_media_player_sound()])
        mp4_player_button.pack(pady=(10, 10), ipadx=20)

        # chatapp button calling exit_function function in app.py (lambda function)
        back_button = customtkinter.CTkButton(labelframe,
                                 text="<-",
                                 command=lambda: [controller.show_frame("StartPage"), stop_welcome_sound()])
        back_button.pack(pady=(10, 50), ipadx=20)

        # plat button calling exit_function function in app.py (lambda function)
        # play_button = customtkinter.CTkButton(labelframe,
        #                          text="|> PLAY",
        #                          command=lambda: [start_welcome_sound()])
        # play_button.pack(side="left", padx=85, pady=20)
        #
        # # pause button calling exit_function function in app.py (lambda function)
        # pause_button = customtkinter.CTkButton(labelframe,
        #                         text="|| PAUSE",
        #                         command=lambda: [stop_sound()])
        # pause_button.pack(side="right", padx=85, pady=20)