import tkinter as tk                # python 3
import webbrowser
import customtkinter
import pygame
from module import StartPage, SelectionPage, MediaPlayer, Chat, MapView, MP4Player

"""***************************************************"""
# App appearance modifier
customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
"""***************************************************"""

"""***************************************************"""
# App Frame Switcher


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


def open_website():
    webbrowser.open("https://")
    print("open website button click")


def open_github():
    print("open github click")
    webbrowser.open("https://github.com/Dude100h/EasyZRCD.git")


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, SelectionPage, MediaPlayer, Chat, MapView, MP4Player):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

        def change_appearance_mode(new_appearance_mode: str):
            customtkinter.set_appearance_mode(new_appearance_mode)
            if new_appearance_mode == "Light":
                selection_sound()
            elif new_appearance_mode == "Dark":
                completion_sound()
            else:
                completion_sound()

        def change_scaling(new_scaling: str):
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            customtkinter.set_widget_scaling(new_scaling_float)
            customtkinter.set_window_scaling(new_scaling_float)
            if new_scaling == "80%":
                app.geometry("570x520")
                completion_sound()
            elif new_scaling == "90%":
                app.geometry("640x620")
                completion_sound()
            elif new_scaling == "100%":
                app.geometry("720x720")
                selection_sound()
            elif new_scaling == "110%":
                app.geometry("790x820")
                selection_sound()
            elif new_scaling == "120%":
                app.geometry("860x920")
                selection_sound()

        sidebar_frame = customtkinter.CTkFrame(master=container, width=80, corner_radius=0, fg_color="gray75")
        sidebar_frame.grid(pady=(5, 5))
        # sidebar_frame.grid_rowconfigure(4, weight=1)

        # sidebar_frame = customtkinter.CTkLabel(sidebar_frame, text="")
        # sidebar_frame.pack(expand=True, pady=(20, 0), padx=0)

        appearance_mode_label = customtkinter.CTkLabel(master=sidebar_frame, text="Appearance Mode:")
        appearance_mode_label.grid(row=0, column=0, padx=20, pady=(10, 0))

        appearance_mode_optionmenu = customtkinter.CTkOptionMenu(master=sidebar_frame,
                                                                 values=["Light", "Dark", "System"],
                                                                 command=change_appearance_mode)
        appearance_mode_optionmenu.grid(row=1, column=0, padx=20, pady=(10, 20))

        scaling_label = customtkinter.CTkLabel(master=sidebar_frame, text="UI Scaling:")
        scaling_label.grid(row=0, column=1, padx=20, pady=(10, 0))

        scaling_optionmenu = customtkinter.CTkOptionMenu(master=sidebar_frame,
                                                         values=["80%", "90%", "100%", "110%", "120%"],
                                                         command=change_scaling)
        scaling_optionmenu.set("100%")
        scaling_optionmenu.grid(row=1, column=1, padx=20, pady=(10, 20))

        git_label = customtkinter.CTkLabel(master=sidebar_frame, text="Git Button:")
        git_label.grid(row=0, column=2, padx=20, pady=(10, 0))

        git_button = customtkinter.CTkButton(sidebar_frame, text="Git Hub", command=lambda: [open_github(), selection_sound()])
        git_button.grid(row=1, column=2, padx=20, pady=(10, 20))

        website_label = customtkinter.CTkLabel(master=sidebar_frame, text="Website Button:")
        website_label.grid(row=0, column=3, padx=20, pady=(10, 0))

        website_button = customtkinter.CTkButton(sidebar_frame, text="Website", command=lambda: [open_website(), selection_sound()])
        website_button.grid(row=1, column=3, padx=20, pady=(10, 20))

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


app = App()
app.title("")
app.geometry("720x720")
app.resizable(False, False)
app.mainloop()
