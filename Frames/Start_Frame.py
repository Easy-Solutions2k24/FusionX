import sys

import customtkinter
from PIL import Image, ImageTk
import pygame
import os

# initialize Pygame Mixer
pygame.mixer.init()


def play_sound_start_page():
    pygame.mixer.music.load("Assets/Welcome.mp3")
    pygame.mixer.music.play()

def selection_sound():
    pygame.mixer.music.load("Assets/Open.mp3")
    pygame.mixer.music.play()

def completion_sound():
    pygame.mixer.music.load("Assets/Close.mp3")
    pygame.mixer.music.play()


def play_sound_start_button():
    pygame.mixer.music.load("Assets/Open.mp3")
    pygame.mixer.music.play()


class StartPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        play_sound_start_page()

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
        file_with_path = os.path.join("Assets/3.jpeg")
        welcome_image = Image.open(file_with_path)
        welcome_image_resized = welcome_image.resize(size=(500, 280))
        welcome_photo = ImageTk.PhotoImage(welcome_image_resized)

        # image_label = ttk.Label(labelframe, image=welcome_photo, style="Avatar.TLabel")
        # image_label.pack(expand=True, fill="both")

        welcome_photo_label = customtkinter.CTkLabel(labelframe, image=welcome_photo, text="")
        welcome_photo_label.image = welcome_photo

        # label1.place(x=35, y=10)
        welcome_photo_label.pack(expand=True, padx=0, pady=(50, 20))

        welcome_description = customtkinter.CTkLabel(labelframe,
                                    text="CLICK ON THE BUTTONS BELOW TO NAVIGATE", font=("Arial", 16, "bold"))
        welcome_description.pack(expand=True, anchor="center")

        # start button
        start_button = customtkinter.CTkButton(labelframe,
                            text="Start",
                            command=lambda: [controller.show_frame("SelectionPage"), play_sound_start_button()])
        start_button.pack(expand=True, fill="y", pady=(30, 10))

        # calling exit_function (lambda function)
        exit_button = customtkinter.CTkButton(labelframe,
                            text="Exit",
                            command=lambda : sys.exit())
        exit_button.pack(expand=True, fill="y", pady=(10, 60))
