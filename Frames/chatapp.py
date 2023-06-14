import tkinter as tk
import customtkinter
from tkinter import ttk
import requests
from message_window import MessageWindow
import pygame

messages = [{"message": "Hello, world", "date": 15498487}]
message_labels = []  # will contain labels


def message_sent_sound():
    pygame.mixer.music.load("Assets/iPhone Text Message Sent.mp3")
    pygame.mixer.music.play()


def start_welcome_sound():
    pygame.mixer.music.load("Assets/Close.mp3")
    pygame.mixer.music.play()


class Chat(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.message_window = MessageWindow(self)
        self.message_window.grid(row=0, column=0, sticky="NSEW", pady=5)

        input_frame = customtkinter.CTkFrame(self)  # input frame
        input_frame.grid(row=1, column=0, sticky="EW")

        self.message_input = customtkinter.CTkTextbox(input_frame, height=3)
        self.message_input.pack(expand=True, fill="both", side="left", padx=(0, 10))

        message_submit = customtkinter.CTkButton(input_frame,
                                    text="Send",
                                    command=lambda: [self.post_message(), message_sent_sound()])
        message_submit.pack(pady=5)

        message_fetch = customtkinter.CTkButton(input_frame,
                                   text="Fetch",
                                   command=self.get_messages)  # fetch button
        message_fetch.pack(pady=5)

        welcome_button = customtkinter.CTkButton(input_frame,
                                    text="Back",
                                    command=lambda: [controller.show_frame("SelectionPage"), start_welcome_sound()])
        welcome_button.pack(pady=5)

        self.message_window.update_message_widgets(messages, message_labels)

    def post_message(self):
        body = self.message_input.get("1.0", "end").strip()
        requests.post("http://167.99.63.70/message", json={"message": body})
        self.message_input.delete("1.0", "end")
        self.get_messages()

    def get_messages(self):
        global messages
        messages = requests.get(
            "http://167.99.63.70/messages").json()  # """http://167.99.63.70/messages""" address of API, as data comes back as object, all we want is the message
        self.message_window.update_message_widgets(messages, message_labels)
        self.after(150, lambda: self.message_window.yview_moveto(1.0))

